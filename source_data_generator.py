from datetime import datetime
from datetime import timedelta
from random import randint
import json

video_play_dict = {}
for i in range(1,10000):
    i += 1
    month=randint(1,12)

    if month == 2:
        day = randint(1,28)
    elif month in (4,6,9,11):
        day = randint(1,30)
    elif month not in (2,4,6,9,11):
        day = randint(1,31)

    hour = randint(1,23)
    minute = randint(1,59)

    start_time = datetime(year=2022, month=month, day=day, hour=hour, minute=minute)
    end_time = start_time + timedelta(minutes=randint(1,120))

    video_play_dict.update({f'VideoPlay{i}':{'start_time':str(start_time), 'end_time':str(end_time)}})

with open("source_data.json", "w") as outfile:
    json.dump(video_play_dict, outfile, sort_keys=False, indent=4, separators=(',', ': '))