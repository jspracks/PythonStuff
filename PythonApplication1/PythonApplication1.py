#imported library
import math

#Defined Constants
USEXCHANGE = 0.046
USEXCHANGEII = 0.037
#Title of Assignment
print("**Koruna Exchange App**\n")

#User Input
savings = float(input("How many Korunas do you have in your savings account?"))
print (f"The exchange information for {savings} korunas is now being recorded")
#Calculations
total = math.fabs (savings)
total = (savings * USEXCHANGE)
totalII = math.fabs (savings)
totalII= (savings * USEXCHANGEII)

difference= math.fabs (total + totalII)

#Output to disk file
report=open('c:\\class\\jsprackman-ke.txt','w')

print(f"For {savings} korunas:")
print(f"n\At the rate of 42 korunas per U.S. dollar\n", file=report)
print(f" you have {total} U.S. dollars.", file=report)
print(f"n\At the rate of 37 korunas per U.S. dollar", file=report)
print(f" you have {totalII} U.S. dollars", file=report)
print(f"The difference is {difference} U.S. dollars.", file=report)

#closing the file
report.close()





