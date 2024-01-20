import json
import turtle
import urllib.request 
import time 
import webbrowser 
import geocoder 
import requests
import datetime


# First API request and set up 
# fetching data from ISS

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt","w")
file.write("there are currently" + 
           str(result["number"]) + " astronauts on the iss: \n\n")
people = result["people"]

for p in people: 
    file.write(p['name'] + " - on board" + "\n")
# print longitude and latitude 
g = geocoder.ip('me')
file.write("\nYour current latitude and longitude is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# set up world map in turtle module

screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180,-90,180,90)

# load world map image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

# Next API, Astronomy picture of the day

api_key = 'ZWXN2DHNj5g4Ivn0nntSmUkJHdxLSr6TlVk8HqLJ'

api_url = 'https://api.nasa.gov/planetary/apod'

# parameters 


# Get the current date
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

params = {
    'api_key' : api_key,
     
    'hd' : 'True',
    
    'date' : current_date
}

response = requests.get(api_url,params = params)
json_data = json.loads(response.text)
image_url = json_data['url']
webbrowser.open(image_url)

while True: 
    #load current status of ISS in real time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read()) 
    # extract ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']
    
    #output to the terminal (latitude and longitude)
    
    lat = float(lat)
    lon = float(lon)
    
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))
    
    # update ISS location on the map
    iss.goto(lon,lat)
    
    # refresh each 5 seconds
    time.sleep(5)
