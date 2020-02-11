#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:07:57 2018

@author: jose
"""

import numpy as np

class Ant(object):          #class ant, every instance of the class is a virtual ant whose task is to explore an area where he is placed
    AreaF = np.zeros((9,9)) #The area where the Feromone is placed
    alpha = 0.5             #constant weights to be used when a new position is taken by an Ant
    beta = 0.5              
    def __init__(self, goalPos, homePos, actPos, TabuArea):
        self.GoalPos = goalPos  #The position where the Ant has to reach
        self.HomePos = homePos  #The positio where the Ant start searching fo the GoalPosition
        self.ActPos = actPos        #np.Array, the Present location of the Ant in the given Area
        self.Journey = [[homePos[0], homePos[1]]]   #the list of locations the Ant has visited so far
        self.TabuArea = TabuArea    #The Area where the forbidden locations for the Ant are placed
        self.FixedTabuArea = TabuArea #The area where every Ant instace will exlore, including the forbidden places the ant can visit
        self.Memory = [[0,0]]       #Each Ant is given a Memory of six places, e.g. the Ant will remember ten past position it has visited
    def getGoalPos(self):       #Methods to retrieve information about the Ant instance
        return self.GoalPos
    def getHomePos(self):
        return self.HomePos
    def getActPos(self):
        return self.ActPos
    def getJourney(self):
        return self.Journey
    def getJourneyLen(self):
        return len(self.Journey)
    def getTabuArea(self):
        return self.TabuArea
    def getFixedTabuArea(self):
        return self.FixedTabuArea
    def getMemory(self):
        return self.Memory
    
    def getAreaF(self):     #Methods to retrieve information about the Ant class
        return Ant.AreaF
    
    
    def Explore(self):      #Method to start the exploration 
        #before starting the exploration, remember to initialize Ant.AreaF
        newPos = self.NextPos(self.ActPos, self.GoalPos, self.TabuArea) #The method NextPos() is called, retrieving the next position the ant is exploring based on the actual one
        self.Journey.append([newPos[0][0], newPos[0][1]])               #The new position is added in the Journey list
        self.Memory.append([newPos[0][0], newPos[0][1]])                #The new position is added as well to the memory list
        self.ActPos = np.array((newPos[0][0],newPos[0][1]))             #The Actual position is updated with the next position coordinates
        while(self.dist(self.ActPos, self.GoalPos) != 0.001):           #If the new position is the Goal position, the search is over, otherwise, the Ant starts exploring until this condition is achieved
            self.updateTabuArea()                               #The method updateTabuArea() is called to place the new positions where the Ant cannot explore anymore
            newPos = self.NextPos(self.ActPos, self.GoalPos, self.TabuArea) #The method NextPos() is called, retrieving the next position the ant is visiting
            self.Journey.append([newPos[0][0], newPos[0][1]])   #The ner position is added to the Journey list
            if len(self.Memory)< 6:                             #Since the ant shall only remember six position it has visited, once the seventh position is reached, the Ant "forgets"  the fist position in the Memory list and adds the next position visited                 
                self.Memory.append([newPos[0][0], newPos[0][1]])
            else:
                self.Memory.reverse()
                self.Memory.pop()
                self.Memory.reverse()
            self.ActPos = np.array((newPos[0][0],newPos[0][1]))  #The actual position is updated 
    
    def updateTabuArea(self):                           #Method used to update the positions the Ant cannot visit
        self.TabuArea = self.FixedTabuArea              #First, the TabuArea is reseted 
        for i in range(0,len(self.Memory)): 
            self.TabuArea[self.Memory[i][0]][self.Memory[i][1]] #After the TabuArea is as in the beggining of the exploration, the posotions saved in the Ant memory are now forbidden to it, e.g. the ant cannot visit the positions it has already visited
            
    
    def initializeAreaF(self,row,col, feroInit):        #Method used to start the Area of Feromones, every position has a feromone density and it has to be initialized with a value      
        Area = np.zeros((row,col))
        for i in range(0,row):
            for j in range(0,col):
                if (i> 0) and (i < row-1 ) and (j > 0) and (j < col-1):
                    Area[i][j] = feroInit* self.FixedTabuArea[i][j]
        Ant.AreaF = Area        
        
        
    def NextPos(self, actual, goal, area):          #Method which retrieves the next position the Ant is taking based on the Actual position and the Feromone Map
        operations = np.array(((0,1),(1,0),(0,-1),(-1,0))) #This operations denote that the ant cannot move in diagonals
        probabilities = self.getProb(actual, goal, area, operations) #Every position the ant can reach from its actual position has a probability to be chosen based on the feromone the position has and how near the position is to the Goal Position
        Choice =np.random.choice([0, 1, 2, 3], 1, p = probabilities) #After the probabilities are given, one of the positions is chosen 
        return operations[Choice] + actual          #The next position is returned 
        
    def getProb(self,actual,goal, area, operations):    #actual has to be an np.array, this mehotd returns the probabilities of being chosen from every possible position the Ant can reach from its actual Position
        probs = {0:0, 1:0, 2:0, 3:0}            #a dictionary is initialized, the positions 0, 1, 2, 3 have at the beggining zero probability of being chosen
        summ = 0                                #The total addition is initialized to zero
        for i in probs:                         #loop in the dictionary
            coord = operations[i]+actual        #get the coordinates of the position whose probability is being calculated
            val = ((Ant.AreaF[coord[0]][coord[1]]**Ant.alpha)*(1/(self.dist(coord,goal))**Ant.beta))*area[coord[0]][coord[1]] #This value is the (Feromone in the position)^(alpha, a weight value) * (1/euxclidean distance from the position to the Goal Position)^(beta, a weight value) * (the value of the area (1: position free of being visited, 0: forbidden position, it cannot be visited
            probs[i] = val                      #the value inside the dictionary os updated
            summ += val                         #the summatory of the total result is updated
        probabilities = []                      #the probabilities list is initialized
        for i in probs:                         #loop in the Dictionary 
            probabilities.append( probs[i]/summ )   #the probabilities of every possible position is calculated and stored inside the Dictionary
        if sum(probabilities) <0.9:             #If the summatory of the probabilities is less than 0.99, it meands the ant has reached a dead end, in which case another Method is called to overcome such situation
            probabilities = self.getProbTabuless(actual, goal, operations)
        return probabilities
        
    def getProbTabuless(self,actual,goal, operations):    #actual has to be an np.array, this method is called when the Ant has gotten to a dead end. The Tabu area is ignored and the probabilities are calculated as in the Method getProb()
        probs = {0:0, 1:0, 2:0, 3:0}
        summ = 0
        for i in probs:
            coord = operations[i]+actual
            val = ((Ant.AreaF[coord[0]][coord[1]]**Ant.alpha)*(1/(self.dist(coord,goal))**Ant.beta))
            probs[i] = val
            summ += val
        probabilities = []
        for i in probs:
            probabilities.append( probs[i]/summ )
        return probabilities
    
    
    def dist(self, actual, goal):   #Method which returns the euclidean distance from an actual point to a goal point
        d = ((actual[0]-goal[0])**2 + (actual[1]-goal[1])**2)**0.5
        if d == 0:          #if distance is zero, it means that the actual and goal position are the same, however, returning zero causes that the program gets a NaN (division by zero), so, a very very small value is returned
            d = 0.001
        return d
    
    def UpdateFeromone(self, SmallestJourney, rho, delta):  #SmallestJourney is an np.array, the feromone in the area goes through a process where it is "evaporated" in every position and "reinforced" in specific positions
        Ant.AreaF *=(1-rho)     #the evaporation of the feromone is given by this line, implying that the feromone is being decreased a rho factor
        for i in range(0, len(SmallestJourney)):    #after the feromone is evaporated, the feromone in the positions of the list SmallestJourney are reinforced by adding (1/the length of the list SmallestJourney)
            Ant.AreaF[SmallestJourney[i][0]][SmallestJourney[i][0]] = (Ant.AreaF[SmallestJourney[i][0]][SmallestJourney[i][0]]) + (Ant.AreaF[SmallestJourney[i][0]][SmallestJourney[i][0]])*(delta/len(SmallestJourney))
    
        
class Colony(object):          #class Colony, the Colony will be formed by n Ants and will be responsible of the Feromone update and the smallest journey  
        def __init__(self, numberOfAnts, Epochs, StartingPoint, EndingPoint, ObstacleArea, rho, delta,InitialFeromone):
            self.AntsNumber = numberOfAnts #int, The number of Ants the class will be formed by
            self.EPOCHS = Epochs            #int, Number of epochs the Colony will explore the Area
            self.StartPos = StartingPoint   #2 dimentional np.array, the position where every Ant in the Colony will start searching
            self.EndPos = EndingPoint       # 2 dimentional np.array, the final position every Ant in the Colony has to reach
            self.Area = ObstacleArea        #Row x Col dimentional np.array, the Area containing the position where no Ant of the Colony can visit
            self.Rho = rho                  #float smaller than 1, the feromone evaporation factor
            self.Delta = delta              #float, the update feromone factor of the 1/(len of journey) value
            self.InitialPheromone = InitialFeromone #float, the Feromone Area is initialized with a constant value
        def SearchRoute(self):          #Method to start the Area exploration
            row, col = self.Area.shape #The dimentions of the Area are taken
            Perez = []      #the Colony instance is initialized
            PapaPerez = Ant(self.EndPos, self.StartPos, self.StartPos, self.Area) #the Colony Watcher is initialized, this Watcher is not used to explore, but to update the Feromone and Tabu Area
            PapaPerez.initializeAreaF(row,col,self.InitialPheromone)    #The watcher is used to initialize the Feromone Area, e.g. every Ant instance will share the same Feromone Area
            MinJourney = 0 #The smallest journey variable is initialized
            MinJourneyLen = 255*255     #the length of the smallest journey is initialized with a ridiculously big number 
            for m in range(0,self.EPOCHS):  #the Search will take place EPOCHS times
                for i in range(0,self.AntsNumber):  #The Colony instance is initialized with AntsNumber members, and every Ant instance inside the Colony instance is initialized as well
                    Perez.append(Ant(self.EndPos, self.StartPos, self.StartPos, self.Area))
                
                for i in range(0,self.AntsNumber): #every Ant inside the Colony initialize the Area with the initial Pheromone value and starts the exploration
                    Perez[i].initializeAreaF(row,col,self.InitialPheromone)
                    Perez[i].Explore()
                for i in range(0,self.AntsNumber): #Once every Ant inside the Colony finishes exploring, the smallest journey (the journey with the less positions visited) is found
                    if Perez[i].getJourneyLen() < MinJourneyLen :
                        MinJourneyLen = Perez[i].getJourneyLen() 
                        MinJourney = Perez[i].getJourney()
                #for i in range(0,numberOfAnts):
                #    print(Perez[i].getJourneyLen())
                Perez.clear()   #The Ants inside the Class are erased
                PapaPerez.UpdateFeromone(MinJourney,self.Rho, self.Delta)  #the Colony watcher is used to update the Pheromone in the Area that every Ant instance shares
            return MinJourney   #Once the EPOCHS are finished, the smallest Journey found within the EPOCHS is returned


'''
row = 9  #row and col have to be bigger by two units of the actual area  
col = 9
Area = np.zeros((row,col))
for i in range(0,row):
    for j in range(0,col):
        if (i> 0) and (i < row-1 ) and (j > 0) and (j < col-1):
            Area[i][j] = 1
Area[2][2] = 0

Col = Colony(10, 10, np.array((1,1)), np.array((7,7)), Area, 0.001, 1,0.1)
m = Col.SearchRoute()
'''


class BMWRoute(object):     #BMW object, this object is used so that the Colony adn the Ant classes are initialized and used for the BMW challenge
    def __init__(self, listOfPoints):
        self.Points = listOfPoints      #list of 2 dimentional np.arrays, this points represent both of the tunnel entrances, every four points represent one tunnel
    
    def Start(self):        #Method used to start the route search after the points are given
        obst = []       #List of obstacles initialized
        for i in range(0, len(self.Points)):    #this loop is used to get the actual positions of the tunnels, to treat them as obstacles in the rout search
            px = (self.Points[i][0][0] + self.Points[i][1][0])/2
            py = (self.Points[i][0][1] + self.Points[i][1][1])/2
            obst.append((px,py))
            
        start = np.array((1,1))     #The initial point assumed to be [1,1] in the map
        d1 = 0                  #two distances variables, d1 and d2, are initialized
        d2 = 0
        orderedPoints = [start]     #The first point to be inside the orderedPoints list is the start point
        for i in range(0, len(self.Points)): #This loop is intended to do 1 task, order the points so that the next point of the tunnel is the nearest to the last one
            d1 = self.distance(self.Points[i][0], start)
            d2 = self.distance(self.Points[i][1], start)
            if min(d1,d2) == self.distance(self.Points[i][0], start):
                orderedPoints.append(self.Points[i][0])
                orderedPoints.append(self.Points[i][1])
                start = self.Points[i][1]
            elif min(d1,d2) == self.distance(self.Points[i][1], start):
                orderedPoints.append(self.Points[i][1])
                orderedPoints.append(self.Points[i][0])
                start = self.Points[i][0]
            else:
                orderedPoints.append(self.Points[i][0])
                orderedPoints.append(self.Points[i][1])
                start = self.Points[i][1]
        orderedPoints.append(np.array((7,7)))   #The Final Goal Point is stored insite the orderedPoints list
            
           
        row = 9  #row and col have to be bigger by two units of the actual area  
        col = 9
        Area = np.zeros((row,col))  #The area is initialized as a zero array, and then just the out boundary is preserved as zeros, the rest of the positions are set to a value of 1
        for i in range(0,row):
            for j in range(0,col):
                if (i> 0) and (i < row-1 ) and (j > 0) and (j < col-1):
                    Area[i][j] = 1
                    
        for i in range(0, len(obst)):   #after the area is initialized, the positions where the tunnels are placed inside the matrix are set to a value of zero, meaning this position is an obstacle
            Area[int(obst[i][0])][int(obst[i][1])] = 0
            #print(i)
        FinalRoute = []  #The list which will contain the positions which form the route to be followed
        count = 0
        for i in range(0, len(orderedPoints)-1,2):  #in this loop the initial point and the goal point are given to the Colony class so that the Ant instances find a way.
            #print(orderedPoints[i])                #the way these points are given to the program are as follows: orderedPoints[i] = Start Position;  orderedPoints[i+1] = Goal position
            #print(orderedPoints[i+1])
            print(orderedPoints[i],orderedPoints[i+1])
            if self.distance(orderedPoints[i], orderedPoints[i+1]) == 0:  #if the starting point and the goal point are the same, this point is added to the list and the nearest tunnel as well
                FinalRoute.append(orderedPoints[i])
                FinalRoute.append(obst[int((i+1)/2)])
                count +=1
                continue
            else:
                    
                Col = Colony(10, 10, orderedPoints[i], orderedPoints[i+1], Area, 0.001, 1,0.1) #if the start and goal positions are different, they are given to the Colony class instance, the area where the Ant instanecs will explore, the initial pheromone value and constants
                m = Col.SearchRoute() #then the route of this search is added to the FinalRoute list
                for i in m:
                     FinalRoute.append(i)   
                #FinalRoute.append(m)
                
                if count < 4:   
                     FinalRoute.append(obst[count])     #the obstacle/tunnel in turn is added
                count +=1
            
        return orderedPoints, Area, FinalRoute

    def distance(self, a, b):       #method to calculate the euclidean distance between to points
        d = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5      
        return d
    
    

