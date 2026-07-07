import schedule
import time


class Scheduler:

    def every_hour(self,func):

        schedule.every().hour.do(func)

    def run(self):

        while True:

            schedule.run_pending()

            time.sleep(1)