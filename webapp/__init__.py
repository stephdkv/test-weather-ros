from flask import Flask, render_template, request
from webapp.weather import weather_in_city, weather_in_city_now

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        title = 'Прогноз погоды'
        weather_now = None
        weather = None
        city = None
        if request.method == 'POST':
            # Получаем название города из формы
            city = request.form['city']
            # Получаем информацию о текущей погоде и прогнозе погоды на ближайщие дни
            weather_now = weather_in_city_now(city)
            weather = weather_in_city(city)
        # Возвращаем index.html
        return render_template('index.html', page_title=title, weather_now=weather_now, weather=weather, city=city)

    return app

