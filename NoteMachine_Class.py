from win10toast import ToastNotifier
import schedule
import time
import threading
import pickle




class Note():
    def __init__(self, tim, notes, message):
        self.notes = notes
        self.time = tim
        self.msg = message

        toast = ToastNotifier()
        hello = lambda: toast.show_toast(self.notes, self.msg, duration=7)

        self.wakeup = schedule.every().day.at(self.time).do(hello)


    def task_cancel(self):
        schedule.cancel_job(self.wakeup)

    def __getstate__(self) -> dict:
        state = {}
        state["msg"] = self.msg
        state["notes"] = self.notes
        state["time"] = self.time
        return state

    def __setstate__(self, state: dict):
        self.msg = state["msg"]
        self.notes = state["notes"]
        self.time = state["time"]

        toast = ToastNotifier()
        hello = lambda: toast.show_toast(self.notes, self.msg, duration=7)
        self.wakeup = schedule.every().day.at(self.time).do(hello)


def schedule_runner():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=schedule_runner, daemon=True).start()


tasks = {}

