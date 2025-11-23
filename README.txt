Weather App - Flask + Docker

1. Description
This is a simple Weather Web Application built with Flask. 
A user enters a city name, and the app retrieves current temperature, weather description, humidity, 
and wind speed from OpenWeatherMap API. The result displays in a clean web UI along with a temperature bar.

The app can run in two ways:
(1) Run directly on your computer (Python environment)
(2) Run inside a Docker container using Docker Desktop


2. How to Run the App Without Docker (Direct Python Run)

Requirements:
- Python 3.x installed
- The file requirements.txt in project folder

Steps:
1. Open a terminal inside the project folder.
2. Install packages:
   pip install -r requirements.txt
3. Run the app:
   python test.py
4. Open your browser and go to:
   http://127.0.0.1:5000


3. How to Run the App Using Docker Desktop

You can run the app using Docker. There are two ways:

---------------------------------------------------------
A. RUNNING IMAGE YOU BUILT LOCALLY
---------------------------------------------------------

1. Build the Docker image:
   docker build -t weather-app .

2. Run the container and map port 5000:
   docker run -p 5000:5000 weather-app

Very important:
- The left side (5000) is your computer’s port.
- The right side (5000) is the Flask port inside the container.
If this is not mapped correctly, the website will not open.

3. Open your browser:
   http://127.0.0.1:5000

---------------------------------------------------------
B. RUNNING IMAGE FROM DOCKER HUB
---------------------------------------------------------

1. Pull the image:
   docker pull yin00050/weather-app

2. Run the container:
   docker run -p 5000:5000 yin00050/weather-app

3. Open your browser:
   http://127.0.0.1:5000


4. Using Docker Desktop (GUI method)

If you prefer using buttons instead of command line:

1. Open Docker Desktop
2. Go to Images tab
3. Find your image (weather-app or yin00050/weather-app)
4. Click RUN
5. In "Optional Settings":
     - Check "Publish all exposed ports"
     - OR manually add a port mapping:
         Host port: 5000
         Container port: 5000
6. Click Run
7. Open your browser:
   http://127.0.0.1:5000

GitHub repository：https://github.com/wo4aizjd/weather-app
Docker Hub:https://hub.docker.com/r/yin00050/weather-app
