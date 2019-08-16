import os
import sys
import time
import reports
from menu import Welcome_Message
from menu import Menu_Chossen
from menu import Correct_Input

# Constas data:

NUMBER_OF_MENU_BEGIN = 0
NUMBER_OF_MENU_END = 8

# Export functions

is_exit = False


def show_menu():
    print(Menu_Chossen)


def init():
    answer_to_save = ""
    if len(sys.argv) > 1:
        file_with_statistics = sys.argv[1]
    else:
        file_with_statistics = "game_stat.txt"  # default value

    while is_exit is False:
        answer_to_save += main(file_with_statistics, answer_to_save) + "\n"

    export_to_file("game_stat", answer_to_save)


def main(file_with_statistics, answer_to_save):
    os.system("clear")
    print(Welcome_Message)
    user_choice = False
    while user_choice is False:
        user_choice = user_input()
    answer_to_save = run_function(user_choice, file_with_statistics)
    return answer_to_save


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


def option_2(file_with_statistics):
    try:
        year_by_check = int(input("Please give a year of publishing: "))
        is_count = reports.decide(file_with_statistics, year_by_check)
        if is_count:
            string = "Yes, in statistics is this game"
            return string
        else:
            string = "No, in statisctics is any this game"
            return string
    except ValueError:
        print("Insert incorrect value! Return to main menu.")
        time.sleep(2)
        main(file_with_statistics, "")


def option_4(file_with_statistics):
    genre_by_check = input("Please give a genre to check: ")
    count = reports.count_by_genre(file_with_statistics, genre_by_check)  # save number of genre to count
    string = "The number of title in that genre -" + str(count)
    return string


def run_function(number_of_function, file_with_statistics):
    if number_of_function == 1:
        answer_to_save = "The most played game - " + str(reports.get_most_played(file_with_statistics))
        return answer_to_save
    elif number_of_function == 2:
        answer_to_save = "All sold from statistics is " + str(reports.sum_sold(file_with_statistics))
        return answer_to_save
    elif number_of_function == 3:
        return "Averange sold is " + str(reports.get_selling_avg(file_with_statistics))
    elif number_of_function == 4:
        answer_to_save = "Characters long in the longest title is " + str(reports.count_longest_title(file_with_statistics))
        return answer_to_save
    elif number_of_function == 5:
        answer_to_save = "Averange year is " + str(reports.get_date_avg(file_with_statistics))
        return answer_to_save
    elif number_of_function == 6:
        title = input("Please give a title to check: ")
        game = reports.get_game(file_with_statistics, title)
        proporties = "List sort:\n"
        for proportie in game:
            proporties += str(proportie) + "\n"
        return proporties
    elif number_of_function == 7:
        count_of_genre = reports.count_grouped_by_genre(file_with_statistics)
        genres = "List of genre:\n"
        for genre in count_of_genre:
            genres += genre + "\n"
        return genres
    elif number_of_function == 8:
        list_of_order = "Date ordered list is: "
        games_title = reports.get_date_ordered(file_with_statistics)
        for title in games_title:
            list_of_order += title + "\n"
    elif number_of_function == 0:  # click zero to exit
        global is_exit
        is_exit = True

    return ""


def export_to_file(file_name, all_answer):

    try:
        with open(file_name, "w") as fileopen:
            fileopen.write(all_answer)
    except OSError:  # informs user if  can't find the file
        print("File '" + file_name + "' not found!\nYour program has been close.")


init()
