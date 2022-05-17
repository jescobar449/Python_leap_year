#Name: Jose Melquiades Escobar

#Turn Magic number into Named Constants 
lowestYearPossible = 1000
highestYearPossible = 9999
leapYear100Criteria = 100
leapYear400Criteria = 400
leapYear4Criteria = 4
remainderOfZero = 0

#Prompt user to enter a year
year = int( input ('Enter a year (4 digits): '))

#Use nested if to verify if the year is divisible by both 100 & 400
if year < lowestYearPossible:           #check for at least 4 digits enterd 
    print ('Error: invalid year entered')
elif year > highestYearPossible:        #check for more than 4 digits entered
    print ('Error: invalid year entered')
else:
    modulusBy100 = year % leapYear100Criteria                         #check for a zero remainder 
    modulusBy400 = year % leapYear400Criteria                         #check for a zero remainder 
    modulusBy4 = year % leapYear4Criteria                             #check for a zero remainder 
    if modulusBy100 == remainderOfZero and modulusBy400 == remainderOfZero:      #Verify that leap year is divisible by both 100 and 400
        print ('That is a leap year. February has 29 days.')          #display for leap year thats divisible by 100 and 400
    elif modulusBy100 != remainderOfZero and modulusBy4 == remainderOfZero:      #Verify that leap year is NOT divisible by 100 and IS divisible by 4
        print ('That is a leap year. February has 29 days.')          #display for leap year thats not divisible by 100 but is divisible by 4
    else:
        print ('That is not a leap year. Feruary has 28 days.')       #display that the leap year criterias were not met


        

