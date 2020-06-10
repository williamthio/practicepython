import json
from datetime import datetime
from collections import Counter

def get_month_name(birthday):
    date = datetime.strptime(birthday, "%m/%d/%Y")
    return date.strftime("%B")

def load_birthdays():
    with open("birthdays.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    birthdays = load_birthdays()
    c = Counter([get_month_name(date) for date in birthdays.values()])
    print(c)
