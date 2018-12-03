a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")
x = len(a)
y = len(b)
z = len(c)
max = x
if y > max:
    max = y
if z > max:
    max = z
print("+" + "-" * (max+2) + "+")
print("|" + a.center(max+2) + "|")
print("|" + b.center(max+2) + "|")
print("|" + c.center(max+2) + "|")
print("+" + "-" * (max+2) + "+")