import os
import winwifi
import datetime
import socket
import time
import webbrowser
import subprocess

def is_connected():
    try:
        socket.create_connection(("1.1.1.1",53))
        return True
    except OSError:
        pass
    return False

def wifi_SSID(ssid):
    wifi = subprocess.check_output(['netsh','WLAN','show','interfaces'])
    data = wifi.decode('utf-8')

    if ssid in data:
        return True
    else:
        return False


if __name__ =='__main__':
    wifi1 = "Amal Jyothi"
    wifi2 = "Guest"
    url = "http://192.168.0.1:8090/"

    wifi = wifi1
    try:
        while(1):
            now = datetime.datetime.now()
            #print(now.strftime("%H:%M:%S"))

            if is_connected() == True:
                #print(now.strftime("%H:%M:%S"),"Online")
                pass
            else:
                print("---------------------------------------------------------------------------")
                print(now.strftime("%H:%M:%S"),"offline")
                print("Connecting to ",wifi)
                
                try:
                    winwifi.WinWiFi.connect(wifi)
                except:
                    print("could not connect to ",wifi)
                    if wifi == wifi1:
                        wifi = wifi2
                    else:
                        wifi = wifi1
                    #wifi = wifi2
                    print("Connecting to ",wifi)
                    
                    winwifi.WinWiFi.connect(wifi)
                    
               

                #if is_connected() == False and wifi_SSID(wifi) == True:
                 #   print("Connected to ",wifi," with No internet access")
                  #  print("Opening the portal")
                   # webbrowser.open(url,new=0)
                
                #if is_connected() == True:
                   # print("Connected Successfully to ",wifi1)
                print("---------------------------------------------------------------------------")

            #time.sleep(1)
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass
