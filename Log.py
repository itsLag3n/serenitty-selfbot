from utils import *

class Log():
    def __init__(self):
        self.co = co()

    def info(self, message, end="\n", flush=False):
        print(f"{GREY}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | [  {self.co}INFO{W}  ] | {message}", end=end, flush=flush)

    def warn(self, message, end="\n", flush=False):
        print(f"{GREY}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | [  {R}WARN{W}  ] | {message}", end=end, flush=flush)
    
    def err(self, message, end="\n", flush=False):
        print(f"{GREY}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | [  {R}ERROR{W} ] | {message}", end=end, flush=flush)
    
    def dbg(self, message, end="\n", flush=False):
        print(f"{GREY}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | [  {self.co}DEBUG{W} ] | {message}", end=end, flush=flush)



class SleepLog():
    def __init__(self, time=3):
        self.co = co()
        self.time = time

    def info(self, message, end="\n", flush=False):
        print(f"{GREY}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | [  {self.co}INFO{W}  ] | {message}", end=end, flush=flush)
        time.sleep(self.time)

    def warn(self, message, end="\n", flush=False):
        print(f"{GREY}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | [  {R}WARN{W}  ] | {message}", end=end, flush=flush)
        time.sleep(self.time)
    
    def err(self, message, end="\n", flush=False):
        print(f"{GREY}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | [  {R}ERROR{W} ] | {message}", end=end, flush=flush)
        time.sleep(self.time)
    
    def dbg(self, message, end="\n", flush=False):
        print(f"{GREY}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | [  {self.co}DEBUG{W} ] | {message}", end=end, flush=flush)
        time.sleep(self.time)