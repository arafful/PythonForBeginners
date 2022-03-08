"""
    Verifica ano bissexto
"""
# import datetime

check_year = int(input("Entre o ano a checar (YYYY): "))

if check_year % 4 == 0 and check_year % 100 != 0:
    print("O ano", check_year, "é bissexto.")
elif check_year % 100 == 0:
    print("O ano", check_year, "não é bissexto.")
elif check_year % 400 == 0:
    print("O ano", check_year, "é bissexto.")
else:
    print("O ano", check_year, "não é bissexto.")



