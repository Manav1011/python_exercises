import re
import os
import time


def stpi_calculator(cmt, dwpd, java, cns):
    # if re.search("/[0-9g-zG-ZeE]|a[c-zC-Z]|b(a|[d-zD-Z])|A[c-zC-Z]|b(a|[d-zD-Z])|c(a|b|[e-zE-Z])|C(a|b|[e-zE-Z])|d(a|b|c|[e-zE-Z])|D(a|b|c|[e-zE-Z])|f([a-eA-E]|[g-zG-Z])|F([a-eA-E]|[g-zG-Z])/g",java) or re.search("/[0-9g-zG-ZeE]|a[c-zC-Z]|b(a|[d-zD-Z])|A[c-zC-Z]|b(a|[d-zD-Z])|c(a|b|[e-zE-Z])|C(a|b|[e-zE-Z])|d(a|b|c|[e-zE-Z])|D(a|b|c|[e-zE-Z])|f([a-eA-E]|[g-zG-Z])|F([a-eA-E]|[g-zG-Z])/g",cns) or re.search("/[0-9g-zG-ZeE]|a[c-zC-Z]|b(a|[d-zD-Z])|A[c-zC-Z]|b(a|[d-zD-Z])|c(a|b|[e-zE-Z])|C(a|b|[e-zE-Z])|d(a|b|c|[e-zE-Z])|D(a|b|c|[e-zE-Z])|f([a-eA-E]|[g-zG-Z])|F([a-eA-E]|[g-zG-Z])/g",cmt) or re.search("/[0-9g-zG-ZeE]|a[c-zC-Z]|b(a|[d-zD-Z])|A[c-zC-Z]|b(a|[d-zD-Z])|c(a|b|[e-zE-Z])|C(a|b|[e-zE-Z])|d(a|b|c|[e-zE-Z])|D(a|b|c|[e-zE-Z])|f([a-eA-E]|[g-zG-Z])|F([a-eA-E]|[g-zG-Z])/g",dwpd):
    match_java = re.search(
        "ab|AB|aa|AA|bb|BB|bc|BC|cc|CC|cd|CD|dd|DD|ff|FF", java)
    match_cmt = re.search(
        "ab|AB|aa|AA|bb|BB|bc|BC|cc|CC|cd|CD|dd|DD|ff|FF", cmt)
    match_dwpd = re.search(
        "ab|AB|aa|AA|bb|BB|bc|BC|cc|CC|cd|CD|dd|DD|ff|FF", dwpd)
    match_cns = re.search(
        "ab|AB|aa|AA|bb|BB|bc|BC|cc|CC|cd|CD|dd|DD|ff|FF", cns)
    if not (match_java or match_dwpd or match_cns or match_cmt):
        print("Enter a valid grade!!")
        time.sleep(2)
        os.system("cls")
        stpi_calculator(input("Enter your cmt grade: "), input("Enter your dwpd grade: "), input(
            "Enter your java grade: "), input("Enter your cns grade: "))
    if re.search("ff|FF", java) or re.search("ff|FF", cmt) or re.search("ff|FF", cns) or re.search("ff|FF", dwpd):
        print("You have not passed the exam!!")
        time.sleep(2)
        os.system("cls")
        stpi_calculator(input("Enter your cmt grade: "), input("Enter your dwpd grade: "), input(
            "Enter your java grade: "), input("Enter your cns grade: "))
    if (len(java) != 2) or (len(cmt) != 2) or (len(dwpd) != 2) or (len(cns) != 2):
        print("Enter a valid grade!!")
        time.sleep(2)
        os.system("cls")
        stpi_calculator(input("Enter your cmt grade: "), input("Enter your dwpd grade: "), input(
            "Enter your java grade: "), input("Enter your cns grade: "))

    grade = {"AA": 10, "AB": 9, "BB": 8, "BC": 7, "CC": 6, "CD": 5, "DD": 4, "FF": 0,
             "aa": 10, "ab": 9, "bb": 8, "bc": 7, "cc": 6, "cd": 5, "dd": 4, "ff": 0}
    credit = {"java": 7, "cmt": 5, "cns": 7, "dwpd": 7}

    total_grade = (grade[f"{java}"]*credit["java"])+(grade[f"{cmt}"]*credit["cmt"])+(
        grade[f"{cns}"]*credit["cns"]+(grade[f"{dwpd}"]*credit["dwpd"]))
    total_credit = credit["java"]+credit["cmt"]+credit["cns"]+credit["dwpd"]
    stpi = total_grade/total_credit
    print(stpi)
    if input("Do you want to continue? (y/n):  ") == "y":
        os.system("cls")
        stpi_calculator(input("Enter your cmt grade: "), input("Enter your dwpd grade: "), input(
            "Enter your java grade: "), input("Enter your cns grade: "))
    else:
        os.system("cls")


stpi_calculator(input("Enter your cmt grade: "), input("Enter your dwpd grade: "), input(
    "Enter your java grade: "), input("Enter your cns grade: "))
