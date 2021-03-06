import sys
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


def count_games(file_name):
    list_games = open_file(file_name)
    count_of_games = len(list_games)
    return count_of_games


def decide(file_name, year):
    list_games = open_file(file_name)
    for game in list_games:
        if int(game[2]) == year:
            return True
    return False


def get_latest(file_name):
    list_games = open_file(file_name)
    latest_year = 1  # start year one A. D.
    title_latest_game = ""
    for game in list_games:
        if int(game[2]) > latest_year:
            latest_year = int(game[2])
            title_latest_game = game[0]
    return title_latest_game


def count_by_genre(file_name, genre):
    list_games = open_file(file_name)
    apperance = 0
    for game in list_games:
        if game[3] == genre:
            apperance += 1
    return apperance


def get_line_number_by_title(file_name, title):
    list_games = open_file(file_name)
    index = 1
    for game in list_games:
        if game[0] == title:
            return index
        index += 1
    raise ValueError

# bonus function


def sort_abc(file_name):
    list_games = open_file(file_name)
    list_title = []
    for game in list_games:
        list_title.append(game[0])
    iter = 0
    size_table = len(list_title)

    while iter < size_table:
        j = 0
        while j <= size_table-2:
            if list_title[j] > list_title[j+1]:
                temp = list_title[j+1]
                list_title[j+1] = list_title[j]
                list_title[j] = temp
            j = j+1
        iter += 1

    return list_title


def get_genres(file_name):
    list_games = open_file(file_name)
    set_genres = set({})
    for game in list_games:
        set_genres.add(game[3])
    list_games = list(set_genres)

    iter = 0
    size_table = len(list_games)

    while iter < size_table:
        j = 0
        while j <= size_table-2:
            if list_games[j] > list_games[j+1]:
                temp = list_games[j+1]
                list_games[j+1] = list_games[j]
                list_games[j] = temp
            j = j+1
        iter += 1

    return list_games


def when_was_top_sold_fps(file_name):
    list_games = open_file(file_name)
    top_sold = 0  # start sold from 0 $
    year_of_realse = 0  # start year from 0 A.D.
    last_genre = ""
    for game in list_games:
        if float(game[1]) > top_sold:
            top_sold = float(game[1])
            last_genre = game[3]
            year_of_realse = int(game[2])
    if last_genre != "First-person shooter":
        raise ValueError
    return year_of_realse
