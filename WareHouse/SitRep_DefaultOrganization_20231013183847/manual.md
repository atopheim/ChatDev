# ChatDev User Manual

## Introduction

Welcome to the ChatDev software! This user manual will guide you through the installation process and explain how to use the software to create a script that summarizes your work from Microsoft Calendar and GitHub.

## Installation

To install the ChatDev software, please follow the steps below:

1. Make sure you have Python installed on your computer. If not, you can download it from the official Python website: https://www.python.org/downloads/

2. Clone the ChatDev repository from GitHub using the following command:

   ```
   git clone https://github.com/chatdev/chatdev.git
   ```

3. Navigate to the cloned repository:

   ```
   cd chatdev
   ```

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

5. You are now ready to use the ChatDev software!

## Usage

To use the ChatDev software and create a script that summarizes your work, follow the steps below:

1. Open the `main.py` file in a text editor.

2. Modify the `read_events` function in the `calendar_reader.py` file to implement code that reads events from your Microsoft Calendar. Replace the placeholder code with the actual code to retrieve events from your calendar.

3. Modify the `read_commits` and `read_pull_requests` functions in the `github_reader.py` file to implement code that reads commit texts and pull request descriptions from your GitHub account. Replace the placeholder code with the actual code to retrieve commits and pull requests.

4. Save the modified files.

5. Run the `main.py` script by executing the following command:

   ```
   python main.py
   ```

6. The script will read events from your Microsoft Calendar and commit texts/pull request descriptions from your GitHub account. It will then generate a report summarizing your work.

7. The generated report will be printed in the console.

## Conclusion

Congratulations! You have successfully installed and used the ChatDev software to create a script that summarizes your work from Microsoft Calendar and GitHub. If you have any further questions or need assistance, please don't hesitate to contact our support team.