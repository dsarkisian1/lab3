#name: David Sarkisian
#Lab 3
#Notes: Assignment is divided into multiple sections, will be seperated by 
###############################################
#################### PROBLEM # ################
###############################################

############################################### 
#################### PROBLEM #1################
############################################### 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 > num2 :
   if num1 > num3 :
      print(num1)
   else :
      print(num3)
else :
   if num2 > num3 :
      print(num2)
   else :
      print(num3)

#####OUTPUT#####

#Enter a number: 3
#Enter a number: 4
#Enter a number: 5
#5

#Enter a number: 10
#Enter a number: 20
#Enter a number: 100
#100

#####GENERAL DESCRIPTION#####
#This code appears to find the largest number in a group of 3



############################################### 
#################### PROBLEM #2################
############################################### 



count = int(input("please enter the number of items purchased: "))
total = int(input("please enter the total cost: "))
print("Average =", 0 if count == 0 else total/count) #place a conditional expression inside


#####OUTPUT#####
#please enter the number of items purchased: 10
#please enter the total cost: 10
#Average = 1.0

#please enter the number of items purchased: 0
#please enter the total cost: 10
#Average = 0



############################################### 
#################### PROBLEM #3################
###############################################

#a)
i = 1
while i < 10 :
  print(i, end =  " ")
  i = i + 2
  if i == 5 :
     i = 9

#b)
for j in range (1, 10, 2) : 
  print(j, end =  " ")
  if j == 5 :
     j = 9


#####OUTPUT#####
#a) 1 3 9
#b) 1 3 5 7 9



############################################### 
#################### PROBLEM #4################
###############################################

#a)
sum = 0
for x in range (1, 20) : 
    sum += x
print("Sum: ", sum) 


#b)
while 1 :
    print("Infinite while loop")

#c)
number = int(input("Enter a number to check Prime or Not: "))
count = 0
for i in range (2, number//2 + 1):
    if number % i == 0 :
        count += 1
        break
    i += 1
if count == 0 :
    print(number, " is a prime number")
else :
    print(number, " is not a prime number")



#####OUTPUT#####
#a) Sum:  190

#b)Infinite while loop
#Infinite while loop
#Infinite while loop
#Infinite while loop
#Infinite while loop
#Infinite while loop
#Infinite while loop
#...

#c)Enter a number to check Prime or Not: 37
#37  is a prime number
#Enter a number to check Prime or Not: 35
#35  is not a prime number


