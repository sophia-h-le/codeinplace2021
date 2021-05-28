from copy_player import *
from copy_recorder import *

def get_input_and_run():
    action = input("Do you want to play or record? Type 'play' or 'record': ")

    while (action != 'play') and (action != 'record'):
        action = input("Please type 'play' or 'record' to continue: ")

    if action == 'play':
        play()
    else:
        record()

get_input_and_run()

repeat = input("Do you want to continue? Type 'yes' to continue. ")
while repeat == 'yes':
    get_input_and_run()
    repeat = input("Do you want to continue? Type 'yes' to continue. ")

print('Thank you! Hope you had a good time!')
