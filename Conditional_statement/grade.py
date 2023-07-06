O_mark = int(input("enter your Obtained mark"))
F_mark = int(input("enter your Full mark"))
grade = (O_mark / F_mark) * 100
if grade >= 90:
    print("A+ grade \n passed")
elif grade >= 80:
    print("A grade")
elif grade >= 70:
    print("B+ grade")
elif grade >= 60:
    print("B grade")
elif grade >= 50:
    print("C+ grade")
elif grade >= 40:
    print("C grade")
else:
    print("Failed")
print('total percentage', grade)
