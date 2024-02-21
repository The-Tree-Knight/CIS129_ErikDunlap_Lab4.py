#Module 4 Lab-4
#Erik Dunlap
#2/21/2024
#Writing a program by doing exactly what it says to calculate raise

monthlySales= 0
storeAmount = 0
empAmount = 0
salesIncrease = 0
prompt = 'What is this month\'s sales in $'
#Declare local variables which is completely unneeded in Python

monthlySales = float(input(prompt))

if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount= 0
#Getting what bonus the store gets

salesIncrease = float(input('Enter percent of sales increase: '))
salesIncrease = salesIncrease / 100

if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0
#Getting employee bonus
    
print("The store bonus amount is $", +storeAmount)
print("The employee bonus amount is $", +empAmount)
if(storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')
#Output of the data
