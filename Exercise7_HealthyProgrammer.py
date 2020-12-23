# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyeDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
import time
def getdate():
    import datetime
    return datetime.datetime.now()

print("Here Your todays time start")

def Water() :
    print("This is your time to Drink Water")

    mixer.init()

    mixer.music.load("D:\Python\Virtual Environment\Water.mp3")

    mixer.music.set_volume(0.7)

    mixer.music.play()
    while True:
        print("Press 'Drank' to exit the Reminder")
        user = input(" ")
        with open("Water.txt",'a') as water:
            water.write(str(str(getdate())) + ":" + user +"\n")
        if user == "Drank".casefold():
            mixer.music.stop()
            break
        elif user == "Drank" :
            mixer.music.stop()
            break
        else:
            mixer.music.unpause()
    print("Okay now time count for eye rest")

def Eyes() :
    print("This is your time to rest your Eyes")
    mixer.init()

    mixer.music.load("D:\Python\Virtual Environment\EyeRest.mp3")

    mixer.music.set_volume(0.7)

    mixer.music.play()
    while True:
        print("Press 'EyeDone' to exit the Reminder")
        user = input(" ")
        with open("Eyes.txt",'a') as water:
            water.write(str(str(getdate())) + ":" + user+"\n")
        if user == "EyeDone".casefold():
            mixer.music.stop()
            break
        elif user == "EyeDone" :
            mixer.music.stop()
            break
        else:
            mixer.music.unpause()
    print("Now time count for Gym")

def Gym() :
    print("This is your time for Gym")
    mixer.init()

    mixer.music.load("D:\Python\Virtual Environment\Gym.mp3")

    mixer.music.set_volume(0.7)

    mixer.music.play()
    while True:
        print("Press 'GymDone' to exit the Reminder")
        user = input(" ")
        with open("Gym.txt",'a') as water:
            water.write(str(str(getdate())) + ":" + user+"\n")
        if user == "GymDone".casefold():
            mixer.music.stop()
            break
        elif user == "GymDone" :
            mixer.music.stop()
            break
        else:
            mixer.music.unpause()

if __name__ == '__main__':
    
    Water()
    time.sleep(2)
    Eyes()
    time.sleep(3)
    Gym()

