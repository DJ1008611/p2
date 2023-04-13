# 定义加法函数
def add(x, y):
    return x + y
#test

# 定义减法函数
def subtract(x, y):
    return x - y

# 定义乘法函数
def multiply(x, y):
    return x * y

# 定义除法函数
def divide(x, y):
    return x / y

# 用户输入
print("选择运算：")
print("1、加法")
print("2、减法")
print("3、乘法")
print("4、除法")

# 获取用户输入
choice = input("输入你的选择（1/2/3/4）:")

num1 = float(input("输入第一个数字: "))
num2 = float(input("输入第二个数字: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("非法输入")