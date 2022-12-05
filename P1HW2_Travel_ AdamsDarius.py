#This program calculates and displays travel expenses
#September 21, 2022
#CTI-110 P1HW2 - travel expenses
#Darius Adams
#
#User enters budget
#User enters destination

#Input
budget = int(input("Enter budget: "))

location = input("location: ")

gas = int(input("How much do you think you will spend on gas? "))

accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))

food = int(input("Last, how much do you need for food? "))

#process

expenses = gas + accomodation + food

budget2 = budget - expenses

#Output

print('------------Travel Expenses----------')
print('Location:', location)
print('initial Budget:', expenses)
print()
print('Fuel:', gas)
print('accomodation:', accomodation)
print('Food:', food)
print()
print('Remaining Balance:', budget2)




