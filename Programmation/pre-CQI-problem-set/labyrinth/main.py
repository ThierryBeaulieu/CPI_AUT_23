#!/usr/bin/env python3
import json
import math

for i in range(100):
    string = str(i)
    if len(string) == 1:
        string = "0" + string

    answer_path = "./solutions/extreme/labyrinth_" + string + ".txt"
    file_path = "./labyrinths/extreme/labyrinth_" + string + ".json"

    with open(file_path, "r") as file:
        data = json.load(file)

    def getType(dict): 
        return dict["_jsontype_"]

    # Makes sure no value is outside of the 2D array
    def getRelative(x, y):
        if x < 0:
            x += SIZE
        if y < 0:
            y += SIZE
        if x >= SIZE:
            x -= SIZE
        if y >= SIZE:
            y -= SIZE
        return x, y

    # Get ARC coordinates from cartesian coordinates
    def getArc(x, y):
        return y % 2, int(math.floor(y / 2)) if int(math.floor(y / 2)) <= maxR else int(math.floor(y / 2)) - SIZE / 2, x if x <= maxC else x - SIZE

    if not getType(data) == "Labyrinth":
        print("Error1", i)

    SIZE = 1000
    
    # -1 means there is no tile. There is a set size for optimisation
    dataOrganisedInCartesian = [[-1 for x in range(SIZE)] for y in range(SIZE)]
    maxR = 0
    minR = 0
    maxC = 0
    minC = 0

    # Directions of the reachable tiles for a step according to a value in HECS system
    accessibleTilesForA0 = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1)]
    accessibleTilesForA1 = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1)]

    # Converts the dict into a 2D array containing each tileType 
        # 0 -> Normal tile
        # 1 -> Wall tile
        # 2 -> Start tile
        # 3 -> End tile
    for tile in data["tiles"]:
        a = r = c = tileType = 0
        for attribute in tile:
            if getType(attribute) == "HexTile":
                a = attribute["a"]
                r = attribute["r"]
                c = attribute["c"]
            elif getType(attribute) == "TileType":
                if attribute["type"] == "TileType.NORMAL":
                    tileType = 0
                elif attribute["type"] == "TileType.WALL":
                    tileType = 1
                elif attribute["type"] == "TileType.START":
                    tileType = 2
                elif attribute["type"] == "TileType.END":
                    tileType = 3
                    
        # Keeps track of the min and max for r and c to make sure there is no overflow of the 2D array
        maxR = max(maxR, r)
        maxC = max(maxC, c)
        minR = min(minR, r)
        minC = min(minC, c)
        
        x = c
        y = 2 * r + a
        x, y = getRelative(x, y)
        dataOrganisedInCartesian[y][x] = tileType
    
    if maxR - minR >= SIZE / 2:
        print("error4", i)
    if maxC - minC >= SIZE:
        print("error5", i)
        
    # Finds all the possible paths by taking one step in any direction from the current path
    def getNextStep(currentPath):
        currentPosition = currentPath[-1]
        paths = []
        specificAccessibleTiles = accessibleTilesForA0 if currentPosition[1] % 2 == 0 else accessibleTilesForA1
        
        # Takes one step in every direction
        for tileOffset in specificAccessibleTiles:
            newX = currentPosition[0] + tileOffset[0]
            newY = currentPosition[1] + tileOffset[1]
            newPos = getRelative(newX, newY)
            newType = dataOrganisedInCartesian[newPos[1]][newPos[0]]
            
            if(newType == 1 or newType == -1):
                continue
            
            paths.append(currentPath + [newPos])
        return paths
    
    MAX_DEPTH = 100000
    
    # Initial values (these should be modified)
    startTile = (-1, -1)
    endTile = (-1, -1)

    for y in range(len(dataOrganisedInCartesian)):
        for x in range(len(dataOrganisedInCartesian[0])):
            if dataOrganisedInCartesian[y][x] == 2:
                startTile = (x, y)
            elif dataOrganisedInCartesian[y][x] == 3:
                endTile = (x, y)
                
    if startTile == (-1, -1) or endTile == (-1 -1) or startTile == endTile:
        print("Error2", i)
        
    currentPaths = [[startTile]]
    visitedTiles = []
    answer = -1, -1
    found = False

    for depth in range(MAX_DEPTH):
        
        # Filter paths that lead to a previously visited tile
        filteredCurrentPaths = []
        for path in currentPaths:
            if not path[-1] in visitedTiles:
                if path[-1] == endTile:
                    answer = path, depth
                    found = True
                    break
                filteredCurrentPaths.append(path)
                visitedTiles.append(path[-1])
        if found:
            break
        currentPaths = filteredCurrentPaths
        
        # Generates new paths from all existing paths
        newCurrentPaths = []
        for path in currentPaths:
            newPaths = getNextStep(path)
            newCurrentPaths = newCurrentPaths + newPaths
        currentPaths = newCurrentPaths

    answerPath = [getArc(z[0], z[1]) for z in answer[0]]

    # Exports the result
    with open(answer_path, 'w') as file:
        for tup in answerPath:
            file.write(str(tup) + '\n')