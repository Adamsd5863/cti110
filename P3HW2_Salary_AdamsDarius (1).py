#This program calculates Your salary, overtime, overtime pay, regular pay and gross pay
#CTI-110.
#P3HW2 - Salary
#Darius Adams
#October 31, 2022
#
#User inputs employees name, Hours worked and the pay rate
#The system calculates the overtime by hours worked subtract it from 40
#The system calulates the overtime formula by multiplying payrate by 1.5,
#The System calulates overtime pay by multiplying overtime formula by overtime,
#The system calculates regular hours rate by multiplying payrate by (hours worked - overtime),
#The system calculates gross pay by adding overtimepay and regular hours pay
#The system uses  prints the remployee name, hours worked, pay rate, overtime, overtime pat, regular hours pay and gross pay.
#Input
employees_name = input("Enter employee's name: ")
hrsworked = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))
print('-----------------------------------')
#process
if hrsworked <= 40:
    overtime = 40
    overtime = hrsworked - 40
    overtimeformula = payrate * 1.5
    overtimepay = overtimeformula * overtime
    reghrspay = payrate * (hrsworked - overtime)
    Grosspay = overtimepay + reghrspay
else:
    overtime = hrsworked - 40
    overtimeformula = payrate * 1.5
    overtimepay = overtimeformula * overtime
    reghrspay = payrate * (hrsworked - overtime)
    Grosspay = overtimepay + reghrspay
#Output
print(f'Employee name:           {employees_name}')
print('')
print(f'Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay')
print('----------------------------------------------------------------------------------------------')
print(f'{hrsworked}           {payrate}     {overtime}      {overtimepay:.2f}         ${reghrspay:.2f}      ${Grosspay:.2f}')


