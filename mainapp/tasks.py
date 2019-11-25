from celery import task
from .models import MainModel
from pH_monitoring.settings import OneM2M_IP
import requests
from datetime import datetime, timedelta

@task()
def import_values():
    model = MainModel()
    URL = "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team12_Water_pH_monitoring/node_1/la"
    headers = {
        "X-M2M-Origin": "admin:admin",
        "Accept": "application/json"
    }
    data = requests.get(URL, headers=headers).json()
    val = data['m2m:cin']['con']
    time = data['m2m:cin']['ct']

    year = int(time[0:4])
    month = int(time[4:6])
    day = int(time[6:8])
    hour = int(time[9:11])
    minute = int(time[11:13])
    seconds = int(time[13:15])
    recordGMT = datetime(year, month, day, hour, minute, seconds)
    recordIST = recordGMT + timedelta(hours=5, minutes=30)
    model.time = recordIST
    model.pH_value = float(val[1:5])
    model.save()

def load_values(cnt):
    model = MainModel()
    URL = "http://onem2m.iiit.ac.in:443/~/in-cse/cin-" + cnt
    headers = {
        "X-M2M-Origin": "admin:admin",
        "Accept": "application/json"
    }
    print(URL)
    data = requests.get(URL, headers=headers).json()
    val = data['m2m:cin']['con']
    time = data['m2m:cin']['ct']

    year = int(time[0:4])
    month = int(time[4:6])
    day = int(time[6:8])
    hour = int(time[9:11])
    minute = int(time[11:13])
    seconds = int(time[13:15])
    recordGMT = datetime(year, month, day, hour, minute, seconds)
    recordIST = recordGMT + timedelta(hours=5, minutes=30)
    model.time = recordIST
    model.pH_value = float(val[1:5])
    model.save()