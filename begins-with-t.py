# Problem sheet, question 2. Checking which letter the current day of the 
# week begins with.
# Consulted https://stackoverflow.com/questions/255147/how-do-i-keep-python-print-from-adding-newlines-or-spaces
# to fix spacing in print syntax, and module lecture for datetime syntax.

import datetime

weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Uses datetime to find numeric format of today's date. Note not all languages
# begin with the same day of the week. E.g., javascript and python differ.
# Something to perhaps watch out for.
today = weekDays[datetime.datetime.today().weekday()]
first_letter = today[0]

if first_letter == 'T':
    print("Yes!", end =' ')
else:
    print("No.", end = ' ')
print("Today is ", today, ", and it begins with '", first_letter,"'.", sep = '')


