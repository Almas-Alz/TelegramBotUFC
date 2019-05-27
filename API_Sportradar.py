import requests
import apikey
from datetime import datetime
import time

key = '?api_key=' + apikey.key
URL = 'https://api.sportradar.us/ufc/trial/v2/en/'

doc = '''
Hello, I'm UFC bot. 
----------------------------
These commands will help you:
/top - show top 10 fighters in UFC
/fnum{} - show main info about fighter in top 10
          where {} - number from 1 to 10
/coming - show future events in UFC
/champion - surprise :)
----------------------------
'''

def rankings():
    """Top 10 fighters in UFC"""

    url = URL + 'rankings.json' + key
    response = requests.get(url).json()

    t = []  # top 10 fighters in UFC

    for i in range(10):
        fighter = response['rankings'][0]['competitor_rankings'][i]['competitor']['name']
        t.append(fighter)

    result = '***** TOP FIGHTERS IN UFC *****\n1. {}\n2. {}\n3. {}\n4. {}\n5. {}\n6. {}\n7. {}\n8. {}\n9. {}\n10. {}'.format(t[0],
    t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9])

    return result


def t_id():
    """Function that returns id list of fighters in top 10"""

    url = URL + 'rankings.json' + key
    response = requests.get(url).json()

    t_id = []  # id of each fighter in list "t"

    for i in range(10):
        fighter_id = response['rankings'][0]['competitor_rankings'][i]['competitor']['id']
        t_id.append(fighter_id)

    return t_id


def about_f(num):
    """Information about fighter in the top 10"""

    id_of_fighters = t_id()

    if num == 1:
        url = URL + 'competitors/' + id_of_fighters[0] + '/profile.json' + key
    elif num == 2:
        url = URL + 'competitors/' + id_of_fighters[1] + '/profile.json' + key
    elif num == 3:
        url = URL + 'competitors/' + id_of_fighters[2] + '/profile.json' + key
    elif num == 4:
        url = URL + 'competitors/' + id_of_fighters[3] + '/profile.json' + key
    elif num == 5:
        url = URL + 'competitors/' + id_of_fighters[4] + '/profile.json' + key
    elif num == 6:
        url = URL + 'competitors/' + id_of_fighters[5] + '/profile.json' + key
    elif num == 7:
        url = URL + 'competitors/' + id_of_fighters[6] + '/profile.json' + key
    elif num == 8:
        url = URL + 'competitors/' + id_of_fighters[7] + '/profile.json' + key
    elif num == 9:
        url = URL + 'competitors/' + id_of_fighters[8] + '/profile.json' + key
    elif num == 10:
        url = URL + 'competitors/' + id_of_fighters[9] + '/profile.json' + key

    response = requests.get(url).json()

    name = response['competitor']['name']
    nickname = response['info']['nickname']
    height = str(response['info']['height'])
    weight = str(response['info']['weight'])
    wins = str(response['record']['wins'])
    draws = str(response['record']['draws'])
    losses = str(response['record']['losses'])

    result = '***** About this fighter *****\nname: {}\nnickname: {}\nheight: {} cm\nweight: {} kg\nwins: {}\ndraws: {}\nlosses: {}'.format(name,
    nickname, height, weight, wins, draws, losses)

    return result


def coming():
    """Returns future events"""

    url = URL + 'seasons.json' + key
    response = requests.get(url).json()

    today_str = datetime.today().strftime('%Y-%m-%d')  # date today (str)
    today = time.strptime(today_str, "%Y-%m-%d")  # from str to python date format
    events = []
    events_id = []
    events_date = []
    ln = len(response['seasons'])

    for i in range(ln):
        ev_date = response['seasons'][i]['start_date']
        ev_date_py = time.strptime(ev_date, "%Y-%m-%d")  # from str to python date format

        if ev_date_py > today:
            events.append(response['seasons'][i]['name'])
            events_id.append(response['seasons'][i]['id'])
            events_date.append(ev_date)

    title = "***** Future events *****\n"
    title2 = "\n***** Date of these events *****\n"
    result = title + "\n".join(events) + title2 + "\n".join(events_date)

    return result



