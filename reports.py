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
    latest_year = 1
    title_latest_game = ""
    for game in list_games:
        if int(game[2]) > latest_year:
            latest_year = int(game[2])
            title_latest_game = game[0]
    return title_latest_game


print(get_latest("game_stat.txt"))
