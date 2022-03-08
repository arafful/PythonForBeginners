# Calcula minha idade
import datetime
dob = input("Entre a sua data de nascimento: (dd/mm/aaaa)")
dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
print("Como seu aniversário é em", dob.strftime("%d"), "de", dob.strftime("%B, %Y"))

currentDate = datetime.datetime.today().date()
print("e hoje é", currentDate)

age = currentDate.year - dob.year
month_calc = currentDate.month - dob.month
day_calc = currentDate.day - dob.day

age = int(age)
month_calc = int(month_calc)
day_calc = int(day_calc)

if month_calc < 0:
    age -= 1
elif day_calc < 0 and month_calc == 0:
    age -= 1

print("Sua idade atual é: {0:d}".format(age), "anos")

