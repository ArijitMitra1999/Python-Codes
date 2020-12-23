import time

initital= time.time()
i=0
while i<=45 :
    time.sleep(1) #Kind of a threed.sleep
    print("Arijit is a good boy",time.time()-initital,"Seconds")
    i+= 1

initital2 = time.time()
for i in range(45) :
    print("Arijit is a good boy",time.time()-initital2,"Seconds" )