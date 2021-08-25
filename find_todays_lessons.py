import json
import datetime

def find_lessons():
    today = datetime.date.today()
    month = today.month
    day = today.day
    filename = f'months/{month}.json'
    with open(filename) as json_file:
        dict = json.load(json_file)
        day_lessons = dict[day-1]
        morning = day_lessons['morning']
        evening = day_lessons['evening']
        print(f""" Today's lessons are: 

        Morning Prayer
            First: {morning['first']}
            Second: {morning['second']}
            
        Evening Prayer: 
            First: {evening['first']}
            Second: {evening['second']}
            
            """)
            

find_lessons()