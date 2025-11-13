from datetime import datetime, timedelta
import requests
from waveshare_epd import epd7in5_V2 # this was for this specific screen. Adjust for your own screen
from PIL import Image, ImageDraw, ImageFont
import traceback
import time

# make sure that the code is saved and executed from the right file location.
# it must have the file waveshare_epd and you chosen font in the same directory (fonts explained bellow)

epd = epd7in5_V2.EPD() # this is for the waveshare 7.5inch screen that I used
#this line of code can be found in the e ink screen documentation

# Get current time
now = datetime.now()

# Start from the current hour (dropping minutes & seconds)
start_hour = now.replace(minute=0, second=0, microsecond=0)


epd.width = 800 # " - - - " you have to find out your width and height of the screen you are using
epd.height = 400 # " - - - " Mine was 800 and 400

# for the api call you need an api key as discussed before. You must also use your longitude and latitude and put it in the url
url = "https://api.openweathermap.org/data/3.0/onecall?lat= &lon= &exclude=minutely,alerts&units=metric&appid= ENTER YOUR API KEY "
response = requests.get(url)
temp = [0] * 10
rain = [0] * 10
wind = [0] * 10
times = [""] * 10


while True:
    print("Going again") # just so I know when the code is looping
    try:
        now = datetime.now()
        response = requests.get(url)
        # Start from the current hour (dropping minutes & seconds)
        start_hour = now.replace(minute=0, second=0, microsecond=0)
        epd.init()
        Make_image = Image.new('1', (epd.width, epd.height), 255)
        draw = ImageDraw.Draw(Make_image)

        # IMPORTANT FOR THIS TO WORK, you also need a font file. You can find many font files on github. Download a font file for the e ink screen
        # and make sure that it is in the same directory as this code

        font  = ImageFont.truetype("avenir-next-medium.ttf",35) # use the name of the font file
        font2  = ImageFont.truetype("avenir-next-medium.ttf",100)
        font3  = ImageFont.truetype("avenir-next-medium.ttf",35)
        font4 = ImageFont.truetype("avenir-next-medium.ttf",25)
        for i in range(10):  # 0 for current hour + 10 more hours
            next_hour = start_hour + timedelta(hours=i)
            times[i] = next_hour.strftime("%H:00")
            print(times[i])
        if response.status_code == 200:
            data = response.json()
            i = 0
            # Next 10 hour temperatures
            if "current" in data:
                print("Weather description for today")
                description = data["current"]["weather"][0]["description"]
                print(description.capitalize())
            if "hourly" in data:
                print("Temperatures for the next 12 hours:")
                for hour in data["hourly"][:10]:
                    temp[i] = hour["temp"]
                    rain[i] = hour["pop"]
                    rain[i] = rain[i] * 100
                    wind[i] = round(hour["wind_speed"] * 2.2369362920544, 1) # converting from m/s to mph
                    i = i+1
                for i in range(len(temp)):
                    print(f"{temp[i]} C --- {rain[i]}% --- {wind[i]}mph")
            else:
                print("No hourly data available.")

            # Tomorrow's min/max
            if "daily" in data and len(data["daily"]) > 1:
                tomorrow = data["daily"][1]
                min_temp = tomorrow["temp"]["min"]
                max_temp = tomorrow["temp"]["max"]
                print("\nTomorrow's forecast:")
                print(f"Min: {min_temp:.1f}°C, Max: {max_temp:.1f}°C")
            else:
                print("Daily forecast data unavailable.")

        else:
            print("API call failed:", response.status_code, response.text)


        # Make the image
        draw.text((30,30),f"{round(temp[0],1)} °C",font=font2,fill=0)
        draw.text((420,45),f"{round(rain[0])}%",font=font3,fill=0)
        draw.text((420,95),f"{round(wind[0],1)}",font=font3,fill=0)
        draw.text((520,50),f"{description}",font=font,fill=0)
        i = 1
        x = 0
        while i < 9:
            draw.text((((x*100)+28),200),f"{times[i]}",font=font4,fill=0)
            draw.text((((x*100)+30),250),f"{round(temp[i],1)}",font=font3,fill=0)
            draw.text((((x*100)+30),312),f"{round(rain[i])}%",font=font3,fill=0)
            draw.text((((x*100)+30),375),f"{round(wind[i],1)}",font=font3,fill=0)
            i = i + 1
            x = x + 1
        epd.display(epd.getbuffer(Make_image))
        epd.sleep()
        time.sleep(600)

    except Exception as e:
        print("###############################NOT WORKING ######################################")
        traceback.print_exc()
        # the except is to ensure that if any errors come, the program will still run.

        # this is useful for running for long sessions
