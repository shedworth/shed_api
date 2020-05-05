#! /usr/bin/env python
import serial, time

arduino = serial.Serial('/dev/ttyACM0', 19200, timeout=.5)
    
tempo = 100
beat = int(tempo/3.7)
tempBeat = (60.0/tempo)

stored_values_A = {	'fixture_A': 1,
										'pattern_A': 0,
										'red_1_A': 0,
										'green_1_A': 0,
										'blue_1_A': 0,
										'red_2_A': 0,
										'green_2_A': 0,
										'blue_2_A': 0,
										'rate_A': 0,
									}
									
stored_values_B = {	'fixture_B': 2,
										'pattern_B': 0,
										'red_1_B': 0,
										'green_1_B': 0,
										'blue_1_B': 0,
										'red_2_B': 0,
										'green_2_B': 0,
										'blue_2_B': 0,
										'rate_B': 0,
									}
stored_values_C = {	'fixture_C': 3,
										'pattern_C': 0,
										'red_1_C': 0,
										'green_1_C': 0,
										'blue_1_C': 0,
										'red_2_C': 0,
										'green_2_C': 0,
										'blue_2_C': 0,
										'rate_C': 0,
									}

fixture_list = {1: stored_values_A,
								2: stored_values_B,
								3: stored_values_C
								}	
											
def control_shed(shed_params):
	shed_move = ShedMove(shed_params)
	shed_move.action()

class ShedMove(object):
    
    def __init__(self, shed_params):
        self.shed_params = shed_params
        self.fixture = shed_params['fixture']
        self.pattern = shed_params['pattern']
        self.colour1 = Colour(shed_params['red_1'], shed_params['green_1'], shed_params['blue_1'])
        self.colour2 = Colour(shed_params['red_2'], shed_params['green_2'], shed_params['blue_2'])
        self.rate = shed_params['rate']
        #stored_values = shed_params

    def action(self):
        self.rate = (str(self.rate).zfill(3))        
        serialOut = (str(self.fixture) + str(self.pattern) + str(self.colour1) + str(self.colour2) + str(self.rate) + "\n")
        #print(str(self.fixture))
        #print(str(self.pattern))
        #print(str(self.colour1))
        #print(str(self.colour2))
        #print(str(self.rate))

        arduino.write(str.encode(serialOut))
        
def Colour(red, green, blue, white = 0):
    if white == 0 and red == 0 and green == 0 and blue ==0:
        return str("00000000")
    else:
        return ((str((white << 24) | (red << 16)| (green <<8) | blue)).zfill(8))

def sides(pattern, red1, green1, blue1, red2, green2, blue2, rate):
        shedMove(1,pattern,red1,green1,blue1,red2,green2,blue2,rate)
        shedMove(2,pattern,red1,green1,blue1,red2,green2,blue2,rate)
        
def window(pattern,red1,green1,blue1,red2,green2,blue2,rate):
        shedMove(3,pattern,red1,green1,blue1,red2,green2,blue2,rate)

def flames(rate):
        shedMove(4,0,0,0,0,0,0,0,rate)

""" Define some lighting states"""
def test():
	print("Hello world!")

def sidesblack():
    sides(1,0,0,0,0,0,0,0)

def sides1():   # sides purple
    sides(1,150,0,150,0,0,0,0)    

def sides2():   # sides yellow
    sides(1,255,150,0,0,0,0,0)

def sides3():   #sides red
    sides(1,255,0,0,0,0,0,0)

def sides4():   # sides green
    sides(1,0,35,0,0,0,0,0)

def sides5():   # sides blue
    sides(1,0,0,255,0,0,0,0)

def sides_scan1():  # sides scan yellow
    sides(2,255,150,0,0,0,0,12)
 



#time.sleep(5) # wait for Arduino to get its shit together
