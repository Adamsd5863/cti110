#This program calculates and displays grades and if statements for letter grades.
#October 26, 2022
#P3HW1 - Debugging
#Darius Adams
#
#User enters grades for module 1-6,
#The system shows all the grades,
#The system adds up all the grades,
#The System sums up the grades based on the number of modules,
#The system shows the minimum and maximum of the statements,
#The system prints the results of the highest and lowest, sum of grades and the average.
#The system uses the average number and converts it to a letter grade and prints the result.
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

average = sum(grades)/ len(grades)

lowestGrade = min(grades)

highestGrade = max(grades)

#Output

print('------------Results----------')
print(f'Lowest Grade:           {lowestGrade}')
print(f'Highest Grade:          {highestGrade}')
print(f'Sum of Grades:          {gradesum}')
print(f'Average:                {average:.2f}')
print('-------------------------------------')
# determine letter grade for average
if average >= 90:
    print('Your grade is: A')
elif average > 80:
    print('Your grade is: B')
elif average > 70:
    print('Your grade is: C')
elif average > 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this




