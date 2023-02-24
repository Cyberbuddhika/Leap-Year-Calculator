print("Welcome to Leap Year Calculator")
print()
print("A leap year is a calendar year that contains an additional day added to keep the calendar year synchronized with the astronomical year or seasonal year.")
print("-------------------------------")
print()
year=int(input("Which year do you want to check? "))
if year%4 !=0:
  print("This is not a leap year")
elif year%100 == 0:
  print("This is a leap year")
elif year%400 != 0:
  print("This is a leap year")
else: print("This is not a leap year")
print()
print("Thank you for using Leap Year Calculator")
print("-------------------------------")
