import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=" + API_KEY


def get_weather(date):
    response = requests.get(BASE_URL)
    data = response.json()
    for item in data["list"]:
        if date in item["dt_txt"]:
            print(f"Temperature on {item['dt_txt']}: {item['main']['temp']} °C")
            break
    else:
        print("Data not found for the given date.")


def get_wind_speed(date):
    response = requests.get(BASE_URL)
    data = response.json()
    for item in data["list"]:
        if date in item["dt_txt"]:
            print(f"Wind Speed on {item['dt_txt']}: {item['wind']['speed']} m/s")
            break
    else:
        print("Data not found for the given date.")


def get_pressure(date):
    response = requests.get(BASE_URL)
    data = response.json()
    for item in data["list"]:
        if date in item["dt_txt"]:
            print(f"Pressure on {item['dt_txt']}: {item['main']['pressure']} hPa")
            break
    else:
        print("Data not found for the given date.")


def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            get_weather(date)
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            get_wind_speed(date)
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            get_pressure(date)
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
