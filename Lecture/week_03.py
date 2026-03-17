# 数据类型
int
float
complex
str
bool 
# 文件路径 如何改变路径中“\”，用前面加r

# f-string <左边补空格 >右边的补空格 ^中间的 :.3f f -> float str,float, 对齐类型不同

# 函数 （内置，标准，扩展，对象）
"hello".upper() #str是不可变对象
a = "hello"
print(a.upper())
print(a)

# 运算符号 算术关系逻辑赋值 
# 非0为真与逻辑错误

year = eval(input())
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("是闰年")
else :
    print("不是闰年")

scores = float(input("what is your score?"))
if scores >= 90:
    print("a")
elif scores >= 80:
    print("b")
elif scores >= 70:
    print("c")
else :
    print("d")

i = 1
s = 0
while i <= 1000 :
    s = s + (-1)**(i-1)/(2*i-1)
    i += 1
print(s)
pi = 4 * s
print(pi)

i = 1
while i <=100:
    print(i, end = " ")
    i += 1
    
else:
    print("WHU")
# break & continue DIFFERENCE

range(1,5,2)
range(1,5)
range(5)