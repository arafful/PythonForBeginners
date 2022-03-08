"""
    Dada uma data retorne o dia da semana
"""
import calendar


def getday(dow):
    day, month, year = (int(i) for i in dow.split("/"))
    dayno = calendar.weekday(year, month, day)
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[dayno]


dow = input("Enter the date (dd/mm/yyyy) to get the day of week: ")
print(getday(dow))
