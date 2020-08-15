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

