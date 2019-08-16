import sys
import math
# Report functions


def shutdown_program():
    sys.exit()


def open_file(file_name):
    list_games = []
    try:
        with open(file_name, "r") as fileopen:
            for line in fileopen:
                line = line.replace('\n', '')  # replace new line with an empty char
                list_games.append(line.split("\t"))  # divides the line of text according to tab
            return list_games
    except OSError:  # informs user if  can't find the file
        print("File '" + file_name + "' not found!\nYour program has been close.")
        shutdown_program()


def get_most_played(file_name):
    list_games = open_file(file_name)
    sold_copies = 0.0  # start from zero sold copies
    title_famoust_game = ""
    for game in list_games:
        if float(game[1]) > sold_copies:
            sold_copies = float(game[1])
            title_famoust_game = game[0]
    return title_famoust_game


def sum_sold(file_name):
    list_games = open_file(file_name)
    sold_copies = 0.0  # start from zero sold copies
    for game in list_games:
        sold_copies += float(game[1])
    return sold_copies


def get_selling_avg(file_name):
    list_games = open_file(file_name)
    sold_copies = 0.0  # start from zero sold copies
    index = 0.0
    for game in list_games:
        sold_copies += float(game[1])
        index += 1.0
    averange = sold_copies / index
    return averange


def count_longest_title(file_name):
    list_games = open_file(file_name)
    length = 0
    for game in list_games:
        if len(game[0]) > length:
            length = len(game[0])
    return length


def get_date_avg(file_name):
    list_games = open_file(file_name)
    year_published = 0  # start from zero year
    index = 0
    for game in list_games:
        year_published += int(game[2])
        index += 1
    averange = year_published / index
    return math.ceil(averange)


def get_game(file_name, title):
    list_games = open_file(file_name)
    for game in list_games:
        if title == game[0]:
            game[1] = float(game[1])
            game[2] = int(game[2])
            return game
    return False


# Bonus function


def count_grouped_by_genre(file_name):
    list_games = open_file(file_name)
    dict_genre = {}

    #  sorting by alphabetical by genre
    iter = 0
    size_table = len(list_games)

    while iter < size_table:
        j = 0
        while j <= size_table-2:
            if list_games[j][3] > list_games[j+1][3]:
                temp = list_games[j+1]
                list_games[j+1] = list_games[j]
                list_games[j] = temp
            j = j+1
        iter += 1
    for game in list_games:
        if game[3] in dict_genre:
            dict_genre[game[3]] += 1
        else:
            dict_genre[game[3]] = 1

    return dict_genre


def get_date_ordered(file_name):
    list_games = open_file(file_name)
    list_title = []
    #  sorting by alphabetical
    iter = 0
    size_table = len(list_games)

    while iter < size_table:
        j = 0
        while j <= size_table-2:
            if list_games[j][0] > list_games[j+1][0]:
                temp = list_games[j+1]
                list_games[j+1] = list_games[j]
                list_games[j] = temp
            j = j+1
        iter += 1
    #  sorting by date
    iter = 0
    size_table = len(list_games)

    while iter < size_table:
        j = 0
        while j <= size_table-2:
            if int(list_games[j][2]) < int(list_games[j+1][2]):
                temp = list_games[j+1]
                list_games[j+1] = list_games[j]
                list_games[j] = temp
            j = j+1
        iter += 1
    # create list of title
    for game in list_games:
        list_title.append(game[0])

    return list_title
