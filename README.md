# AutoHome
## Inspiration
We invest a lot of time and money making our homes work for us. Right from buying the house and buying smart appliances that save power and give you more control over the way you want your house to be setup to be comfortable for you, there's a large cost and involvement required. You lose a lot of time doing simple tasks such as adjusting the lights or adjusting the temperature in the house. These everyday tasks have a lot of scope for automation. Our project AutoHome presents a smart home solution that works for you by automating these everyday tasks. AutoHome is more a cost-effective, more efficient solution to operate all the devices at a home, monitor and control them remotely and securely.

## What it does
The AutoHome is a powered by a Raspberry Pi, which serves as a platform to connect various sensors to detect various aspects of the house such as light levels, CO levels, cooking gas levels, temperature and humidity, and controls these devices using a relay. When a user signs up for the service on our website, then enter a device identifier to identify the Pi they've connected to our service, which enables communication between the RasPi and the Firebase Realtime Database. The temperature, light levels and humidity data are fed to the Realtime Database to display to the user in real time. The user sets their temperature and humidity preferences in the web app, and the Pi checks with the database to accordingly use the AC/Heater/Humidifier/Lights to make the environment optimal for the user. 

## How we built it
The Smart Home device is built with a Raspberry Pi that is connected to a MQ9 cooking gas sensor, MQ7 carbon monoxide sensor, TCS34725 light sensor, DHT11 temperature/humidity sensor and two relays. The data from the TCS34725 and the DHT11 is pushed to the Firebase Realtime database which stores all the information. The user interacts with a chatbot built using Twilio and Google Dialogflow. When the user asks about a particular place, we leverage the capability of the Shine API(by Liberty Mutual) and give the user information about the safety of the place.         

## Challenges we ran into
We ran into various challenges throughout the course of the project. Getting all the hardware to work to gather with interrupts and timing all the loops to ensure nothing crashes was a lot of work. Integrating Twilio, Dialogflow and Firebase was quite difficult and taxing. Even at the end of the Hackathon, we were unable to get the Dialogflow Cloud Functions to work.

## Accomplishments that we're proud of
We are proud to get all the hardware to work together to get the values from all the sensors. Further, working with Twilio and implementing a chatbot was awesome to achieve. 

## What we learned
We learned a lot from this project. Integrating all the hardware and using them effectively using Python, using technologies such as Twilio, Firebase Firestore, and Dialogflow.

## What's next for AutoHome
We feel that AutoHome has large scale applications for a lot of people and belongs in a lot of homes. We would like to conduct testing of this device in a home and collect user feedback and look at ways to allow the user to interact with in various ways, and to integrate more technologies.

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```
