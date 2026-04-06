#LIB
import time                                                
import requests
import os
#SCRIPT
os.system("clear")
print("\033[31m ▀████▀███▀▀▀██▄  ▄▄█▀▀▀█▄█▀███▀▀▀███  ▄▄█▀▀██▄ ")  
time.sleep(0.8)
print("\033[31m   ██   ██   ▀██▄██▀     ▀█  ██    ▀█▄██▀    ▀██▄")
time.sleep(0.8)
print("\033[31m   ██   ██   ▄████▀       ▀  ██   █  ██▀      ▀██")
time.sleep(0.8)
print("\033[31m   ██   ███████ ██           ██████  ██        ██")
time.sleep(1.0)
print("\033[31m   ██   ██      ██▄    ▀████ ██   █  ▄█▄      ▄██")
time.sleep(0.8)
print("\033[31m   ██   ██      ▀██▄     ██  ██     ▄███▄    ▄██▀")
time.sleep(0.8)
print("\033[31m ▄████▄████▄      ▀▀███████▄██████████ ▀▀████▀▀  ")           
ip = input("Enter Your ip: ")
geo = requests.get(f"http://ip-api.com/json/{ip}").json()
with open("info.txt", "w", encoding="utf-8") as lock:
    lock.write(f"Country: {geo['country']}\n")
    lock.write(f"Lat: {geo['lat']}\n")
    lock.write(f"lon is {geo['lon']}\n")
    lock.write(f"city is: {geo['city']}\n")
    lock.write(f"org: {geo['org']}")
print(f"Country is: {geo['country']}")
print(f"city is: {geo['city']}")
print(f"lat is: {geo['lat']}")
print(f"lon is: {geo['lon']}")
print(f"org is : {geo['org']}")