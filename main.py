######################
# Extra Hard Starting Project
# ######################
import smtplib as sm
import datetime as dt
import pandas as pd
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)

MY_EMAIL = "coolvinayhassani@gmail.com"
PASSWORD = "jvmlmtiyoczurmns"

data = pd.read_csv("birthdays.csv")

birthday_dic = {(data_row.month, data_row.day): data_row
                for (index, data_row) in data.iterrows()}

if today in birthday_dic:
    birthday_person = birthday_dic[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace(["NAME"], birthday_person["name"])

    with sm.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg="Subject:Happy Birthday"
                                f"\n\n{contents}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
