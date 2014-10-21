import time
import datetime

class SpeedBenchmark():

    time_start = None
    time_end = None
    time_total = None

    def start_benchmark(self):
        self.time_start = time.time()

    def stop_benchmark(self):
        self.time_end = time.time()
        self.time_total = self.time_end - self.time_start

    def get_benchmark(self):
        secs = self.time_total
        return str(datetime.timedelta(seconds=secs))