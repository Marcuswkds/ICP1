#Question 1
#Differences between Python 2 and Python 3
#1) The print keyword in Python 2 is replaced by the print() function in Python 3
#2) In Python 2 implicit str type is ASCII. But in Python 3 implicit str type is Unicode.
#3) In Python 2, if you write a number without any digits after the decimal point, it rounds your calculation down to the nearest whole number.
# In Python 3, you don't have to worry about the calculation rounding down even if you don't add any digits behind the numbers. ex. 5/2 = 2.5

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

#Question 3
string=input("Enter string:") #Prompts user to input string
string=string.replace('python','pythons') #Replaces the string 'python' with 'pythons'
string=string.replace('Python','pythons') #Replaces the string 'Python' with 'pythons'
print("Modified string:")
print(string) #Outputs the modified string to the user.
