#This program calculates and displays grades and if statements for letter grades.
#November 14, 2022
#P4HW1 - Score List
#Darius Adams
#
#Maximum value is set to 100
#Minimum value is set to 0
#User inputs how many scores they want to enter
#The System finds out if the score 1-5 is within 0 and 100
#If not the systems tells you to reinput the scores
#The system the list of 5 scores
#The System sums up the grades based on the number of modules,
#The system shows the minimum and maximum of the statements,
#The system prints the results of the lowest, List of modified grades and the average.
#The system uses the average number and converts it to a letter grade and prints the result.
#Input
maximum = 100
minimum = 0
Score_List = float(input("How many scores do you want to enter? "))
print()
Score1 = float(input("Enter Score # 1: "))
if Score1 < minimum:
      print('INVALID Score entered!!!!')
      print('Score should be between 0 and 100')
      Score1 = float(input("Enter Score # 1 again: "))
      Score2 = float(input("Enter Score # 2: "))
elif Score1 > maximum:
      print('INVALID Score entered!!!!')
      print('Score should be between 0 and 100')
      Score1 = float(input("Enter Score # 1 again: "))
      Score2 = float(input("Enter Score # 2: "))
else:
    Score2 = float(input("Enter Score # 2: ")) 
if Score2 < minimum:
      print('INVALID Score entered!!!!')
      print('Score should be between 0 and 100')
      Score2 = float(input("Enter Score # 2 again: "))
      Score3 = float(input("Enter Score # 3: "))
elif Score2 > maximum:
      print('INVALID Score entered!!!!')
      print('Score should be between 0 and 100')
      Score2 = float(input("Enter Score # 2 again: "))
      Score3 = float(input("Enter Score # 3: "))
else:
    Score3 = float(input("Enter Score # 3: "))  
if Score3 < minimum:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    Score3 = float(input("Enter Score # 3 again: "))
    Score4 = float(input("Enter Score # 4: "))
elif Score3 > maximum:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    Score3 = float(input("Enter Score # 3 again: "))
    Score4 = float(input("Enter Score # 4: "))
else:
    Score4 = float(input("Enter Score # 4: "))
if Score4 < minimum:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    Score4 = float(input("Enter Score # 4 again: "))
    Score5 = float(input("Enter Score # 5: "))
elif Score4 > maximum:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    Score4 = float(input("Enter Score # 4 again: "))
    Score5 = float(input("Enter Score # 5: "))
else:
    Score5 = float(input("Enter Score # 5: "))
if Score5 < minimum:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        Score5 = float(input("Enter Score # 5 again: "))
elif Score5 > maximum:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    Score5 = float(input("Enter Score # 5 again: "))
print()
print()
    
#process

scores1 = [Score1, Score2, Score3, Score5]
scores = [Score1, Score2, Score3, Score4, Score5]
average = sum(scores1)/ len(scores1)
lowestScore = min(scores)


#Output

print('------------Results----------')
print(f'Lowest Grade    : {lowestScore}')
print(f'Modified List   : {scores1}')
print(f'Scores Average  : {average:.2f}')
# determine letter grade for average
if average >= 90:
    print(f'Grade           : A')
elif average > 80:
    print(f'Grade           : B')
elif average > 70:
    print(f'Grade           : C')
elif average > 60:
    print(f'Grade           : D')
else:
    print(f'Grade           : F') # TO DO: finish this
print('-------------------------------------')


