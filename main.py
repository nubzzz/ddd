#!/usr/bin/env python3

from flask import abort, Flask, jsonify, request
from plexapi.myplex import MyPlexAccount
import random
import os

plex_username = os.environ['PLEX_USERNAME']
plex_password = os.environ['PLEX_PASSWORD']
account = MyPlexAccount(plex_username, plex_password)
plex = account.resource('storage02').connect()

app = Flask(__name__)

def choose_ddd_episode():
    ddd_episodes = plex.library.section('TV Shows').get('Diners, Drive-ins and Dives').episodes()
    chosen_episode = random.choice(ddd_episodes)
    return_text = f"The episode chosen is: {chosen_episode.seasonEpisode} {chosen_episode.title}\n\n"
    return_text += chosen_episode.summary
    return return_text

# TO DO: ADD SEARCH FEATURE

def is_request_valid(request):
    is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
    is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']

    return is_token_valid and is_team_id_valid

@app.route('/ddd', methods=['POST'])
def ddd():
    if not is_request_valid(request):
        abort(400)

    ddd_text = choose_ddd_episode()

    return jsonify(
        response_type='in_channel',
        text=ddd_text,
    )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
