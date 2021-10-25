#question 1
def convert_to_days():
   hours=eval(input("Enter number of hours:"))
   min = eval(input("Enter number of minutes:"))
   sec = eval(input("Enter number of seconds:"))
   return hours,min,sec

def get_days():
   h,m,s=convert_to_days()
   days=((h/24)+(m/(60*24))+(s/(3600*24)))
   k=round(days,4)
   return k
k=get_days()
print("the number of days is:",k)
