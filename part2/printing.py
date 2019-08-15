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


def option_4():
    genre_by_check = input("Please give a genre to check: ")
    count = reports.count_by_genre(file_with_statistics, genre_by_check)  # save number of genre to count
    print("The number of title in that genre -", str(count))


def run_function(number_of_function):
    if number_of_function == 1:
        print("The most played game -", str(reports.get_most_played(file_with_statistics)))
    elif number_of_function == 2:
        print("All sold from statistics is", str(reports.sum_sold(file_with_statistics)))
    elif number_of_function == 3:
        print("Averange sold is", str(reports.get_selling_avg(file_with_statistics)))
    elif number_of_function == 4:
        option_4()
    elif number_of_function == 5:
        user_title = input("Please insert a title by search in file: ")
        print("Line number by title", str(reports.get_line_number_by_title(file_with_statistics, user_title)))
    elif number_of_function == 6:
        list_sort = reports.sort_abc(file_with_statistics)
        print("List sorted:")
        for game in list_sort:
            print(game)
    elif number_of_function == 7:
        list_of_genre = reports.get_genres(file_with_statistics)
        print("List of genre:")
        for genre in list_of_genre:
            print(genre)
    elif number_of_function == 8:
        print("Release date of the top sold First-person shooter game is", str(reports.when_was_top_sold_fps(file_with_statistics)))


main()  # run program
