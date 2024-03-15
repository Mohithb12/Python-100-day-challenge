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
    return 'enter valid operator'
flag=True
oprnd1=float(input("What's the first number?:"))
while(flag) :
  
  oprtr=operator()
  oprnd2=float(input("whats the next number?:"))
  result=calcy(oprnd1,oprtr,oprnd2)
  print(f"{oprnd1} {oprtr} {oprnd2} = {result} ")

  con=input("Press y to continue and n to stop:")
  if(con=='n'):
    flag=False
    sys.exit()
  else:
    oprnd1=result


  