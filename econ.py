from pygame import mixer
import time
import random
import os

lst = ['Monopoly.mp3', 'Monopolistically Competitive Market With Ads.mp3', 'Monopolistically Competitive Market.mp3',
       'Natural Monopoly.mp3', 'Perfectly Competitive Market.mp3', 'The Good.mp3', 'The Bad.mp3', 'The Ugly.mp3']

lst2 = ['Monopoly.mp3', 'Monopolistically Competitive Market With Ads.mp3', 'Monopolistically Competitive Market.mp3',
        'Natural Monopoly.mp3', 'Perfectly Competitive Market.mp3', 'The Good.mp3', 'The Bad.mp3', 'The Ugly.mp3']

print("\nIt's econ time!")
print("Voielines will be yelled at 5-10 minute intervals, randomized")
print("Please contact Kai if you wish to add more voicelines")
print("~~~")
print(f"Current voicelines are as follows: {lst}")
print("~~~\n")
p = 0
inn = True

while inn:
    try:
        p = input("Input an initial delay: (in seconds, 300 = 5 mins) ")
        p = int(p)
        if p < 0:
            print("Whoops, please input a positive number")
        else:
            inn = False
    except Exception as e:
        print("Whoops, that's an invalid input. Try again.")

time.sleep(p)

while True:

    mixer.init()

    if len(lst2) == 0:
        print("~~~")
        print("list complete")
        print("~~~")
        lst2 = lst
        c = 'comedy.mp3'
    else:
        c = random.choice(lst2)

    print(c)

    try:
        lst2.remove(c)
    except Exception as e:
        pass

    current_path = os.path.dirname(__file__)

    mixer.music.load(os.path.join(current_path, c))

    mixer.music.set_volume(100)

    mixer.music.play()

    t = random.randint(300, 600)

    print(f"{t} seconds ({t/60} minutes)")

    time.sleep(t)

# pyinstaller --add-data "*.mp3;." --onefile econ.py
