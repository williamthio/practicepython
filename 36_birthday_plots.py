import json
import calendar
from datetime import datetime
from collections import Counter
from bokeh.plotting import figure, show, output_file

def get_month_name(birthday):
    date = datetime.strptime(birthday, "%m/%d/%Y")
    return date.strftime("%B")

def load_birthdays():
    with open("scientist_birthdays.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    birthdays = load_birthdays()
    c = Counter([get_month_name(date) for date in birthdays.values()])

    x_range = calendar.month_name[1::]
    x = list(c.keys())
    y = list(c.values())

    output_file("plot.html")
    p = figure(x_range=x_range)
    p.vbar(x=x, top=y, width=0.5)
    show(p)
