#Question 2
# Part 1
txt = "Python" [2:] #Deletes two characters from the string "Python".
txt2 = txt [::-1] #Reverses the string.
print (txt2) #Prints the string with two characters deleted and in reverse.

#Part 2
print("Welcome to the Simple Arithmetic Calculator!")
print("For Subtraction, the second number will be subtracted from the first number.") #Outputs condition for subtraction.
print("For Division, the first number will be divided by the second number.") #Outputs condition for division.
userNum1 = float(input("Enter the first number:")) #Obtains user input for the first number.
userNum2 = float(input("Enter the second number:"))#Obtains user input for second number.
addNum = userNum1+userNum2 #Adds the two numbers together.
minusNum = userNum1-userNum2 #Subtracts the second number from the first number.
divideNum = userNum1/userNum2 #Divides the first number with the second number.
multiplyNum = userNum1*userNum2 #Multiplies the two numbers together.
print ("Addition:",addNum, "Subtraction:",minusNum, "Division:",divideNum, "Multiplication:",multiplyNum,) #Outputs the arithmetic to the user.