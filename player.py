import requests
import os
from time import sleep
from influxdb import InfluxDBClient
from datetime import datetime
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

ENV_VARS = ['INFLUXDB_HOST', 'INFLUXDB_PORT', 'INFLUXDB_LOGIN', 'INFLUXDB_PASSWORD', 'INFLUXDB_DATABASE', 'CR_API_TOKEN', 'PLAYER_TAG']

def _required_vars():
    for var in ENV_VARS:
        if var not in os.environ:
           logging.error("Please set {}".format(var))
           exit(1)

MEASUREMENT = "players"
SLEEP_SECONDS = 300

_required_vars()

while 1:
    logging.info('Get players stats for CR api')
    headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(os.environ['CR_API_TOKEN']),
            }
    request = requests.get('https://api.clashroyale.com/v1/players/%23{}'.format(os.environ['PLAYER_TAG']), headers=headers)
    
    if request.status_code == 200:
    
        logging.info('Connecting to {}:{}/{}'.format(os.environ['INFLUXDB_HOST'], os.environ['INFLUXDB_PORT'], os.environ['INFLUXDB_DATABASE']))
        client = InfluxDBClient(os.environ['INFLUXDB_HOST'], os.environ['INFLUXDB_PORT'], os.environ['INFLUXDB_LOGIN'], os.environ['INFLUXDB_PASSWORD'], os.environ['INFLUXDB_DATABASE'])

        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        player = request.json()
        json_body = {
            "measurement": MEASUREMENT,
            "tags": {
               "player_name": player['name'].replace(' ', '_'),
               "player_tag": player['tag']
            },
            "time": current_time,
            "fields": {
                "expLevel": int(player['expLevel']),
                "trophies": int(player['trophies']),
                "bestTrophies": int(player['bestTrophies']),
                "wins": int(player['wins']),
                "losses": int(player['losses']),
                "battleCount": int(player['battleCount']),
                "threeCrownWins": int(player['threeCrownWins']),
                "challengeCardsWon": int(player['challengeCardsWon']),
                "challengeMaxWins": int(player['challengeMaxWins']),
                "tournamentCardsWon": int(player['tournamentCardsWon']),
                "tournamentBattleCount": int(player['tournamentBattleCount']),
                "donations": int(player['donations']),
                "donationsReceived": int(player['donationsReceived']),
                "totalDonations": int(player['totalDonations']),
                "warDayWins": int(player['warDayWins']),
                "clanCardsCollected": int(player['clanCardsCollected'])
            }
        }
    
        logging.info("Writing data to influxdb")
        logging.info(json_body)
        client.write_points([json_body])

        logging.info("Closing influxdb connection")
        client.close()
    
    else:
        logging.error(request.text)
        exit(1)

    logging.info("Waiting {}s".format(SLEEP_SECONDS))
    sleep(SLEEP_SECONDS)

