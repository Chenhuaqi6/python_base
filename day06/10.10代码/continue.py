#continue

# for x in range(0,10):
#     if x % 2 == 0:
#         continue
#     print(x)

s = 0
for x in range(1,100):
    if x % 2 ==0 or x % 3 ==0 or x % 5 == 0 or x % 7 == 0:
        continue
    s += x
print("和为: ",s)



