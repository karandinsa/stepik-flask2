from flask import render_template

from data import departures, tours
import data as tours_data


def check_departure(departure):
    if departure not in departures.keys():
        ret = "<h1>Неверный пункт отправления</h1>" \
              "<p>Верные пункты: " + ",".join(departures.keys()) + "</p>"
        return ret, 404
    else:
        return "OK", 200


def check_tour(id):
    ret = "<h1>Такого тура не существует</h1>"
    try:
        if int(id) not in tours.keys():
            return ret, 404
        else:
            return "OK", 200
    except Exception as e:
        return ret, 404


def index_html():
    tours6 = {}
    for i in range(1, 7):
        tours6[i] = tours[i]

    return render_template('index.html',
                           tour=tours6,
                           departures_menu=departures)


def departure_html(departure):
    ret, status = check_departure(departure)
    if status == 200:
        ret_departure = {}
        deps_dict = []
        for i in tours.keys():
            if tours[i]["departure"] == departure:
                ret_departure[i] = tours[i]
                deps_dict.append(tours[i])
        return render_template('departure.html',
                               tour=ret_departure,
                               departures=departures[departure],
                               deps=deps_dict,
                               departures_menu=departures)
    else:
        return ret


def tour_html(id):
    ret, status = check_tour(id)
    if status == 200:
        return render_template('tour.html',
                               tour=tours[int(id)],
                               departure=departures,
                               departures_menu=departures)
    else:
        return ret


def data_html():
    ret = "<h1>Все туры:</h1>" + "\n"
    for i in tours_data.tours.keys():
        ret = ret + "<p>" + \
              tours_data.tours[i]["country"] + \
              ': <a href="/data/tours/' + str(i) + '/">' + \
              tours_data.tours[i]["title"] + \
              "</a></p>"
    return ret


def data_departures_html(departure):
    ret, status = check_departure(departure)
    if status == 200:
        departure_place = "Неверный пункт отправления"
        ret_departure = ""
        for i in tours_data.tours.keys():
            if tours_data.tours[i]["departure"] == departure:
                ret_departure = ret_departure + \
                                "<p>" + tours_data.tours[i]["country"] + ':<a href="/tours/' + str(i) + '/">' + \
                                tours_data.tours[i]["title"] + "</a></p>\n"
                departure_place = tours_data.departures[departure]

        return "<h1>Туры по направлению " + departure_place + ": </h1>\n" + ret_departure
    else:
        return ret


def data_tours_html(id):
    ret, status = check_tour(id)
    if status == 200:
        td = tours_data.tours[id]
        ret_tour = "<h1>" + td["country"] + ": " + td["title"] + ":</h1>\n" + \
                   "<p>" + str(td["nights"]) + " ночей</p>\n" + \
                   "<p>Стоимость: " + str(td["price"]) + " Р</p>\n" + \
                   "<p>" + td["description"] + "</p>"

        return ret_tour
    else:
        return ret
