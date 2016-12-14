import pyowm

owm = pyowm.OWM("69bbca9d1eab20bbc6e314c78c28d893")
obs= owm.weather_at_place('Rostov-on-Don,ru')
weather = obs.get_weather()
location = obs.get_location()
strana = location.get_country()
oblaka = weather.get_clouds()
vet = weather.get_wind()['deg']
fc = owm.daily_forecast('Rostov-on-Don,ru')
rain = fc.will_have_rain()

translate = {'Rostov-na-Donu' : 'Ростов-на-Дону'}

def obl() :
    if 0 <= oblaka <= 10:
        return 'ясная'

    if 10 < oblaka <= 50:
        return 'облачная'

    if 50 < oblaka <= 100:
        return 'пасмурная'
def deg():
    if 0 <= vet < 90:
        return 'северо-восточный'
    if vet == 90:
        return  'восточный'
    if 91 <= vet < 180:
        return 'юго-восточный'
    if vet == 180:
        return 'южный'
    if 181 <= vet < 270:
        return 'юго-западный'
    if vet == 270:
        return 'западный'
    if 271 <= vet < 360:
        return ('северо-западный')
    if vet == 360:
        return  'северный'
def rainn():
    if rain == 0:
        return "Осадков не ожидается"
    if rain == 1:
        return 'Ожидаются осадки'
print('Погода в городе ', translate[location.get_name()], ' на ', obs.get_reception_time(timeformat='iso'))
print('Ожидается ' +obl(), 'погода. Ветер ' + deg(), 'со скоростью = ' + str(weather.get_wind()['speed']), 'м/с')
print(rainn(), 'Температура составляет ' + str(weather.get_temperature('celsius')['temp']), 'градусов по цельсию.')


