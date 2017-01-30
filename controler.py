import os
import time as tm
from DataFetcher import *
import subprocess as s







def run():
    log_ping()
    os.startfile('g.py')
    tm.sleep(20)
  # os.popen('g.py')
    while True:
        #log_ping()
        tm.sleep(18)
        a_ping = check_ping()
        last_ping = a_ping[0]
        print int(a_ping[1])
        pid = int(a_ping[1])
        print " Last ping at " + str(last_ping)
        if last_ping > 400.0:
            #last_ping = check_ping()
            killProcess(pid)
            print " File terminated"
            os.startfile('g.py')
            print " File restarted"


def killProcess(pid):
    s.Popen('taskkill /F /PID {0}'.format(pid), shell=True)


def log_ping():
    """Logs all the data in a text file for each individual"""
    file_name = "ping1.txt"
    ping = basic_data()
    pid = os.getpid()
    print pid
    text_file = open(file_name, "w")
    text_file.write(str(ping.start_time))
    text_file.write('\n')
    text_file.write(str(pid))
    text_file.close()
    #print ping.start_time


def check_ping():
    """Logs all the data in a text file for each individual"""
    file_name = "ping1.txt"
    text_file = open(file_name, "r")
    ping1 = text_file.readlines()
    a_ping = float(ping1[0])
    pid = ping1[1]
    text_file.close()
    ping = basic_data()
    ping.start_time = a_ping
    ping.stop_timer()
    #print ping.duration
    return  [ping.duration, pid]

run()
