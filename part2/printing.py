import os
import sys
import reports
from menu import Welcome_Message
from menu import Menu_Chossen
from menu import Correct_Input

# Constas data:

NUMBER_OF_MENU_BEGIN = 0
NUMBER_OF_MENU_END = 8

# Printing functions:

is_exit = False


def show_menu():
    print(Menu_Chossen)


def init():
    if len(sys.argv) > 1:
        file_with_statistics = sys.argv[1]
    else:
        file_with_statistics = "game_stat.txt"  # default value

    while is_exit is False:
        main(file_with_statistics)


def main(file_with_statistics):
    os.system("clear")
    print(Welcome_Message)
    user_choice = False
    while user_choice is False:
        user_choice = user_input()
    run_function(user_choice, file_with_statistics)


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


def run_function(number_of_function, file_with_statistics):
    if number_of_function == 1:
        print("The most played game -", str(reports.get_most_played(file_with_statistics)))
    elif number_of_function == 2:
        print("All sold from statistics is", str(reports.sum_sold(file_with_statistics)))
    elif number_of_function == 3:
        print("Averange sold is", str(reports.get_selling_avg(file_with_statistics)))
    elif number_of_function == 4:
        print("Characters long in the longest title is", str(reports.count_longest_title(file_with_statistics)))
    elif number_of_function == 5:
        print("Averange year is", str(reports.get_date_avg(file_with_statistics)))
    elif number_of_function == 6:
        title = input("Please give a title to check: ")
        game = reports.get_game(file_with_statistics, title)
        print("Proporties:")
        for value in game:
            print(value)
    elif number_of_function == 7:
        count_of_genre = reports.count_grouped_by_genre(file_with_statistics)
        print("List of genre:")
        for genre, value in count_of_genre.items():
            print(genre, "-", value)
    elif number_of_function == 8:
        print("Date ordered list is:")
        games_title = reports.get_date_ordered(file_with_statistics)
        for title in games_title:
            print(title)
    elif number_of_function == 0:
        global is_exit
        is_exit = True

    input("Please enter to continue ")


init()  # run program
