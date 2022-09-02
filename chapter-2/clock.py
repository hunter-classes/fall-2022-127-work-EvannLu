#str var to ask question
cTime_str = input("What time is it now (in hours)? ")
wTime_str = input("How long (in hours) do you want your alarm to go off? ")

#int var to store user input 
cTime_int = int(cTime_str)
wTime_int = int(wTime_str)

#get the time (in  24 hour)
hour = cTime_int + wTime_int

#turn the 24 hours + in 24 hour scale
alarm = hour % 24

#print the desired time
print(alarm)

#check work
#input = 0
#alarm off 60 hours
print(60 % 24)
#works


