#This program calculates and displays travel expenses
#October 10, 2022
#CTI-110 P2HW1 - Travel
#Darius Adams
#
#User enters budget,
#User enters location,
#User enters gas,
#User enters accomodations,
#The system adds the gas, accomodations and food,
#The System subtracts the budget and expenses,
#The system outputs the results in float values with dollar signs.

#Input
budget = float(input("Enter budget: "))


location = input("Enter your travel destination: ")


gas = float(input("How much do you think you will spend on gas? {:.2f}"))


accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))


food = float(input("Last, how much do you need for food? "))


#process

expenses = gas + accomodation + food

budget2 = budget - expenses

#Output

print('------------Travel Expenses----------')
print(f'Location:           {location}')
print(f'initial Budget:     ${budget}')
print(f'Fuel:               ${gas}')
print(f'Accomodation:       ${accomodation}')
print(f'Food:               ${food}')
print('-------------------------------------')
print()
print(f'Remaining Balance:  ${budget2}')




