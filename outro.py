import vlc
import os
import time
#link location in the gap below
p = vlc.MediaPlayer(r"       \outro.mp3")
shutdown = 10
p.play()
time.sleep(2.5)
for i in range(10):
    print("Shutting down in: ", shutdown)
    shutdown -= 1
    time.sleep(1)

time.sleep(0.5)
p.stop()
os.system("shutdown /s /t 0")


    
