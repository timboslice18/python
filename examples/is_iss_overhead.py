import requests
from datetime import datetime
import smtplib
import time


MY_EMAIL = "emailt@gmail.com"
MY_PASSWORD = "password_value"
MY_LAT = 40.440624
MY_LNG = -79.995888

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # #next line will show the exception that is returned
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #check if position is within +5 or -5 degrees of the iss position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # First split returns:
    # ['2022-10-22', '11:37:23+00:00']
    # Second Split returns
    # ['11', '37', '23+00', '00']
    # You can add this snippet to the sunrise and sunset vars to get just the hour
    # print(sunrise.split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

#use is_iss_overhead and is_night functions. If they both return True then it is nighttime and the
#iss is overhead. Send email if both are true
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg= "Subject:Look Up\n\nThe ISS is above you in the sky."
        )
