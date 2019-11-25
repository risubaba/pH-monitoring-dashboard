from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from mainapp.models import MainModel
from datetime import datetime, timedelta

from .fusioncharts import FusionCharts


def index(request):
    # time_threshold = datetime.now() - timedelta(hours=100)

    l = MainModel.objects.all()
    print(l)
    data_source = OrderedDict()
    data_source['chart'] = OrderedDict({
        "caption": "pH_value (Last 20 values)",
        "yAxisName": "pH",
        "theme": "candy",
        "xAxisName": "time",
        "labelstep": 30
    })
    data_source['data'] = []
   
    data_source2 = OrderedDict()
    data_source2['chart'] = OrderedDict({
        "caption": "pH_value (All time)",
        "yAxisName": "pH",
        "theme": "candy",
        "xAxisName": "time",
        "labelstep": 30
    })
    data_source2['data'] = []
    for model in l[int(len(l))-20:]:
        xval = str(model.time.hour)+ "-" + str(model.time.minute)
        data_source["data"].append({'label': xval , 'value': float(model.pH_value)})

    for model in l:
        xval = str(model.time.day)+ "/" + str(model.time.month) + "-" +str(model.time.hour)
        data_source2["data"].append({'label': xval , 'value': float(model.pH_value)})

    graph = FusionCharts("line", "pH_value", "1000", "500", "pH_value-container", "json", data_source)
    graph2 = FusionCharts("line", "pH_value_all", "1000", "500", "pH_value-container_all", "json", data_source2)

    return render(request, 'index.html', {
        'pH_value_output': graph.render(),
        'pH_value_output_all': graph2.render()
    })