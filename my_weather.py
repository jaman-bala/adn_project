from pyowm import OWM
import datetime


owm = OWM("166dc9f8a386105b21687e8f50bad441")
mgr = owm.weather_manager()
language = "ru"



def get_weather(city):

    observation = mgr.weather_at_place(city)
    w = observation.weather
    data = w.temperature('celsius')
    time = datetime.datetime.now()



    if data['temp'] < 10:
        advice = "Сейчас очень холодно, одевайтесь по теплее! "
    elif data['temp'] < 15:
        advice = "На улице холодно, можете одется легко! "
    else:
        advice="на улице тепло"
    temperatur = data['temp']
    text = f"Температура:{temperatur}\n Время: {time}\n Совет: {advice}"
    return text
