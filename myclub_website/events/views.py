from django.shortcuts import render

import calendar
from calendar import HTMLCalendar
from datetime import datetime


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Fazliddin"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # making a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    # get current year
    now = datetime.now()
    current_year = now.year
    # get a time
    time = now.strftime('%I:%M %p')

    return render(request, 'events/home.html', {
        'month': month,
        'month_number': month_number,
        'year': year,
        'cal': cal,
        'current_year': current_year,
        'time': time,
        'name': name
    })
