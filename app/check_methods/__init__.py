from app.check_methods.stuck import stuck
from app.alerts import alert

def __check(method, section, key, value):
    if method == 'stuck':
        return stuck(section, key, value)
    return False

def check(method, section, key, value):
    c = __check(method, section, key, value)
    if c is True:
        # Alert
        alert(section, key, value)
    return c
        