#Here is a main app where we will call functions and classes
#from other .py files.
#There will be a main page that loads with options
#A function to set new goals
#A function to edit goals
#A function to contribute towards a goal (will have a summary progress report at end)
#A function to show all contributions towards all goals (user can filter month, week, type of activity)
#An option to see how much left till goal with that number chopped down to monthly, weekly and daily averages.
#adding a back option for each menu and user error handling

#ultimately there are 3 dictionaries to be saved into the txt file

#there needs to be an option to delete one goal, all goals or to reduce progress.

import json
empty_json = {} 
empty_json_string = json.dumps(empty_json) 
goals2Load = open('goals2.json')
goals3Load = open('goals3.json')
goals1 = open('goals.json',)
goals = {}
goals = json.load(goals1)
goals2 = {}
goals2 = json.load(goals2Load)
goals3 = {}
goals3 = json.load(goals3Load)
def mainDisplay():
    print('\n\t1) Set a goal\n\t2) Edit a goal\n\t3) Add progress\n\t4) Progress Report\n\t5) Left to target\n\t6) Save and Exit')
    return
def setGoal():
    goalInput = input('\nPlease enter the name of the activity:\t')
    goalAmount = int(input('\nPlease enter the yearly amount only:\t'))
    goalUnit = input('\nPlease enter the unit for the amount:\t')
    goals[goalInput] = goalAmount
    goals2[goalInput] = goalUnit

def editGoal():
    keyDict = goals.keys()
    keyList = list(keyDict)
    keyNum = 0
    print('\n')
    for key in goals:
        print(str(keyNum+1)+') Your '+ keyList[keyNum] +' goal of '+str(goals.get(key))+ ' '+str(goals2.get(key))+' a year.')
        keyNum += 1
    goalChoice = int(input('\nPlease enter your choice:\t'))
    print('\nYour '+ keyList[goalChoice-1]+ ' goal of '+str(goals.get(keyList[goalChoice-1]))+' '+str(goals2.get(keyList[goalChoice-1]))+' a year.')
    editChoice = int(input('\nWhich part of it do you want to edit?\t 1) Name\t 2) Amount\t 3) Unit\n'))
    if editChoice == 1:
        newName = input('\nPlease enter the new name:\t')
        goals[newName] = goals.pop(keyList[goalChoice-1])
        print('\nName was changed successfuly.\n')
        print('\nYour '+ keyList[goalChoice-1]+ ' goal of '+str(goals.get(keyList[goalChoice-1]))+' '+str(goals2.get(keyList[goalChoice-1]))+' a year.')
        return
    elif editChoice == 2:
        newAmount = int(input('\nPlease enter the new amount:\t'))
        goals[str(keyList[goalChoice-1])] = newAmount
        print('\nAmount was changed successfuly.\n')
        print('\nYour '+ keyList[goalChoice-1]+ ' goal of '+str(goals.get(keyList[goalChoice-1]))+' '+str(goals2.get(keyList[goalChoice-1]))+' a year.')
        return
    elif editChoice == 3:
        newUnit = input('\nPlease enter the new unit:\t')
        goals2[keyList[goalChoice-1]] = newUnit
        print('\nUnit was changed successfuly.\n')
        print('\nYour '+ keyList[goalChoice-1]+ ' goal of '+str(goals.get(keyList[goalChoice-1]))+' '+str(goals2.get(keyList[goalChoice-1]))+' a year.')
        return 
def addProgress():
    keyDict = goals.keys()
    keyList = list(keyDict)
    keyNum = 0
    print('\n')
    for key in goals:
        print(str(keyNum+1)+') '+ keyList[keyNum])
        keyNum += 1
    goalChoice = int(input('\nPlease enter your choice:\t'))
    progressAmount = int(input('\nPlease enter the amount of progress:\t'))
    goals[str(keyList[goalChoice-1])] += progressAmount
    print('\nProgress successfuly saved.')
    print('\nYour '+str(progressAmount)+' '+goals2.get(str(keyList[goalChoice-1]))+' were recorded.')
    return
def reportProgress():
    keyDict = goals.keys()
    keyList = list(keyDict)
    keyNum = 0
    print('\n')
    for key in goals:
        print(str(keyNum+1)+')\t'+ keyList[keyNum]+ '\t|\tYearly Target:\t'+str(goals.get(key))+'\t|\tYour Progress:\t'+str(2000))
        keyNum += 1
    #The 2000 is a placeholder
    return
def leftGoal():
    return
menuInput = 8
while menuInput:
    mainDisplay()
    menuInput = int(input('Please enter your choice:\t'))
    if menuInput == 1:
        setGoal()
    elif menuInput == 2:
        editGoal()
    elif menuInput == 3:
        addProgress()
    elif menuInput == 4:
        reportProgress()
    elif menuInput == 5:
         leftGoal()
    elif menuInput == 6:
        open('goals.json',w).close()
        open('goals2.json','w').close()
        open('goals3.json','w').close()
        with open('goals.json','w') as goalFile:
            json.dump(goals, goalFile)
        with open('goals2.json','w') as UnitFile:
            json.dump(goals2, UnitFile)
        with open('goals3.json','w') as progressFile:
            json.dump(goals3 , progressFile)
        quit()
    else: menuInput = 8


