import random
user_name = input("Enter your name: ")
print("Hello, {}".format(user_name))
rating = 0
rating_file = open('rating.txt', 'r')
for line in rating_file:
    if line.startswith(user_name):
        rating = line.split()[1]
options = input().split(',')
if options == ['']:
    options = ['rock', 'paper', 'scissors']
print("Okay, let's start")
while True:
    player_option = input()
    if player_option == '!exit':
        print("Bye!")
        break
    elif player_option == '!rating':
        print("Your rating: {}".format(rating))
    elif player_option not in options:
        print("Invalid input")
    else:
        computer_option = random.choice(options)
        computer_win = {}
        options_divided = len(options) // 2
        for i in range(len(options)):
            if i + 1 > options_divided:
                computer_win[options[i]] = options[i:] \
                                           + options[:abs(len(options)
                                                          - (i + options_divided + 1))]
            else:
                computer_win[options[i]] = options[i:i + options_divided + 1]
        if player_option == computer_option:
            print("There is a draw ({})".format(computer_option))
            rating += 50
        elif player_option in computer_win\
                and computer_option in computer_win[player_option]:
            print("Sorry, but computer chose {}".format(computer_option))
        else:
            print("Well done. Computer chose {} and failed".format(computer_option))
            rating += 100
