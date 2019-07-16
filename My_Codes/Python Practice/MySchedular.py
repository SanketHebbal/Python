import schedule
import datetime
import time


def motivate():
    print("Sanket keeping coding...")
    print(datetime.datetime.now())
    
def main():

    schedule.every(0.1).minutes.do(motivate)

    while True:
        schedule.run_pending()
    
if __name__ == "__main__":
    main()
