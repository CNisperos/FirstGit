from weatherapi.weatherapi_client import WeatherapiClient
import calendar
import time
import datetime
import jsonpickle

# Configuration parameters and credentials
key = 'af02d822128e4a6f92082633212712'
client = WeatherapiClient(key)
ap_is_controller = client.ap_is

q = "London"
lang = 'None'
result = ap_is_controller.get_realtime_weather(q, lang)
result2 = ap_is_controller.get_time_zone(q)
print(result,result2)
#jsonpickle.decode(result)

days = 1
dt = 'None'
unixdt = None
hour = 1
lang = 'lang'

result2 = ap_is_controller.get_forecast_weather(q, days, dt, unixdt, hour, lang)

