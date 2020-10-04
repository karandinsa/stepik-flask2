from flask import render_template
from data import tours
import random
def index_html():
    tours6 ={}
    for i in range(1,7):
        tours6[i] = tours[i]

    return render_template('index.html',tour = tours6)