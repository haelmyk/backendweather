from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

# import json to deal with the connected API
# import urllib.request to help open the API url


def index(request):
    # ensuring the request from the form is available
    try:
        if request.method == 'POST':
            # getting the city input to the form into a variable that can later be displayed or used
            city = (request.POST['city']).title()
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=3240e390da8d3e43614a4c1418cdd775').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                "temp": int(json_data['main']['temp']) - 273,
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
                   }

        else:
            city = ''
            data = {}
        return render(request, 'index.html', {'city': city, 'data': data})
    except:
        Err_msg = 'City Not Found'
        return render(request, 'error.html', {'Err_msg': Err_msg})
