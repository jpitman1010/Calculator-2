"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
while True:
    user_equation= input("enter equation. >>>>>>")
    user_equation=user_equation.split(" ")
    if user_equation[0]=="q":
        break
    else:
        num1=int(user_equation[1])
        if len(user_equation)==2:
            if user_equation[0] == "**":
                print(square(num1))
            else:
                print(cube(num1))
        elif len(user_equation)==3:
            num2=int(user_equation[2])
            if user_equation[0] == "+":
                print(add(num1,num2))
            elif user_equation[0] == "-":
                print(subtract(num1,num2))
            elif user_equation[0] == "*":
                print(multiply(num1,num2))
            elif user_equation[0] == "/":
                print(divide(num1,num2))
            elif user_equation[0] == "**":
                print(power(num1,num2))
            elif user_equation[0] == "%":
                print(mod(num1,num2))
