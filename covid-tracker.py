import sys
import requests

from tabulate import tabulate

table = []
total_cases_global = 0
total_cases_philippines = 0
latest_date = 0


# check covid-19 updates around the globe
def scan_updates():
    URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series time_series_covid19_confirmed_global.csv'
    request = requests.get(URL)
    url_content = request.content

    csv_file = open('covid-data.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

    update_statistics()


def update_statistics():
    global table, total_cases_global, total_cases_philippines, latest_date

    try:
        file_handler = open('covid-data.csv')

        for line in file_handler:
            line = line.rstrip()
            line = line.split(',')

            if table == []:
                table.append([line[0], line[1], 'As of ' + line[-1]])
                latest_date = line[-1]
                continue

            if line[1] == 'Philippines':
                total_cases_philippines = int(line[-1])

            total_cases_global = total_cases_global + int(line[-1])
            table.append([line[0], line[1], line[-1]])

    except Exception as e:
        print(e)


# Run console
def run_console():
    print('Welcome to COVID-19 daily updates')
    print('As of', latest_date, 'there are a total of', total_cases_global, 'cases global.\n')

    user_input = ''
    while user_input != '3':
        print('\n')
        print(tabulate([['(0) Total cases global'], ['(1) Cases around the '], ['(2) Total cases in the Philippines'], ['(3) Exit']], headers=['See more:'], tablefmt="github"))
        user_input = input('>>')

        if user_input == '1':
            print(f'Total cases in the Philippines: {total_cases_philippines}')
            continue
        elif user_input == '2':
            print(tabulate(table, headers='firstrow'))
            continue
        elif user_input == '3':
            sys.exit(0)
        else:
            print('Syntax error!')
            continue


# main program
scan_updates()
run_console()

