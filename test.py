import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "32ff20c1f3389d4bd565c09bbb57cfb3"


def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    resp = requests.get(url, params=params)




    if resp.status_code != 200:
        return None

    data = resp.json()

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    desc = data["weather"][0]["description"].title()
    city_name = data["name"]

    min_temp = -30
    max_temp = 40
    percent = (temp - min_temp) / (max_temp - min_temp) * 100
    temp_percent = max(0, min(100, percent))

    return {
        "city": city_name,
        "description": desc,
        "temp": temp,
        "feels_like": feels_like,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "temp_percent": temp_percent,
    }


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            weather = get_weather(city)
            if weather is None:
                error = "City not found or API error."
        else:
            error = "Please enter a city name."

    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)