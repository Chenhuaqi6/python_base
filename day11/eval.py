#eval.py


# s = "1+2*3+4"
# v = eval(s)
# print(v)

# while 1:
#     s = input(">>>")
#     print(eval(s))

# s = """
# def fx(f,x,y):
#     print(f(x,y))
# fx((lambda a,b: a+b),100,200)
# fx((lambda x,y: x**y),3,4)



# """
# exec(s)
s="x+y"
d1={"x":100,"y":200}
d2={"x":1}

v = eval(s,d1,d2)
print(v)