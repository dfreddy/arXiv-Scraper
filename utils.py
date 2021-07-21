import os
import time
import json
from datetime import date
from datetime import timedelta
from tkinter import *
from tkinter.ttk import *
import threading

config = json.load(open('./config.json', 'r'))
base_dir = config['directory']
yesterday = date.today() - timedelta(days = 1)

'''
    checks if the directory for yesterday exists     
'''
def checkYesterdaysDir():
    day = yesterday.strftime('/%Y/%B/19')
    date_dir = base_dir + day
    if not os.path.exists(date_dir):
        os.makedirs(date_dir)
    
    return date_dir

'''
    checks if the paper is from yesterday
'''
def isPaperFromYesterday(paper_date):
    day = yesterday.strftime('%Y-%m-19')
    if day in paper_date:
        return True
    return False

'''
# loading bar
def startLoadingBar():
    root = Tk()
    root.title('Fetching papers...')
    root.minsize(300,25)
    progress=Progressbar(root,orient=HORIZONTAL,length=300,mode='indeterminate')
    progress.pack(pady = 10)
    def bar():
        progress.grid(row=1,column=0)
        progress.start()
    
    def quit():
        root.destroy()

    # This button will initialize
    # the progress bar
    threading.Thread(target=bar).start()
    time.sleep(3)
    threading.Thread(target=quit).start()
    root.mainloop()
    return root
'''

def activateFinished():
    root = Tk()
    root.title('arXiv Papers')
    root.geometry('300x50')
    l = Label(root, text = "Finished fetching papers")
    l.config(font =("Courier", 14))
    l.pack()
    root.mainloop()