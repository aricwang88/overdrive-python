from overdrive import Overdrive

def locationChangeCallback(addr, location, piece, speed, clockwise):
    # Print out addr, piece ID, location ID of the vehicle, this print everytime when location changed
    print("Location from " + addr + " : " + "Piece=" + str(piece) + " Location=" + str(location) + " Clockwise=" + str(clockwise))


car = Overdrive("F5:64:F7:27:C4:70")
car.setLocationChangeCallback(locationChangeCallback) # Set location change callback to function above
car.changeSpeed(200, 1000) # Set car speed with speed = 500, acceleration = 1000
#car.changeLaneRight(1000, 1000) # Switch to next right lane with speed = 1000, acceleration = 1000
input() # Hold the program so it won't end abruptly
