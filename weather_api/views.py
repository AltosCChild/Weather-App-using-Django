from django.shortcuts import render
import requests

# Create your views here.
def weather(request):
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city')

        if not city:
            error_message = 'Please enter a city name'
        else:
            api_url = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
            url = api_url + city
            response = requests.get(url)
            content = response.json()
            
            if city == 'Dragon ball'.lower() :
                error_message = "Best Anime in the history 😎"
            elif city == 'ONE PIECE'.lower() :
                error_message = "Sanji aswa2 chakhsiya 👍"    
               
            elif content.get('cod') == '404':
                error_message = 'Please enter a valid city name'   
            else:
                city_weather = {
                    'City': city,
                    'Temperature': round(content['main']['temp']-273.15, 2),
                    'Description': content['weather'][0]['description'],
                    'Icon': content['weather'][0]['icon']
                }
                return render(request, 'weather_api/weather.html', {'city_weather': city_weather})

    return render(request, 'weather_api/weather.html', {'error_message': error_message})

    
