from flask import render_template
from data import tours, departures
def tour_html(id):
    return render_template('tour.html',tour = tours[int(id)], departure = departures)