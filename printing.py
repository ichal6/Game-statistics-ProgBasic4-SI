import os
import time
import reports
from menu import Welcome_Message
from menu import Menu_Chossen
from menu import Correct_Input

# Constas data:

NUMBER_OF_MENU_BEGIN = 1
NUMBER_OF_MENU_END = 8

# temporary value:

file_with_statistics = "game_stat.txt"  # implement choose diffrent file name

# Printing functions:


def show_menu():
    print(Menu_Chossen)


def main():
    os.system("clear")
    print(Welcome_Message)
    user_choice = False
    while user_choice is False:
        user_choice = user_input()
    run_function(user_choice)


def user_input():
    try:
        show_menu()
        user_choice = int(input())
        if user_choice in range(NUMBER_OF_MENU_BEGIN, NUMBER_OF_MENU_END + 1):
            return user_choice
        print(Correct_Input)
        return False
    except ValueError:
        print(Correct_Input)
        return False


def option_2():
    try:
        year_by_check = int(input("Please give a year of publishing: "))
        is_count = reports.decide(file_with_statistics, year_by_check)
        if is_count:
            print("Yes, in statistics is this game")
        else:
            print("No, in statisctics is any this game")
    except ValueError:
        print("Insert incorrect value! Return to main menu.")
        time.sleep(2)
        main()


def option_4():
    genre_by_check = input("Please give a genre to check: ")
    count = reports.count_by_genre(file_with_statistics, genre_by_check)  # save number of genre to count
    print("The number of title in that genre -", str(count))


def run_function(number_of_function):
    if number_of_function == 1:
        print("Count games in statistics -", str(reports.count_games(file_with_statistics)))
    elif number_of_function == 2:
        option_2()
    elif number_of_function == 3:
        print("Title of the latest game is", str(reports.get_latest(file_with_statistics)))
    elif number_of_function == 4:
        option_4()
    elif number_of_function == 5:
        user_title = input("Please insert a title by search in file: ")
        print("Line number by title", str(reports.get_line_number_by_title(file_with_statistics, user_title)))
    elif number_of_function == 6:
        print("Not implemention, yet")
    elif number_of_function == 7:
        print("Not implemention, yet")
    elif number_of_function == 8:
        print("Not implemention, yet")


main()  # run program
