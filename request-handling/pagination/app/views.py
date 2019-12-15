import csv
from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings

bus_stations_file = settings.BUS_STATION_CSV
bus_station_data = []
with open(bus_stations_file, newline='',
          encoding='CP1251') as bus_csvfile:
    reader = csv.DictReader(bus_csvfile)
    for row in reader:
        bus_stop = {'Name': row['Name'],
               'Street': row['Street'],
               'District': row['District']}
        bus_station_data.append(bus_stop)

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page_num = int(request.GET.get('page', 1))
    count = 10

    paginator = Paginator(bus_station_data, count)

    if page_num >= paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.get_page(page_num)

    data = page.object_list

    if page_num <= 1:
        prev_page_url = None
    else:
        prev_params = {'page': f'{page_num - 1}'}
        prev_page_url = f'{reverse("bus_stations")}?{urlencode(prev_params)}'

    if page_num >= paginator.num_pages:
        next_page_url = None
    else:
        next_params = {'page': f'{page_num + 1}'}
        next_page_url = f'{reverse("bus_stations")}?{urlencode(next_params)}'

    context = {
        'bus_stations': data,
        'current_page': page_num,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }
    return render_to_response('index.html', context=context)

