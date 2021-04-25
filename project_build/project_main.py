from flask import Flask, request
from pyhtml import html, body, p, form, input_, img

import requests
import json
import sqlite3

# pip install pyxivapi
# requirements for xivapi
import asyncio
import aiohttp
import pyxivapi
import logging



app = Flask(__name__)

#==========================================================================================================
@app.route('/')
# Main page: header, navigation (make profile, search players)
def main():

    players_goto = form(action='players')(
      input_(type='submit', name='Search players', value='Browse players')
    )

    test_player = form(action='test')(
      input_(type='text', name='test_id', value='enter test ID'),
      input_(type='submit', value='Test ID')
    )

    page_body = html(
      body(
        p("Hi"),
        players_goto,
        #img(src=player_info['avatar'])
        test_player
      )
    )

    return str(page_body)

#==========================================================================================================
@app.route('/players', methods=['POST'])
# The page where all players are displayed, with search/filter options
# Click on a player card to go to their page that has more details and links to other sites (eg. fflogs)
def players_main():

    response = html(
      body(
        p("This is the page where players are listed")
      )
    )

    return str(response)


#==========================================================================================================
@app.route('/test', methods=['POST'])
# For testing purposes

def test_page():

    test_id = request.form['test_id']
    
    player_list = []

    f = open('players.csv', 'r')
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        player_list.append(row)
    f.close()

    #for player in players_list:
    #  print(player['name'])

    return player_list




#==========================================================================================================
#@app.route('/register')
# The page where you can register your character and make an entry on the app



if __name__ == "__main__":
    app.run(debug=True)


#players = {"Dominic Dice": {"Job": "Paladin", "Language": "English", "Commitment": "Midcore"}, "Vanilla Meowmeow": {"Job": "Black Mage", "Language": "English", "Commitment": "Hardcore"}}

#def player_search_job(job):
  #for player in players:
    #if job == players[player]["Job"]:
      #display_info(player)

#def display_info(player):
  #print(player + "\nJob: " + players[player]["Job"] + "\nLanguage: " + players[player]["Language"] + "\nCommitment: " + players[player]["Commitment"])