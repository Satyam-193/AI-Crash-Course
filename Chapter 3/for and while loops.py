fact = 1
num = int(input("Enter a number: "))

for i in range(1, num+1):
  fact*=i

print("The factorial of a number ",num,"is ",fact)

# print 
# Enter a number: 5
# The factorial of a number  5 is  120
----------------------------------------------------

# For While Loops
fact = 1
# initializing a bool value
stop = False
i = 1 
number = int(input("Enter a number: "))
while stop == False:
  fact*=i
  i+=1
  if i>num:
    stop = True

print("The factorial of a number ",num,"is ",fact)

