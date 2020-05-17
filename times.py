import time
import calendar

#daryafte unix timestamp
currentTime = time.time()
print(currentTime)
print(int(currentTime))

#be har kodam az tavabe zir mitavan zamane feli ra be sanie pas dad ya nadad
#ke dar in surat zamane konuni hesab mishavad
print(time.ctime(currentTime)) #ctime string barmigardanad
print(time.localtime(currentTime))
print(time.gmtime(currentTime)) #shabihe tabe localtime vali bar hasbe saate jahani

print(calendar.month(2020, 5))