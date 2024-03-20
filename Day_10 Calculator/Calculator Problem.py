from art import logo
import sys 
print(logo)

def operator():
  print('\n + \n - \n * \n / \n')
  op=input("Pick an Operator:")
  return op

def calcy(oprnd1,oprtr,oprnd2):
  if oprtr=='+':
    return oprnd1+oprnd2
  elif oprtr=='-':
    return oprnd1-oprnd2
  elif(oprtr=='*'):
    return oprnd1*oprnd2
  elif(oprtr=='/'):
    return oprnd1/oprnd2
  else:
    print("Invalid Operator")
    return 0

def calculator()  :
  flag=True
  oprnd1=float(input("What's the first number?:"))
  oprtr=operator()
  oprnd2=float(input("whats the next number?:"))
  result1=calcy(oprnd1,oprtr,oprnd2)
  print(f"{oprnd1} {oprtr} {oprnd2} = {result1} ")
  while(flag) :
    con=input("Press y to continue \n n to start again \n z to exit:")
    if(con=='z'):
      flag=False
      sys.exit()
    elif(con=='n'):
      calculator()
    
    oprtr=operator()
    oprnd2=float(input("whats the next number?:"))
    
    result=calcy(result1,oprtr,oprnd2)
    print(f"{result1} {oprtr} {oprnd2} = {result} ")
    result1=result

  
calculator()
  