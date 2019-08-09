import time
import ttn
import json

TTN_APP_ID = "emca"
TTN_ACCESS_KEY = "ttn-account-v2.Ebyo38DrTI5dynOb28aw0ExjDLYZGGsr4D6yanc9jcs"

sensor_data = {'Temperature': 0,'Humidity': 0,'Pressure': 0,'CO': 0,'O3': 0,'SO2': 0,'NO2': 0,'PM1': 0,'PM10': 0,'PM25': 0}

def uplink_callback(msg, client):
    sensor_data['Temperature']  = msg.payload_fields.Temperature
    sensor_data['Humidity']     = msg.payload_fields.Humidity
    sensor_data['Pressure']     = msg.payload_fields.Pressure
    sensor_data['CO']           = msg.payload_fields.CO
    sensor_data['O3']           = msg.payload_fields.O3
    sensor_data['SO2']          = msg.payload_fields.SO2
    sensor_data['NO2']          = msg.payload_fields.NO2
    sensor_data['PM1']          = msg.payload_fields.PM1
    sensor_data['PM10']         = msg.payload_fields.PM10
    sensor_data['PM25']         = msg.payload_fields.PM25

handler = ttn.HandlerClient(TTN_APP_ID, TTN_ACCESS_KEY)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    pass

mqtt_client.close()
