
length = 7.8
width = 3.5
print("Area: " + str(length * width))
print("Perimeter: " + str((length + width) * 2))


Fibonacci_cache = {}
Alist = []
m = int(input("nhap tu ban phim so m :"))
def Fibonacci(n):
    if n in Fibonacci_cache:
        return Fibonacci_cache[n]
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    elif n > 1:
        value = Fibonacci(n - 1) + Fibonacci(n - 2)
    Fibonacci_cache[n] = value
    return value

for n in range(1,100):
    print(Fibonacci(n))






a = int(input("nhap so a :"))
b = int(input("nhap so b :"))
count_odd = 0
count_even = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)

i = float(input("nhap mot so bat ki :"))
while i <= 100:
    print(i)
    i += 1

n = int(input("nhap mot so bat ki :"))
b = 1

while b <= 5:
    print(n, "*", b, "=", n * b)
    b += 1

def xin_chao():
    print("xin chao")
xin_chao()

a = float(input())
b = float(input())
answer = 0
while a <= b:
    if a % 2 != 0:
        answer += a
    a += 1
print(answer)


so_thu_nhat = float(input("dien so thu nhat :"))
dau = input("dien phep tinh :")
so_thu_hai = float(input("dien so thu hai :"))
if dau == "+":
    print(so_thu_nhat + so_thu_hai)
elif dau == "-":
    print(so_thu_nhat - so_thu_hai)
elif dau == "*":
    print(so_thu_nhat * so_thu_hai)
elif dau == "/":
    print(so_thu_nhat / so_thu_hai)
else:
    print("khong tinh duoc")


name = input("dien ten cua ban :")
age = int(input("dien tuoi cua ban :"))
gender = input("dien gioi tinh cua ban :")
print("co mot ban " + gender + " ten " + name + " 10 nam sau co ay " + str(age + 10) + " tuoi .")

a = int(input("do dai tam giac = "))
h = int(input("chieu cao tam giac = "))
area = 1/2 * a * h
print("The area of triangle is", area)

print("nhap du lieu de so sanh gia tri sau co dung khong :")
a = int(input("nhap so a :"))
b = int(input("nhap so b :"))
print(a is b)

age = int(input("nhap tuoi cua ban :"))
if age > 50:
    print("you are so old")
else:
    print("you are incredible young!")

temp = int(input("nhap nhiet do ngay hom nay! :"))
if temp >= 45:
    print("Stay at home and enjoy a good movie")
elif temp >= 40:
    print("Stay at home")
elif temp == 20:
    print("Go out side and enjoy the weather")
elif temp <= 10:
    print("It's cold outside")
else:
    print("Let's go to school")

a = int(input("nhap so a :"))
b = int(input("nhap so b :"))
c = int(input("nhap so c :"))
avg = (a + b + c) / 2

if avg > a and avg > b:
    print("The average value is greater than both a and b")
elif avg > b and avg > c:
    print("The average value is greater than both b and c")
elif avg > a and avg > c:
    print("The average value is greater than both a and c")
elif avg > a:
    print("The average value is greater than a")
elif avg > b:
    print("The average value is greater than b")
else:
    print("the average value is greater than c")