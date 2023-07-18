def calculate_hcf(x,y):
    if x<y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf

num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
print("your result is ",calculate_hcf(num1,num2))