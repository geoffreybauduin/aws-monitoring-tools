from flask import Flask
from config import config
import json
from sqs.sqs import check_queue as check_sqs_queue

app = Flask(__name__)
app.debug = True

def get_conf_dict():
    conf = {}
    for section in config.sections():
        conf[section] = {}
        for item in config.items(section):
            conf[section][item[0]] = item[1]
    return conf

available_checks = {
    'sqs': check_sqs_queue
}

@app.route("/")
def health_check():
    checks = {}
    for section in config.sections():
        checks[section] = None
        len_section = len(section)
        for module, fn in available_checks.iteritems():
            if len(module) <= len_section and section[:len(module)] == module:
                checks[section] = fn(section)
    return json.dumps(checks)
        