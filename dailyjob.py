import schedule
import time

def job():
    print("I'm working...")
    return

schedule.every().day.at("20:47").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)