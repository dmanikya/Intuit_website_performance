import urllib2
from time import time,sleep
import requests
import pycurl
from io import BytesIO
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
from chartjs.views.pie import HighChartPieView, HighChartDonutView


User = get_user_model()

def get_data(request, *args, **kwargs):  
    return JsonResponse(data) # http response


# 1. Server response time (home page- http://localhost:8000) - On pie and bar charts:

    # 1.1. html page for server response time
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'serverresponsetime.html')

    # 1.2. Data for server response serverresponsetime.htmltime - core logic
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        default_items=[]
        labels = ["Intuit Home Page", "Intuit Wikipedia Page", "Intuit Career Page"]
        sites=["http://www.intuit.com/", "http://en.wikipedia.org/wiki/Intuit", "http://careers.intuit.com/"]  
        for i in range(3):  
            response = requests.post(sites[i], data = {'key':'value'})
            default_items.append(response.elapsed.total_seconds())
        # default_items = [2, 23, 2, 3, 12, 2]
        
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)




# 2. DNS resolution time and response time (http://localhost:8000/dns):

    # 2.1. html page for DNS performance
class DnsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dns.html', {"customers": 10})

    # 2.2. Data for DNS resolution time - core logic
class DnsResolution(APIView):

        def get(self, request, format=None):
            metrics=[]
            labels = ["TOTAL_TIME", "NAMELOOKUP_TIME", "CONNECT_TIME", "PRETRANSFER_TIME", "REDIRECT_TIME", "STARTTRANSFER_TIME","SPEED_UPLOAD"]

            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'http://www.intuit.com/')
            c.setopt(c.WRITEDATA, buffer)
            c.perform()
            body = buffer.getvalue()
        
            metrics.append(c.getinfo(pycurl.TOTAL_TIME))
            metrics.append(c.getinfo(pycurl.NAMELOOKUP_TIME))
            metrics.append(c.getinfo(pycurl.CONNECT_TIME))
            metrics.append(c.getinfo(pycurl.PRETRANSFER_TIME))
            metrics.append(c.getinfo(pycurl.REDIRECT_TIME))
            metrics.append(c.getinfo(pycurl.STARTTRANSFER_TIME))
            metrics.append(c.getinfo(pycurl.SPEED_UPLOAD))

            data = {
                "labels": labels,
                "default": metrics,
            }
            return Response(data)



# 3. Page load time(http://localhost:8000/pageload) - On line charts:

        # Helper functions - calculate() and laps() to get the page load times for the 3 websites, with 5 hits each

# calculate() : calculates the page load time 
def calculate(site):
    stream = urllib2.urlopen(site)
    start_time = time()
    output = stream.read()
    end_time = time()
    stream.close()
    return (round(end_time-start_time, 3))

# Each website is called 5 times:
def laps(i,doubleArray,site):
    for x in range(5):
        doubleArray[i].append(calculate(site))

# 3.1. Data for page load time
class ChartMixin(object):
    def get_providers(self):
        """Return names of datasets."""
        return ["Intuit Home Page", "Intuit Wikipedia Page", "Intuit Career Page"]

    def get_labels(self):
        """Return 5 labels."""
        return ["Access 1", "Access 2", "Access 3", "Access 4", "Access 5"]

    def get_data(self):
        """Return 3 random dataset to plot."""
        doubleArray=[]
        sites=["http://www.intuit.com/", "http://en.wikipedia.org/wiki/Intuit", "http://careers.intuit.com/"]
        for i in range(3):
            doubleArray.append([])
            laps(i,doubleArray,sites[i])

        return doubleArray                
        # return [[0.049, 0.02, 0.019, 0.02, 0.025],
        #         [0.062, 0.3, 0.057, 0.08, 0.095],
        #         [0.019, 0.06, 0.819, 0.22, 0.004]]



class LineChartJSONView(ChartMixin, BaseLineChartView):
    pass


class LineHighChartJSONView(ChartMixin, HighchartPlotLineChartView):
    pass

# 3.2. html page for page load
line_chart = TemplateView.as_view(template_name='pageloadtime.html')

# 3.3. Variables to display the data in line and high charts
line_chart_json = LineChartJSONView.as_view()
line_highchart_json = LineHighChartJSONView.as_view()



# Javascripts needed for line charts
highchartsvar = TemplateView.as_view(template_name='highcharts.js')
chartjsvar = TemplateView.as_view(template_name='Chart.min.js')