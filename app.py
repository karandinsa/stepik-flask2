from flask import Flask

from controllers import chapter2

app = Flask(__name__)


@app.route('/')
def main():
    return chapter2.index_html()


@app.route('/departures/<departure>/')
def departures(departure):
    return chapter2.departure_html(departure)


@app.route('/tours/<id>/')
def tours(id):
    return chapter2.tour_html(id)


@app.route('/data/')
def data():
    return chapter2.data_html()


@app.route('/data/departures/<departure>/')
def data_departures(departure):
    return chapter2.data_departures_html(departure)


@app.route('/data/tours/<id>/')
def data_tours(id):
    return chapter2.data_tours_html(id)


if __name__ == '__main__':
    app.run()
