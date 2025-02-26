import pandas as pd
import smtplib
import datetime as dt
from random import *  # Importing random module to choose a random letter template

# Email and password for sending birthday emails
my_email = "johndoe@example.com"
password = "password"

# Getting today's date
today_date = dt.datetime.today()  # Current date and time
today = [today_date.month, today_date.day]  # Extracting month and day from today's date

# Reading the birthdays CSV file
df = pd.read_csv("birthdays.csv")  # Assuming the CSV contains columns like "name", "month", "day", and "email"

# Finding the birthday row matching today's date
birthday = df.loc[(df["month"] == today[0]) & (df["day"] == today[1])]  # Filtering for today’s date

# If there's no birthday today, exit the script
if birthday.empty:
    exit()

else:
    # Extracting the name and email from the filtered birthday data
    name = birthday["name"].values[0]  # Getting the name of the person
    email = birthday["email"].values[0]  # Getting the email of the person

    # List of letter templates to choose from
    l_1 = "./letter_templates/letter_1.txt"
    l_2 = "./letter_templates/letter_2.txt"
    l_3 = "./letter_templates/letter_3.txt"
    letters = [l_1, l_2, l_3]  # Storing paths to letter templates in a list

    # Choosing a random letter template
    random_letter = choice(letters)  # Randomly selecting a letter template from the list

    with open(random_letter, "r+") as letter:  # Opening the chosen letter template in read-write mode
        letter_main = letter.readlines()  # Reading all lines of the letter template into a list
        letter.seek(0)  # Moving the cursor to the start of the file to overwrite content

        # Replacing placeholder "[NAME]" in the letter with the recipient's name
        for i in range(len(letter_main)):
            if "[NAME]" in letter_main[i]:
                letter_main[i] = letter_main[i].replace("[NAME]", name)

        letter.writelines(letter_main)  # Writing the modified content back into the file
        letter.truncate()  # Removing any extra content beyond the written lines
        letter.seek(0)  # Moving the cursor to the beginning again before reading the file

        # Reading the final content of the letter after modification
        letter = letter.read()

        # Sending the email with the modified letter content
        with smtplib.SMTP("smtp.gmail.com") as connection:  # Connecting to Gmail's SMTP server
            connection.starttls()  # Encrypting the connection
            connection.login(user=my_email, password=password)  # Logging in to the email account
            # Sending the email with subject and letter content
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday\n\n{letter}",
            )

    # Opening the letter template again to revert the name placeholder "[NAME]" back
    with open(random_letter, "r+") as letter:
        letter_main = letter.readlines()  # Reading all lines of the letter
        letter.seek(0)  # Moving the cursor to the beginning for writing

        # Reverting any changes of replacing the recipient's name with "[NAME]" back to the placeholder
        for i in range(len(letter_main)):
            if name in letter_main[i]:  # If the actual name is found in the letter
                letter_main[i] = letter_main[i].replace(name, "[NAME]")  # Reverting it back to placeholder

        letter.writelines(letter_main)  # Writing the reverted content back to the file
        letter.seek(0)  # Moving the cursor back to the beginning before further actions
