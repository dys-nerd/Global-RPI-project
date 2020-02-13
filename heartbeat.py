#view output at https://docs.google.com/spreadsheets/d/1cWpe9ZPZQQpOZ9mMeV9KI0ZOWzzbxGj4_AowTcVN9pA/edit?usp=sharing

import requests
import time
import random

P1="""https://docs.google.com/forms/d/1vdrTC5PoVatlVjVCAMZcy8QrGbd6bDRTrxhDvS4YEGU/formResponse?entry.66599517="""
P2="""&entry.1801203113="""
P3="""&entry.654844405="""
P4="""&entry.500020622="""

r1=input("Name:")
r2=input("Location:")
r3=input("RPI Model:")
g1=str(random.randint(0000000000000000000000000, 9999999999999999999999999))
print("Running Press Ctrl+c to exit")
while True:
    r = requests.get(P1+r1+P2+r2+P3+r3+P4+g1)
    time.sleep(15*60)
