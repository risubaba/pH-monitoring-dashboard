from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from mainapp.models import MainModel
from datetime import datetime, timedelta

from .fusioncharts import FusionCharts


def index(request):
    # time_threshold = datetime.now() - timedelta(hours=100)

    l = MainModel.objects.filter()

    data_source = OrderedDict()
    data_source['chart'] = OrderedDict({
        "caption": "pH_value (All time)",
        "yAxisName": "pH",
        "theme": "candy"
    })
    data_source['data'] = []
   
    i = 1

    for model in l:
        data_source["data"].append({'label': i, 'value': float(model.pH_value)})
        i = i + 1

    graph = FusionCharts("line", "pH_value", "800", "500", "pH_value-container", "json", data_source)

    return render(request, 'index.html', {
        'pH_value_output': graph.render(),
    })