from flask import Flask, render_template, request
import weather

app = Flask(__name__)

API_KEY = 'c613f5fe08ec7f312fc6f6e3e1de2f8e'

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'POST':
        # Get the selected city from the button clicked
        city = request.form.get('city')  # This retrieves the city from the button
        return weather_page(city)  # Call weather_page with the selected city

    return render_template('location.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather_page(city=None):
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = weather.get_weather(city, API_KEY)

        if isinstance(weather_data, str):
            weather_data = None

    return render_template('index.html', weather_data=weather_data)

@app.route('/Expect_Weather', methods=['GET', 'POST'])
def expected_weather():
    forecast_data = None
    city = request.args.get('city')  
    days = 1  

    if city:
        forecast_data = weather.get_forecast(city, API_KEY, days=days)
    
    return render_template('expected.html', forecast_data=forecast_data, city=city)

if __name__ == '__main__':
    app.run(debug=True)
