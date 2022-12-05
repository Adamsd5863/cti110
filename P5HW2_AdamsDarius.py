# Execute a fun math Quiz...
# November 28, 2022
# CTI-110 P5HW2 - Math Quiz
# Darius Adams
#
#User can pick between 3 options to execute.
#When user enters 1, the system generates 2 numbers and adds them and check if they are equal greater than or less than each other if equal they congradulates the user, if not go back to menu
#When user enters 2, the system generates 2 numbers and subtracts them them and check if they are equal greater than or less than each other if equal they congradulates the user, if not go back to menu
##When user enters 3, they thank the user for playing and exit the scene.
rng_num1 = 0
rng_num2 = 0
correct_ans = 0
menu = 0
guesses = 0

def math_quiz(menu):
      print('Welcome to Math Quiz')
      print()
      print()
      print('MAIN MENU')
      print('---------------------------------')
      print('1. Adding Random Numbers')
      print('2. Subtracting Random Numbers')
      print('3. Exit')
      print()
      
quit_program = False

while not quit_program:
      math_quiz(menu)
      menu = input('please choose one of the menu options: ')
      
      if menu == '1' :
            import random
            rng_num1 = random.randint(1, 100)
            rng_num2 = random.randint(1, 100)
            correct_ans = rng_num1 + rng_num2
            print(f'{rng_num1}')
            print(f'+{rng_num2}')
            print()
            answer = int(input('Enter answer. '))
            if answer > correct_ans:
                  print('Sorry, guess is too high. ')
                  guesses +=1
            elif answer < correct_ans:
                  print('Sorry, guess is too low. ')
                  guesses +=1
            elif answer == correct_ans:
                  print('Congradulations!!! your answer is correct..')
                  print(f'number of guesses: {guesses}')
      
      elif menu == '2' :
            import random
            rng_num1 = random.randint(1, 100)
            rng_num2 = random.randint(1, 100)
            correct_ans = rng_num1 - rng_num2
            print(f'{rng_num1}')
            print(f'-{rng_num2}')
            print()
            answer = int(input('Enter answer. '))
            if 'answer' > 'correct_ans':
                  print('Sorry, guess is too high.')
                  guesses +=1
            elif 'answer' < 'correct_ans':
                  print('Sorry, guess is too low.')
                  guesses +=1
            elif answer == correct_ans:
                  print('Congradulations!!! your answer is correct..')
                  print(f'number of guesses: {guesses}')
      
      elif menu == '3' :
            print('Thank you for playing...')
            print('Bye!!')
            quit_program = True
            


