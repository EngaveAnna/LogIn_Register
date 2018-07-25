from validate_email import validate_email
import re

def mail_validation(addressToVerify):
    is_valid1 = validate_email(addressToVerify)
    is_valid2 = validate_email(addressToVerify, verify=True)

    #match1 = re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", addressToVerify) #https://www.scottbrady91.com/Email-Verification/Python-Email-Verification-Script

    is_valid3 = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", addressToVerify) #http://emailregex.com/

    if is_valid1 and is_valid2 and is_valid3!='None':
        print("Valid adress email")
        return True
    else:
        print('Invalid adress email')
        return False
