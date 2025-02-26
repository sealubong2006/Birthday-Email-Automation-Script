# Birthday Email Automation Script

## Overview
This Python script automates the process of sending birthday wishes via email. It checks the current date, finds any matching birthdays from a CSV file, selects a random letter template, customizes it with the recipient's name, and sends it via email using SMTP.

## Requirements
- Python 3.x
- `pandas` library
- `smtplib` library
- `datetime` module
- `random` module
- Gmail account for sending emails

## Files Structure
```
|-- birthday_email.py
|-- birthdays.csv
|-- letter_templates/
|   |-- letter_1.txt
|   |-- letter_2.txt
|   |-- letter_3.txt
```

### `birthdays.csv` Format
The CSV file should contain the following columns:
```csv
name,email,year,month,day
John Doe,johndoe@example.com,1990,2,26
Jane Doe,janedoe@example.com,1985,3,15
```

### `letter_templates/`
This folder contains text files with birthday messages. The placeholder `[NAME]` is used where the recipient's name should be inserted.

## How It Works
1. The script reads `birthdays.csv` to check for any birthdays matching the current date.
2. If a birthday is found:
   - A random letter template is selected.
   - The `[NAME]` placeholder is replaced with the recipient’s actual name.
   - The email is sent via Gmail SMTP.
3. After sending, the template is restored to its original state by replacing the name back with `[NAME]`.

## Setup Instructions
1. Install dependencies:
   ```sh
   pip install pandas
   ```
2. Enable **Less Secure Apps** or generate an **App Password** for your Gmail account.
3. Modify the `my_email` and `password` variables in the script with your email credentials.
4. Deploy the script on **PythonAnywhere** or schedule it with `cron` or `Task Scheduler`.

## Running the Script
Run the script manually with:
```sh
python birthday_email.py
```

Or schedule it using a cron job (Linux/macOS):
```sh
0 9 * * * /usr/bin/python3 /path/to/birthday_email.py
```
This will run the script every day at 9 AM.

## Security Considerations
- Use an **App Password** instead of your actual Gmail password.
- Avoid hardcoding credentials in the script; use environment variables instead.
- Ensure your `birthdays.csv` file is kept secure and private.

## Deployment on PythonAnywhere
1. Upload the script, CSV file, and templates to your PythonAnywhere environment.
2. Schedule a daily task in PythonAnywhere’s Task Scheduler to run `birthday_email.py`.

## Troubleshooting
- If emails are not being sent, check the Gmail security settings for blocked sign-in attempts.
- Ensure the `birthdays.csv` file has the correct date format and data.
- If the script crashes due to missing data, verify the CSV file contents.

## License
This project is open-source and free to use.

