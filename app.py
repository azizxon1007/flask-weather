from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = '44a76a61047d740fce7b1579392bc737'  # Replace with your actual API key
        weather_data = get_weather(city, api_key)
    return render_template('index.html', weather=weather_data)

def get_weather(city, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == '__main__':
    app.run(debug=True)
