from flask import render_template
from data import departures, tours
def departure_html(departure):
    ret_departure = {}
    deps_dict = []
    for i in tours.keys():
        if tours[i]["departure"] == departure:
            ret_departure[i] = tours[i]
            deps_dict.append(tours[i])
    return render_template('departure.html',
                           tour = ret_departure,
                           departures = departures[departure],
                           deps = deps_dict)