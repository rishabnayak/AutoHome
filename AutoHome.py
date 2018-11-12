import time, io, sys, smbus, Adafruit_TCS34725, Adafruit_DHT, firebase_admin, os
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from os import system
from twilio.rest import Client
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
cred = credentials.Certificate("/home/pi/Downloads/autohome-hoe-firebase-adminsdk-8b6uu-562f94bade.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
tcs = Adafruit_TCS34725.TCS34725()
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.output(18,0)
GPIO.output(17,0)

def getserial():
    cpuserial = '0000000000000000'
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=="Serial":
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = 'ERROR000000000'
    return cpuserial

account_sid = 'AC6acdb2a4ea804b400fcea7e220f6802d'
auth_token = '6286a0062217e5a3389802976b978d15'
client = Client(account_sid, auth_token)
serial = getserial()
dataref =  db.collection(u'users').where(u'serial', u'==', serial)
data = dataref.get()
getdata = next(data)
uid = getdata.get('uid')
econtact = getdata.get('econtact')

def readLight():
    #18 is for lights turn on
    light = tcs.get_raw_data()[3]
    if(light < 7):
        GPIO.output(17, 1)
    else:
        GPIO.output(17, 0)
        
        
def readHumidity():
    humidity = Adafruit_DHT.read_retry(11,4)[0]
    hum = {u'humidity': humidity}
    db.collection(u'users').document(uid).set(hum, merge=True)
    dataref =  db.collection(u'users').document(uid)
    data = dataref.get()
    humidityPreference = data.get('userHumidity')
    print("Humidity: " + '%.1f' % humidity + "%")

def readTemp():
    
    temperature = Adafruit_DHT.read_retry(11,4)[1]
    temp = {u'temperature': temperature}
    db.collection(u'users').document(uid).set(temp, merge=True)
    dataref =  db.collection(u'users').document(uid)
    data = dataref.get()
    temperaturePreference = data.get('userTemp')
    print("Temperature: " + '%.1f' % temperature + " C")
    #18 air conditioner , 17 heater
    humidity = Adafruit_DHT.read_retry(11,4)[0]
    if(humidity < 100):
        if(temperature < float(temperaturePreference)):
           #turn on heater
            GPIO.output(18, 1)
        else:
           #turn on ac
            GPIO.output(18, 0)
        
       
    
        

def COAlert(pin):
    message = client.messages \
        .create(
            body="Warning from your Home: high levels of CO present!",
            from_='+13396746836',
            to= econtact
             )
    return
    
def GasAlert(pin):
    message = client.messages \
        .create(
            body="Warning from your Home: high levels of flammable gas present!",
            from_='+13396746836',
            to= econtact
             )
    return

GPIO.add_event_detect(15, GPIO.RISING, callback=COAlert, bouncetime=10000)
GPIO.add_event_detect(14, GPIO.RISING, callback=GasAlert, bouncetime=10000)

try:    
    while True:
        readLight()
        readHumidity()
        readTemp()
        time.sleep(2)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()