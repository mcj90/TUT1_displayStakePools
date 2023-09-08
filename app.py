from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://api.koios.rest/api/v0/pool_list"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pool_list = response.json()
    else:
        pool_list = None

    return render_template('index.html', pool_list=pool_list)

if __name__ == '__main__':
    app.run()