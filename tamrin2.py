import math
while(True):
 n1=float(input("enter a number:\n"))
 op=input("enter operation:\n")
 if op=="cos":
    Rcos=math.cos(n1)
    dcos=math.cos(math.radians(n1))
    print("cos to Radian is:",Rcos)
    print("cos to degrees is:",dcos)
 elif op=="sin":
    Rsin=math.sin(n1)
    dsin=math.sin(math.radians(n1))
    print("sin to Radian is:",Rsin)
    print("sin to degrees is:",dsin)
 elif op=="tan":
    Rtan=math.tan(n1)
    dtan=math.tan(math.radians(n1))
    print("tan to Radian is:",Rtan)
    print("tan to degrees is:",dtan)
 elif op=="cot":
    Rcos=math.cos(n1)
    Rsin=math.sin(n1)
    Rcot=Rcos/Rsin
    print("cot to Radians is:",Rcot)
    dcos=math.cos(math.radians(n1))
    dsin=math.sin(math.radians(n1))
    dcot=dcos/dsin
    print("cot to degrees is:",dcot)
 else:
  n2=float(input("enter a number:\n"))
 if op=="+":
  sum=n1+n2
  print("summation is:",sum)
 elif op=="-":
  sub=n1-n2
  print("subtraction is:",sub)
 elif op=="*":
  multi=n1*n2
  print("multiplication is:",multi)
 elif op=="/":
  div=n1/n2
  print("division is:",div)
 elif op=="**":
  pow=n1**n2
  print("pow is:",pow)
 
