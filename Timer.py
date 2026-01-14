
import time
""" Timer Class """
class Timer:

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise Exception("Timer was not started.")
        elapsed_time = time.time() - self.start_time
        self.start_time = None
        return elapsed_time
    
