import requests as r
from bs4 import BeautifulSoup
import time
import csv
import sys
from itertools import islice
import datetime
import socket
import os
import math

teams_scraped = 0
players_scraped = 0
elapsed_time = 0
total_elapsed_seconds = 0

start_time = datetime.datetime.now()
error_messages = []

def scrapeStats(url, year):
    headers = {'user_agent': 'College Project (musicwriter93@gmail.com)'}
    response = r.get(url, headers=headers)
    page = BeautifulSoup(response.text, 'html.parser')
    tableRow = page.find(id='players_per_game.' + str(year))
    cols = tableRow.find_all('td')
    results = []
    for col in cols:
        results.append(col.text)
    return results

def get_Host_name_IP():
    ipinfo = []
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        ipinfo.append("Hostname: " + host_name)
        ipinfo.append("IP: " + host_ip)
        return ipinfo
    except:
        ipinfo.append("Unable to get Hostname and IP")
        return ipinfo

def get_elapsed_time(elapsed_time):
    global total_elapsed_seconds
    total_elapsed_seconds += elapsed_time
    hours = 0
    minutes = 0
    seconds = total_elapsed_seconds
    if total_elapsed_seconds > 60:
        minutes = math.floor(total_elapsed_seconds/60)
        seconds = total_elapsed_seconds - (minutes * 60)
        if minutes > 60:
            hours = math.floor(minutes/60)
            minutes = minutes - (hours * 60)
            seconds = total_elapsed_seconds - (minutes * 60)
    return str(hours) + ' hrs ' + str(minutes) + ' mins ' + str(seconds) + ' secs'

def get_Summary():
    summary = []
    end_time = datetime.datetime.now()
    print('\n-----SUMMARY-----', '\nStart Time:', start_time, '\nEnd Time:', end_time, '\nTeams Scraped:', teams_scraped, '\nPlayers Scraped:', players_scraped)
    for i in get_Host_name_IP():
        print(i)
    if error_messages:
        print('Errors:')
        for message in error_messages:
            print(message)


# For a new file the openType should be w, for appending to an existing file the openType should be a
# The starting index should be the row number of the row to start reading at minus 1 (e.g. row 50 is index 49)
# The ending index would be the index to stop reading at

openType = 'a'
starting_index = 0
ending_index = None
read_file = 'cbb-teams-appendage.csv'
write_file = 'team_rosters_appendage.csv'

with open(read_file, 'r', newline='') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    try:
        headerRowValues = ['player_name', 'school_code', 'year', 'played_nba', 'school_name', 'conf', 'g', 'gs', 'mp', 'fg', 'fga', 'fg_pct', 'two_p', 'two_pa', 'two_pct', 'three_p', 'three_pa', 'three_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', '', 'sos', '', 'awards']
        with open(write_file, openType, newline='') as csvwrite:
            writeCSV = csv.writer(csvwrite)
            if openType == 'w':
                writeCSV.writerow(headerRowValues)
            for row in islice(readCSV, starting_index, ending_index):
                start_time = time.time()
                school = row[0]
                year = int(float(row[19]))
                print('Elapsed Time:', get_elapsed_time(elapsed_time))
                print('Teams Scraped:', teams_scraped)
                print('Players Scraped:', players_scraped)
                print('Scraping players for line', readCSV.line_num, '-', school, str(year))
                url = 'https://www.sports-reference.com/cbb/schools/' + school + '/' + str(year) + '.html'
                headers = {'user_agent': 'College Project (musicwriter93@gmail.com)'}
                response = r.get(url, headers=headers)
                page = BeautifulSoup(response.text, 'html.parser')
                try:
                    table = page.find(id='roster')
                    rows = table.find_all('tr')
                    allResults = []
                    countPlayers = len(rows)-1
                    ## We have to minus 1 here because the first row is the header with the label "Player"
                    sys.stdout.write('['+' '*countPlayers+']')
                    sys.stdout.write('\b'*(countPlayers+1))
                    sys.stdout.flush()
                    for row in rows:
                        col = row.find(attrs={"data-stat":"player"})
                        results = []
                        if col.text != 'Player':
                            playedNBA = 0
                            if 'sr_nba' in col.get("class"):
                                playedNBA = 1
                            results.extend([col.text, school, year, playedNBA])
                            children = col.findChildren("a" , recursive=False)
                            stats_url = 'https://www.sports-reference.com' + children[0]['href']
                            playerStats = scrapeStats(stats_url, year)
                            results.extend(playerStats)
                            # time.sleep(3)
                            allResults.append(results)
                            sys.stdout.write('.')
                            sys.stdout.flush()
                            players_scraped += 1
                    sys.stdout.write('] Scraping Complete! ' + 'Writing to File\n', )
                    print('DO NOT QUIT\n')
                    for results in allResults:
                        writeCSV.writerow(results)
                    # time.sleep(3)
                    os.system('clear')
                    teams_scraped += 1
                    end_time = time.time()
                    elapsed_time = round(end_time - start_time, 2)
                except Exception as e:
                    print('Error ' + str(e))
                    error_messages.append('Unable to get data for line ' + str(readCSV.line_num) + ' ' + school + ' ' + str(year))
                    continue
        csvwrite.close()
    except KeyboardInterrupt:
        end_time = datetime.datetime.now()
        print('\n\nKeyboard Interrupt')
        get_Summary()
        print('\nLine Index in Process:', readCSV.line_num - 1, '\nSchool: ', school, '\nYear: ', year, '\n')
        csvwrite.close()
        csvfile.close()
        sys.exit(0)
end_time = datetime.datetime.now()
csvfile.close()
print('\n\nEnd of File')
get_Summary()
