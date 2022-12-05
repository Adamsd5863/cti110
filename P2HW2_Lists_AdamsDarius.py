#This program calculates and displays travel expenses
#October 17, 2022
#P2HW2 - List
#Darius Adams
#
#User enters module 1-6,
#The system adds up all of the modules,
#The System divides the grades of the module by 6,
#The system outputs the lowest grade, the highest grade, sum of grades and the average.

#Input
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for module 5: "))
module6 = float(input("Enter grade for module 6: "))
#process
grades = [module1, module2, module3, module4, module5, module6]
gradesum = sum(grades)
average = sum(grades) / len(grades)
lowestGrade = min(grades)
highestGrade = max(grades)
#Output
print('------------Results----------')
print(f'Lowest Grade:           {lowestGrade}')
print(f'Highest Grade:          {highestGrade}')
print(f'Sum of Grades:          {gradesum}')
print(f'Average:                {average:.2f}')
print('-------------------------------------')




