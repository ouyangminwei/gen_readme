from openai import OpenAI

import subprocess
import dotenv
import os


from dotter import Dotter
from tqdm.auto import tqdm

textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

list_of_files = subprocess.check_output("git ls-files", shell=True, encoding='utf-8').splitlines()

if (len(list_of_files) == 0):
    print("[*] `git ls-files` returned 0 files. please run `git add .` first")
    print("[*] Exiting...")
    exit(1)

def in_gitingore(file):
    if file in list_of_files:
        return False
    return True

def get_files():
    # walk through the directory and read all non binary file
    # files and return them as a list
    files = []
    for this_file in list_of_files:
        if not is_binary_string(open(this_file, 'rb').read(1024)):
            files.append(this_file)
    return files

def get_file_content(file):
    with open(file, 'r',encoding='utf-8') as f:
        return f.read()


def summary_project_file(files, client, system):
    output = ""
    for file in tqdm(files):
        content = get_file_content(file)
        prompt = f'\nFile: {file}\n{content}\n請簡短的總結這個文件在幹嘛，包含使用的套件，call的API，inherent的class等等\n'
        response = call_openai(client, prompt, system)
        output += f'\nFile: {file}\n{response}\n'
    return output

def call_openai(client:OpenAI, prompt, system, model="gpt-4o-mini", temperature=0.3) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.3,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content.strip()


def main():
    dotenv.load_dotenv(".env")
    client = OpenAI(api_key=str(os.getenv("OPENAI_API_KEY")))

    files = get_files()
    print(f"[*] Detected {len(files)} files")
    for each in files:
        print(f"    - {each}")
    input("Using above files to generate readme, press enter to continue...")


    system = "你是一個中文開發者，你正在做code reveiw，每一個code你需要看一次就可以記得所有的關鍵訊息。"
    prompt = summary_project_file(files, client, system)

    with Dotter("[*] Generating final result"):
        system = "你是一個中文開發者，你需要製作一份readme.md，讓其他人可以快速了解這個專案。"
        response = call_openai(client, prompt, system)

    print(response)
    print("="*50)
    userinput = input("以上是AI生成的readme.md 是否要儲存? [y/n]")
    if userinput.lower() == 'y':
        filename = input("請輸入檔名: ")
        with open(f'{filename}', 'w',encoding='utf-8') as f:
            f.write(response)
    else:
        print("You did not save the file. Exiting...")


if __name__ == '__main__':
    main()