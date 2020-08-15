UODA Batch 45 (CSE407 & CSE407L)CSE
Md.Rafiuzzaman Khan

    All
    Assigned
    Returned
    Missing

Class Test-3: CSE 407
Aug 12, 4:40 PM
Missing
Assignment-5: Python script
1
1 private comment
4
4 submission attachments
Aug 10, 11:59 PM
Turned in
Class Test-2: CSE-407
3
3 private comments
3
3 submission attachments
Jul 25, 5:05 PM
8 points out of possible 158/15Done late
Class assignment on Python class
4
4 private comments
2
2 submission attachments
Jul 22, 4:00 PM
Turned inDone late
Assignment-4: Python script
2
2 private comments
3
3 submission attachments
Jul 25, 11:59 PM
10 points out of possible 1010/10
Class test -1: CSE-407
3
3 submission attachments
Jul 15, 4:30 PM
10 points out of possible 1510/15
Assignment-3: Python Script
2
2 private comments
3
3 submission attachments
Jul 15, 11:59 PM
10 points out of possible 1010/10
Md.Rafiuzzaman Khan - Assignment-3: Python Script
Google Docs
assignment 3 updated code.py
Text
commonstr output updated.PNG
Image
2 private comments
Md.Rafiuzzaman KhanJul 15
Hello Mam,
I have submitted my assignment 3 , did you able the check it ?
Md.Rafiuzzaman KhanJul 15
Mam ,

i have updated my code and added regex to only except number in this format (+880-XXX-XXX-XXXX) also i have limited the network operator number in range from 5 to 9 .so it will only allow known operators mobile number .
please have a look .

Thank you.
CSE-407 MCQ Questions(10)
1
1 submission attachment
Jul 5, 4:20 PM
Turned inDone late
CSE-407 Theory Questions(15)
Jul 5, 1:00 PM
Turned inDone late
Assignment-2: Bash script
14
14 private comments
9
9 submission attachments
Jul 11, 2:25 PM
10 points out of possible 1010/10
Assignment-1:Bash script
2
2 private comments
2
2 submission attachments
Jun 20
10 points out of possible 1010/10
Expanded Assignment-3: Python Script

import sys
import re

# Name: Md.Rafiuzzaman Khan
# ID  : 011161017

# check if arguments were passed
if len(sys.argv) < 3:
    print('You must set phone number and email as commandline arguments!!!')
    print("Example: filename.py +880-171-305-6070  user@emailprovider.com ")
    exit()

# check if number is valid
def validate_number(value):
    rule = re.compile(r"^(?:\+880-)?[1][5-9]\d{1}-\d{3}-\d{4}$")
    if not rule.search(value):
        msg = u"Invalid mobile number.please provide the number in proper format! Example: +880-171-305-6070"
        print(msg)
        exit()

# phone number from command line arguments
phone =  str(sys.argv[1])
# email address from command line arguments
email = str(sys.argv[2])

# validating phone number in full format with dash +880-171-305-6070
validate_number(phone)



operator_code = phone[6:7]




# a simple function to find operator name based on operator code
def find_operator(operator_code):
    operator_switch = {
        "5": "Teletalk",
        "6": "Airtel",
        "7": "Grameen Phone",
        "8": "Robi",
        "9": "Banglalink"
    }
    return operator_switch.get(operator_code, "Unknown operator")


# for validating an Email
def check_email(email):
    # for validating an Email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    # and the string in search() method
    if (re.search(regex, email)):
        return 1

    else:
        return 0


if (check_email(email)) != 1:
    print("Please provide a valid email address")
    exit()

print("Output:")

print("It is", find_operator(operator_code), "Number")

username = email.split('@')[0]
domain = email.split('@')[1]

# hotmail domain filter
if domain.lower() == "hotmail.com":
    print("Hotmail is not acceptable")
else:
    print("Username:", username)
    print("Domain Name:", domain)

