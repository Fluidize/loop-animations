import sys,time
from typing import Any
from termcolor import colored

class progress_bar():
    def __init__(self, stop, start=0):
        self.count = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.count == self.stop:
            print('')
            raise StopIteration
        
        elif self.count != self.stop:
            self.count += 1
            percentage = '〙' + str(round(self.count * 100/self.stop, 2)) + '%'
            if round(self.count * 100/self.stop, 2) == 100:
                percentage = colored(percentage, 'green')
            bar = colored('〘','green') + colored('█','green')*self.count + "-" * (self.stop-self.count)
            sys.stdout.write(f"{bar}{percentage} \r")
            sys.stdout.flush()
            return self.count

class animation():
    def __init__(self, stop, start=0):
        self.count = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.count == self.stop:
            print('')
            raise StopIteration
        
        elif self.count != self.stop:
            self.count += 1
            anim=r'-\|/'
            sys.stdout.write('[%s]\r' % (anim[self.count % 4]))
            sys.stdout.flush()
            return self.count
    
for x in progress_bar(50):
    time.sleep(0.1)