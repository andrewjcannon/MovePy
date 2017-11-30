import shutil
import os
import configparser
from time import sleep
from datetime import datetime

def worker_function():
    print("running")
    #Program will loop if set true in config.ini
    loop = True
    while loop is True:
        #try-catch for fatal errors
        try:
            #initalize configparser and read config.ini
            config = configparser.ConfigParser()
            config.read("config.ini")
            settings = config['CONFIGURATION']
            rules = config['RULES']
            status = config['STATUS']

            if status['status'] == "off":
                continue
            
            #if loop false, run once
            #if loop true, continue to run until set false
            if 'loop' in settings:
                loop = settings['loop']
                if(loop == "True" or loop == "true"):
                    loop = True
                else:
                    loop = False
            else:
                loop = False

            #format filepaths from config.ini
            if 'base_path' in settings:
                basepath = settings['base_path'] + "/"
            else:
                basepath = ""
                
            originalpath = settings['search_path']
            if(originalpath == ""):
                originalpath = ""
            else:
                originalpath = originalpath + "/"

            #loop over files in search directory
            for filename in os.listdir(basepath + originalpath):
                name, file_extension = os.path.splitext(basepath + originalpath + filename)     #split extension from filename
                #if file has rules, move it to its respective folder
                if file_extension in rules:
                    try:
                        shutil.move(basepath + originalpath + filename, basepath + rules[file_extension])
                    except Exception as e:
                        #catch any errors and output to log
                        logname = "log.txt"
                        if os.path.exists(logname):
                            file = open(logname, 'a')
                            file.write(str(datetime.now()) + " ----> " + str(e) + "\n")
                            file.close()

            #if looping, delay for user-set time between each execution
            if(loop is True):
                delay = float(settings["delay"])
                sleep(delay)

        #catch any fatal errors and output to log.txt
        except Exception as e:
            logname = "log.txt"
            if os.path.exists(logname):
                file = open(logname, 'a')
                file.write(str(datetime.now()) + " ----> FATAL " + str(e) + "\n")
                file.close()
            print(e)
            break
                    



