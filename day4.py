import requests

# Replace with your OpenWeatherMap API Key
API_KEY = "YOUR_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=10)

        # Raise exception for HTTP errors
        response.raise_for_status()

        data = response.json()

        if data["cod"] != 200:
            print(f"\nError: {data['message'].capitalize()}")
            return

        print("\n========== Weather Report ==========")
        print("City         :", data["name"])
        print("Country      :", data["sys"]["country"])
        print("Temperature  :", data["main"]["temp"], "°C")
        print("Humidity     :", data["main"]["humidity"], "%")
        print("Condition    :", data["weather"][0]["description"].title())
        print("Wind Speed   :", data["wind"]["speed"], "m/s")
        print("====================================")

    except requests.exceptions.HTTPError:
        print("\nError: Invalid city name or server error.")

    except requests.exceptions.ConnectionError:
        print("\nError: No internet connection.")

    except requests.exceptions.Timeout:
        print("\nError: Request timed out.")

    except requests.exceptions.RequestException as e:
        print("\nRequest Error:", e)

    except KeyError:
        print("\nError: Unexpected response from the API.")

    except Exception as e:
        print("\nUnexpected Error:", e)


def main():
    print("====== Weather CLI Application ======")

    while True:
        city = input("\nEnter City Name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("Thank you!")
            break

        if city == "":
            print("City name cannot be empty.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
