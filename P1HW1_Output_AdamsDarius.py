user_num = int(input("Enter integer: \n"))
def cube(x):
    return x * x * x
print("You entered:", user_num)
squ = user_num ** 2
cub = cube(user_num)
print(user_num, "squared is", squ)
print("And", user_num, "Cubed is", cub, " !!")
user_num2 = int(input("Enter another integer: \n"))
print("4 + 5", "is", user_num + user_num2)
print("4 * 5", "is", user_num * user_num2)
