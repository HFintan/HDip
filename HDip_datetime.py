# Problem sheet q8.
# Prints time in
# Tuesday, March 19th 2019 at 11:37am
# format.

# Renamed script, as calling it datetime.py seemed to
# cause some sort of clash, presumably with the datetime package

# Used various to get awkward time formatting
# https://stackoverflow.com/questions/2925230/get-235pm-instead-of-0235pm-from-python-date-time
# https://www.w3schools.com/python/python_datetime.asp
# https://stackoverflow.com/questions/904928/python-strftime-date-without-leading-0
# and zip
# https://www.programiz.com/python-programming/methods/built-in/zip

import datetime

NOW = datetime.datetime.now()

todays_date = int(NOW.strftime("%d"))
#if what_date in [1,21,31]:
#    ordinal = 'st'
#else:
#    if what_date in [2,22]:
#        ordinal = 'nd'
#    else:
#        if what_date in [3,23]:
#            ordinal = 'rd'
#        else:
#            ordinal = 'th'

# gets ordinal for date
dates = [[1,21,31],[2,22],[3,23]]
ordinals = ['st','nd','rd']

for date, ordinal in zip(dates,ordinals):
    if todays_date in date:
        desired_ordinal = ordinal
        break
    else:
        desired_ordinal='th'

print(NOW.strftime("%A, %B %d"),desired_ordinal,NOW.strftime(" %Y at %-I:%M%P"), sep='')
