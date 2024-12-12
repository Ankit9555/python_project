import requests

def fetch_api():

    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

    querystring = {"lat":"35.5","lon":"-78.5","units":"imperial","lang":"en"}

    headers = {
	"x-rapidapi-key": "e5bb2e52b6mshaa1a98c0a8a370ep156f09jsn3346c5db4616",
	"x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    
    if data["country_code"] == "US" and "data" in data:
        for i in range(40):
            date_time = data["data"][i]["datetime"]
            temp = data["data"][i]["temp"]
            win_dir = data["data"][i]["wind_cdir_full"]
            s_rad = data["data"][i]["solar_rad"]
            wind_speed = data["data"][i]["wind_spd"]
            print("*" * 40)
            print(f"\nToday date and time:- {date_time}")
            print(f"Temperature:- {temp}")
            print(f"Wind direction:- {win_dir}")
            print(f"Wind Speed:- {wind_speed}")
            print(f"Solar radiation:- {s_rad}")
            print("*" * 40)
    else:
        raise Exception("fail to fetch your Api data")

def main():
    fetch_api()
    
if __name__ == "__main__":
    main()
