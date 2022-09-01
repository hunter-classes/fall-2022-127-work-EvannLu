#Activity: 2.8.2 ActiveCode (inputfun)

n = input("Evan Lu")
print("Hello", n)



#Activity: 2.8.3 ActiveCode (int_secs)

str_seconds = input("36000000")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)



#Activity: 2.8.4 Multiple Choice (test_question2_7_1)

What is printed when the following statements execute?

n = input("Please enter your age: ")
# user types in 18
print ( type(n) )

Answer:  <class 'str'>



#Activity: 2.8.5 Clickable (ca_id_ints)

seconds = input("Please enter the number of seconds you wish to convert")

hours = int(seconds) // 3600
total_secs = int(seconds)
secs_still_remaining = total_secs % 3600
print(secs_still_remaining)

Answer: 
- hours
- total_secs (X2)
- secs_still_remaining (X2)



#Activity: 2.8.6 Clickable (ca_id_str)

: Click on all of the variables of type `str` in the code below
seconds = input("Please enter the number of seconds you wish to convert")

hours = int(seconds) // 3600
total_secs = int(seconds)
secs_still_remaining = total_secs % 3600
print(secs_still_remaining)

Answer: 
- seconds (X3)