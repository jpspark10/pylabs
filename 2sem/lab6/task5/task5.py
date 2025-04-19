import schedule
import time
from datetime import datetime


def greet():
    hour = datetime.now().hour % 12
    hour = 12 if hour == 0 else hour
    print("Ку" * hour)


def main():
    print("Запуск планировщика")
    schedule.every().hour.at(":00").do(greet)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
