from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

import json
from json import JSONEncoder

bp = Blueprint('dj_spotify', __name__)

@bp.route('/')
def index():
    cur = get_db().cursor()
    cur.execute(
        'SELECT id, acousticness, danceability, duration_ms, energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, valence'
        ' FROM tracks'
    )
    r = [dict((cur.description[i][0], value) \
         for i, value in enumerate(row )) \
         for row in cur.fetchall()]
    
    return json.dumps(r)

# @bp.route('/get_prediction', method=('GET', 'POST'))
# def get_prediction():
#     Obtener el dataframe del usuario
#     Obtener el dataframe del DMC (base de datos)
#     retornar la predicción



