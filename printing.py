import os
from menu import Welcome_Message
from menu import Menu_Chossen
from menu import Correct_Input

# Constas data:

NUMBER_OF_MENU_BEGIN = 1
NUMBER_OF_MENU_END = 8

# Printing functions:


def main():
    os.system("clear")
    print(Welcome_Message)
    user_choice = False
    while user_choice is False:
        user_choice = user_input()


def user_input():
    try:
        show_menu()
        user_choice = int(input())
        if user_choice in range(NUMBER_OF_MENU_BEGIN, NUMBER_OF_MENU_END + 1):
            return True
        print(Correct_Input)
        return False
    except ValueError:
        print(Correct_Input)
        return False


def show_menu():
    print(Menu_Chossen)


main()
