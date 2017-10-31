"""charts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .views import HomeView, DnsView, get_data, ChartData, line_chart_json, line_highchart_json, line_chart, chartjsvar, highchartsvar, DnsResolution


urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    
    # Javascripts for line charts
    url(r'^highcharts.js$', highchartsvar, name='home'),
    url(r'^Chart.min.js$', chartjsvar, name='home'),

    # Server response time - On pie and bar charts:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),

    # DNS resolution time and response time:
    url(r'^dns$', DnsView.as_view(), name='home'),
    url(r'^api/dns/data/$', DnsResolution.as_view()),

    # Page load time - On line charts
    url(r'^pageload$', line_chart, name='home'),
    url(r'^line$', line_chart_json, name="line-chart-json"),
    url(r'^highline$', line_highchart_json, name="highline-chart-json")
]
