import schedule
import time
import requests

def job():
    print("Time to make a call to port 3005")
    requests.get("http://localhost:3005")

    return

schedule.every().monday.at("20:30").do(job)
schedule.every().tuesday.at("20:30").do(job)
schedule.every().wednesday.at("20:30").do(job)
schedule.every().thursday.at("20:30").do(job)
schedule.every().friday.at("20:30").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
