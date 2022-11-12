import re


def password_evaluate(pw):
    print("Criteria")
    print("Length (At least 16 characters): " + check_pass_len(pw))
    print("Contains at least 1 number: " + check_pass_num(pw))
    print("Contains at least 1 special character: " + check_pass_spec_char(pw))
    print("Contains at least 1 uppercase character: " + check_pass_upper(pw))
    print("Contains at least 1 lowercase character: " + check_pass_lower(pw))


def check_pass_len(pw):
    if len(pw) < 16:
        return "Not satisfied"
    else:
        return "Satisfied"


def check_pass_num(pw):
    if any(char.isdigit() for char in pw):
        return "Satisfied"
    else:
        return "Not satisfied"


def check_pass_spec_char(pw):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(pw) == None:
        return "Not satisfied"
    else:
        return "Satisfied"


def check_pass_upper(pw):
    if any(char.isupper() for char in pw):
        return "Satisfied"
    else:
        return "Not satisfied"


def check_pass_lower(pw):
    if any(char.islower() for char in pw):
        return "Satisfied"
    else:
        return "Not satisfied"


password = "hello!"
password_evaluate(password)