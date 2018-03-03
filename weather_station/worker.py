import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging


def fetch_data():
    api_token = '9fd0d5429a3fd32c'
    url = 'http://api.wunderground.com/api/' + api_token + '/conditions/q/CA/San_Francisco.json'
    r = requests.get(url).json()
    data = r['current_observation']
    location = data['observation_location']['full']
    weather = data['weather']
    wind_str = data['wind_string']
    temp = data['temp_f']
    humidity = data['relative_humidity']
    precip = data['precip_today_string']
    icon_url = data['icon_url']
    observation_time = data['observation_time']
    print(data)
    print(r)
"""
    #open db
    try:
        conn = psycopg2.connect(dbname='weather', user='postgres', host='localhost', password='postgres')
        print('Database connected')
    except:
        print(datetime.now(), "Unable to connect to database")
        logging.exception(datetime.now(), "Unable to connect/open the database")
        return
    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # save data to dbase
    cur.execute(insert into station_reading (location, weather, wind_str, temp, humidity, precip, icon_url, observation_time) values (%s, %s, %s, %s, %s, %s, %s, %s), (location, weather, wind_str, temp, humidity, precip, icon_url, observation_time))
    conn.commit()
    cur.close()
    conn.close()
    print('New data writen at: ', datetime.now())

fetch_data()"""

fetch_data()