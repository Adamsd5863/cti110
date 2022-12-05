#This program calculates Your salary, overtime, overtime pay, regular pay and gross pay
#CTI-110.
#P4HW2 - Salary Calculator
#Darius Adams
#November 16, 2022
#
#I manually set the number of employees, total overtime pay, total regular hours and total gross pay to 0.
#The system checks if the loop is true
#The user inputs the employees name
#The System checks if the name is none if so it breaks if not then add 1 number of employees,
#The user inputs the hours worked and the payrate and the overtime overtime pay regular pay and Gross pay is set to 0.
#The system checks if the hours worked are 40 or more if so then calculates the overtime, overtime pay, regular hours and the gross pay
#The system calculates regular pay, gross pay, total overtime pay, total regular pay and gross pay and inputs them.
#The System inputs the number of employees, total overtime pay, total regular pay and the total gross pay.
number_employees = 0
totalovertimepay = 0
totalreghrspay = 0
totalGrossPay = 0
while True:
    employees_name = input("Enter employees name or \"None\" to terminate: ")
    if employees_name == "None":
        break
    else:
        number_employees += 1
        hrsworked = float(input(f'How many hours did {employees_name} worked? '))
        payrate = float(input(f'What is {employees_name} pay rate? '))
        overtime = 0
        overtimepay = 0
        reghrspay = 0
        Grosspay = 0
        if hrsworked > 40:
            overtime = hrsworked - 40
            overtimepay = overtime * payrate * 1.5
            reghrspay = payrate * 40
            Grosspay = overtimepay + reghrspay
            print()
            print(f'Employee name:           {employees_name}')
            print('')
            print(f'Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay')
            print('----------------------------------------------------------------------------------------------')
            print(f'{hrsworked}           {payrate}     {overtime}      {overtimepay}         ${reghrspay:.2f}      ${Grosspay:.2f}')
            print()
        else:
            reghrspay = hrsworked * payrate
            Grosspay = reghrspay
            totalovertimepay += overtimepay
            totalreghrspay += reghrspay
            totalGrossPay += Grosspay
            print()
            print(f'Employee name:           {employees_name}')
            print('')
            print(f'Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay')
            print('----------------------------------------------------------------------------------------------')
            print(f'{hrsworked}           {payrate}     {overtime}      {overtimepay}         ${reghrspay:.2f}      ${Grosspay:.2f}')
            print()
print()
print(f"Total number of employees entered: {number_employees}")
print(f"Total number of payed overtime: {totalovertimepay}")
print(f"Total number of payed for regular hours: {totalreghrspay}")
print(f"Total number of payed in gross: {totalGrossPay}")


