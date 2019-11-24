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
    l = data['m2m:cin']['con']
    model.pH_value = float(l[1:5])
    model.save()
