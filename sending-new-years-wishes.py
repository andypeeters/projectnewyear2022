from datetime import datetime, timezone, timedelta
import time

def send_all_wishes():
    wishes_file = open("new-years-wishes.txt", "r")
    wish_line = wishes_file.readline()
    while len(wish_line) > 0:
        process_wish_line(wish_line)
        wish_line = wishes_file.readline()
    wishes_file.close()

def process_wish_line(wish_line):
    definedtime,wish = wish_line.split(";")
    timestamp = datetime.fromisoformat(definedtime)
    wait_period(timestamp)
    print("Wishes: ", wish)

def wait_period(timestamp):
    currenttime = datetime.now(timezone(timedelta(hours=1)))
    timediff = timestamp - currenttime
    print("current time:", currenttime, ", timediff: ", timediff.total_seconds())
    if timediff.total_seconds() > 0.0:
        print("waiting ", timediff.total_seconds(), " seconds...")
        time.sleep(timediff.total_seconds())

# Main program starts here.
if __name__ == '__main__':
    send_all_wishes()
    print("All wishes are tweeted!")
