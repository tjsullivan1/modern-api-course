import requests

def main():
    choice = input("[R]eport weather or [s]ee reports?")
    while choice:
        if choice.lower().strip() == 'r':
            desc = input("What is happening now?")
            city = input("What city are you in?")
            state = input("What is your state?")
            report_event(desc, city, state)
        elif choice.lower().strip() == 's':
            see_events()
        else:
            print(f"I don't know what to do with {choice}")

        choice = input("[R]eport weather or [s]ee reports?")


def report_event(description: str, city: str, state: str):
    data = {
        "description": description,
        "location": {
            "city": city,
            "state": state
        }
    }

    url = "http://127.0.0.1:8000/api/reports"
    resp = requests.post(url, json=data)
    resp.raise_for_status()

    result = resp.json()

    print(f"Reported new event: {result}")


def see_events():
    url = "http://127.0.0.1:8000/api/reports"
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    for r in data:
        print(f"{r.get('location').get('city')} has {r.get('description')}")


if __name__ == '__main__':
    main()