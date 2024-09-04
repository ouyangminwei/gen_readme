# Project README Generator

## Overview
This project is designed to automatically generate a README file for your project by analyzing the contents of your codebase. It utilizes OpenAI's API to create a clear and concise README that helps others quickly understand your project.

## Features
- **Automatic File Scanning**: The script scans the project directory for non-binary files and reads their content.
- **OpenAI Integration**: It leverages OpenAI's language model to generate a README based on the collected file contents.
- **User Interaction**: After generating the README, the user is prompted to save the output to a `README.md` file.

## Requirements
- Python 3.x
- `dotenv` library for environment variable management
- `openai` library for API interaction

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install python-dotenv openai
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage
1. Run the script:
   ```bash
   python gen_readme.py
   ```

2. The script will scan the directory, generate a README based on the contents of your files, and display it in the console.

3. You will be prompted to save the generated README to a `README.md` file. Type `y` to save or `n` to exit without saving.

## Code Structure
- **`.env`**: Contains environment variables, specifically the OpenAI API key.
- **`gen_readme.py`**: The main script that handles file scanning, content reading, and interaction with the OpenAI API.
- **`README.md`**: The generated README file (created after running the script).

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- OpenAI for providing the API that powers the README generation.
- The Python community for the libraries used in this project.

---

This README serves as a guide to understanding and using the project effectively. If you have any questions or need further assistance, feel free to reach out!