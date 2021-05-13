"""
#Bài 1:
import math
print("Giải phương trình bậc 2: ax**2 + bx + c = o \n")
a = float(input("nhập a ="))
b = float(input("nhập b ="))
c = float(input("nhập c =" ))
if a == 0:
    if b == 0:
        print("phương trình vô nghiệm")
    else:
        print(f"nghiệm của phương trình là: x = {-c/b}")
else:
    denta = b**2 - 4*a*c
    if denta < 0:
        print("phương trình vô nghiệm")
    elif denta == 0:
        print(f"phương trình có nghiệm kép: x1 = x2 =  {-b/ (2*a)}")
    else:
        x1 = (-b+ math.sqrt(denta))/(2*a)
        x2 = (-b - math.sqrt(denta))/(2*a)
        print(f"phương trình có 2 nghiệm: x1 = {x1}, x2 = {x2}")
        """
"""
#Bài 2:
n = int(input("nhập n ="))
x = float(input("nhập x ="))
i = 0
s1 = 0
while i <= n:
    s1 = s1 + x**i
    i += 1
print(f"giá trị của s1 là: {s1}")"""
"""print("\n")
n = int(input("nhập n ="))
x = float(input("nhập x ="))
i = 0
s2 = 0
while i <= n:
    s2 = s2 + (-x)**i
    i += 1
print(f"giá trị của s2 là: {s2}")
'"""
"""
#Bài 3:
import math
n = int(input("nhập n ="))
x = float(input("nhập x ="))
i = 0
s3 = 0
while i <= n:
    s3 = s3 + x**i/math.factorial(i)
    i += 1
print(f"giá tri của s3 là: {s3}")"""
print("\n")
"""
#Bài 4:
n = int(input("nhập n ="))
if n >= 1000:
    print("yêu cầu nhập lại!")
else:
    a = int(n/100)
    b = int((n - 100*a)/10)
    c = n - 100*a - 10*b
    print(f"tổng  giá trị các chữ số của số nguyên n = {a+ b+ c}")
    """
print("\n")
"""
#Bài 5:
a = float(input("nhập a ="))
b = float(input("nhập b ="))
c = float(input("nhập c ="))
if a > b + c or b > a + c or c > a +b:
    print("đây không phải ba cạnh của  một tam giác")
else:
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("Đây là ba cạnh của một tam giác vuông")
    else:
        print("Đây không phải ba cạnh của một tam giác vuông")"""
#Bài 5:
import math
i = 0
e = 0
a = float(input("nhập a ="))
if a >= 1:
    print("Vui lòng nhập lại a.")
else:
    while a < 1/ math.factorial(i):
        e = e + 1/ math.factorial(i)
        i += 1
    print(f"giá trị của e là {e}")





