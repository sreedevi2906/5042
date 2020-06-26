3.python program to check leapyear

In [50]:
year=int(input('enter year:'))
if year%4==0 and year%100!=0:
    print('its leap year',year)
elif year%100==0:
    print('its not leap year',year)
elif year%400==0:
    print('its leap year',year)
else:
    print('its not leap year',year)