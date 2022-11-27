import re
import numpy as np
from wordfreq import zipf_frequency


def password_evaluate(pw):
    grade = 0
    print("Criteria")
    grade, condition = check_pass_len(pw, grade)
    print("Length (At least 16 characters): " + condition)
    grade, condition = check_pass_num(pw, grade)
    print("Contains at least 1 number: " + condition)
    grade, condition = check_pass_spec_char(pw, grade)
    print("Contains at least 1 special character: " + condition)
    grade, condition = check_pass_upper(pw, grade)
    print("Contains at least 1 uppercase character: " + condition)
    grade, condition = check_pass_lower(pw, grade)
    print("Contains at least 1 lowercase character: " + condition)
    grade = strength_grading(pw, grade)
    min(grade, 100)
    print("Total: " + str(grade) + "/100")
    if grade < 50:
        print("Strength: Weak")
    elif 50 < grade < 80:
        print("Strength: Normal")
    else:
        print("Strength: Strong")


def check_pass_len(pw, g):
    if len(pw) < 16:
        return g, "Not satisfied"
    else:
        g += 8
        return g, "Satisfied"


def check_pass_num(pw, g):
    if any(char.isdigit() for char in pw):
        g += 8
        return g, "Satisfied"
    else:
        return g, "Not satisfied"


def check_pass_spec_char(pw, g):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(pw) == None:
        return g, "Not satisfied"
    else:
        g += 8
        return g, "Satisfied"


def check_pass_upper(pw, g):
    if any(char.isupper() for char in pw):
        g += 8
        return g, "Satisfied"
    else:
        return g, "Not satisfied"


def check_pass_lower(pw, g):
    if any(char.islower() for char in pw):
        g += 8
        return g, "Satisfied"
    else:
        return g, "Not satisfied"


def strength_grading(pw, g):
    g += max(min(5, pw.count(" ")), 0) * 3
    m = 0
    freq = 0
    for x in pw.split():
        if len(x) >= 5:
            m += 1
        if zipf_frequency(x, 'en') < 5:
            freq += 1
    g += min(m, 5) * 3
    g += min(freq, 5) * 3
    m = max(5, len(pw.split()))
    for x in np.unique(list(map(len, pw.split())), return_counts=True)[1]:
        if x > 1:
            m -= 1
    g += max(m, 0) * 3
    return g
