#Import important stuff
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

#Main page
@app.route("/") #"/" is the default page
def main():
    #creates list items for each different page
    return """
    <h1>Home Page</h1>
    <ul>
        <li><a href="/date">Date</a></li>
        <li><a href="/time">Time</a></li>
        <li><a href="/ampm">AM/PM</a></li>
    </ul>
    """

#Date page
@app.route("/date")
def date():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    return f"""
    <h2>Current Date</h2>
    <p>{current_date}</p>
    <p><a href="/">Back to Main</a></p>
    <p><a href="/time">Time</a></p>
    <p><a href="/ampm">AM/PM</a></p>
    """
    def test_date(self):
        self.assertEqual(now, now.strftime("%Y-%m-%d"))

#Time page
@app.route("/time")
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"""
    <h2>Current Time</h2>
    <p>{current_time}</p>
    <p><a href="/">Back to Main</a></p>
    <p><a href="/date">Date</a></p>
    <p><a href="/ampm">AM/PM</a></p>
    """
    def test_time(self):
        self.assertEqual(now, now.strftime("%H:%M:%S"))

#ampm page
@app.route("/ampm")
def ampm():
    now = datetime.now()
    am_pm = "AM" if now.hour < 12 else "PM"
    return f"""
    <h2>AM/PM</h2>
    <p>{am_pm}</p>
    <p><a href="/">Back to Main</a></p>
    <p><a href="/date">Date</a></p>
    <p><a href="/time">Time</a></p>
    """
    def test_ampm(self):
        self.assertEqual(now, "AM" if now.hour < 12 else "PM")

if __name__ == "__main__":
    app.run()