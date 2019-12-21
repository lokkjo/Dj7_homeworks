import csv
from pprint import pprint

from django.shortcuts import render

from .settings import STATIC_URL, STATICFILES_DIRS



def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    inf_path = str(STATICFILES_DIRS[0]) + r'\app'
    inflation_file = f'{inf_path}\inflation_russia.csv'
    inflation_data = []
    with open(inflation_file, newline='',
              encoding='UTF-8') as inf_csvfile:
        reader = csv.DictReader(inf_csvfile, delimiter=';')
        for row in reader:
            # print(row)
            inf_row = {
                'Year': row['Год'],
                'Jan': row['Янв'],
                'Feb': row['Фев'],
                'Mar': row['Мар'],
                'Apr': row['Апр'],
                'May': row['Май'],
                'Jun': row['Июн'],
                'Jul': row['Июл'],
                'Aug': row['Авг'],
                'Sep': row['Сен'],
                'Oct': row['Окт'],
                'Nov': row['Ноя'],
                'Dec': row['Дек'],
                'Sum': row['Суммарная'],
            }
            inflation_data.append(inf_row)


    context = {
        'inflation_data': inflation_data
    }

    return render(request, template_name,
                  context)