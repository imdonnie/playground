import time
from progressbar import *

total = 1000

def doSomeWork():
    time.sleep(0.01)

widgets = ['Progress', Percentage(), ' ', Bar('#'), ' ', Timer(), ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=10*total).start()
for i in range(total):
    pbar.update(10 * i + 1)
    doSomeWork()
pbar.finish()
