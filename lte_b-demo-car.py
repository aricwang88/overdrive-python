from overdrive import Overdrive
import os,sys,time

#track_set

track_sets = set([])
track_lst = []
track_id = 17 

def locationChangeCallback(addr, location, piece, speed, clockwise):
    # Print out addr, piece ID, location ID of the vehicle, this print everytime when location changed
    print("Location from " + addr + " : " + "Piece=" + str(piece) + " Location=" + str(location) + " Speed=" + str(speed) +" Clockwise=" + str(clockwise))
    #track_sets.add(str(piece))
    #track_lst.append(str(piece))
    #print("TRACK:"+str(track_lst))
#    if piece == track_id:
#        car.changeSpeed(0,15000) 
    if addr == "F5:64:F7:27:C4:70" and speed > 508:
         print("######################   Car cash detected!") 
    pass

def pongCallback(addr):
    print("pong Location from " + addr)
    pass

def transitionCallback(addr,piece,piecePrev,offset,direction):
    print("Piece transition " + addr +" piece:"+ str(piece) +" piecePrev:"+str(piecePrev)+" offset:"+str(offset)+" direction:"+str(direction))
    pass

def delocalizedCallback():
    print("Delocalized!!!!")
    pass

def offsetFromRoadCenter(offset):
    print("Offset from Rd center:" + str(offset))

#car = Overdrive("F5:64:F7:27:C4:70")
car = Overdrive("E4:E7:75:16:93:AC")
print("LTE-B DEMO:", str(dir(car)))
car.setDelocalizedCallback(delocalizedCallback)
car.setOffsetFromRoadCenterCallback(offsetFromRoadCenter)

#car.setPongCallback(pongCallback)
#car.setTransitionCallback(transitionCallback)
car.setLocationChangeCallback(locationChangeCallback) # Set location change callback to function above
car.changeSpeed(200, 1000) # Set car speed with speed = 500, acceleration = 1000
#car.changeLaneRight(1000, 1000) # Switch to next right lane with speed = 1000, acceleration = 1000
#input() # Hold the program so it won't end abruptly
car.ping()
car.changeLane(800,1000,0)

car2 = Overdrive("F5:64:F7:27:C4:70")
car2.setDelocalizedCallback(delocalizedCallback)
car2.setLocationChangeCallback(locationChangeCallback)
car2.changeSpeed(200, 1000)
car2.changeLane(800,1000,0)

while True:
    #print("Notification:",car.getNotificationsReceived())
    time.sleep(5)
    car.changeSpeed(200,1000)
    car.changeLane(800,1000, -44.6)
    #car.changeLaneLeft(500,1000)
    time.sleep(5)
    #car.changeLaneRight(500,1000)
    car.changeSpeed(200,1000)
    car.changeLane(800,1000, 44.0)
    #ret = input("Please enter stop track ID:")
    #print(ret)
    #car.changeLane(800,1000,float(ret))
    #track_id = int(ret)
    #car.changeSpeed(500,1000)
    
    pass
