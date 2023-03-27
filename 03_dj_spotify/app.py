from flask import Flask, flash, request, render_template
from spotipy_client import *

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
def client_auth_form():
    if request.method == 'POST':
        # Realizar la autenticación
        sp = SpotipyClient()
        flash('Sistema listo para usar!')

    return render_template('welcome.html')