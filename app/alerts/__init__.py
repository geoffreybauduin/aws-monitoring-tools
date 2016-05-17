from app.alerts.email import send_email
from config import config

def alert(section, key, value):
    method = config.get(section, "alert_method")
    if method == "email":
        send_email(section, key, value)