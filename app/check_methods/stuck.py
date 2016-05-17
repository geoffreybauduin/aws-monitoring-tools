from config import config
import time

data = {}

# Default behavior: no message count decrease in the last 5 minutes
def __check(key):
    current_timestamp = time.time()
    five_minutes_ago = current_timestamp - 5 * 60
    last_value = None
    for value in data[key]['values']:
        if five_minutes_ago >= value['time']:
            if last_value is not None and last_value['value'] > value['value']:
                return False
            last_value = value
    return last_value is not None

def stuck(section, key, value):
    value = int(value)
    data.setdefault(key, {'values':[]})
    if value == 0:
        data[key]['values'] = []
        return False
    else:
        data[key]['values'].append({
            'time': time.time(),
            'value': value,
        })
        return __check(key)