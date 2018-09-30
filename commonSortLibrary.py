from random import randint
from sys import setrecursionlimit

setrecursionlimit(100000)

def bubbleSort(itemsArray):
    lastPosition = len(itemsArray) - 1
    while 0 < lastPosition:
        currentPosition = 0
        while currentPosition < lastPosition:
            if(itemsArray[currentPosition] > itemsArray[currentPosition+1]):
                swap(itemsArray,currentPosition,currentPosition+1)
            currentPosition += 1
        lastPosition -= 1
    return itemsArray

def quickSort(itemsArray, recursionCounter):
    recursionCounter += 1
    if(len(itemsArray) == 2):
        if(itemsArray[0] > itemsArray[1]):
            itemsArray = swap(itemsArray,0,1)
        return [itemsArray, recursionCounter]
    elif (len(itemsArray) <= 1):
        return [itemsArray, recursionCounter]

    pivot = itemsArray[len(itemsArray) // 2]
    leftPosition = 0
    rightPosition = len(itemsArray) - 1

    while(leftPosition < rightPosition):
        while(itemsArray[leftPosition] < pivot):
            leftPosition += 1
        while(itemsArray[rightPosition] > pivot):
            rightPosition -= 1
        if(itemsArray[leftPosition] == itemsArray[rightPosition]):
            leftPosition += 1
        else:
            swap(itemsArray,leftPosition,rightPosition)
   
    subArrayLeft = quickSort(itemsArray[0:leftPosition],0)
    subArrayRight = quickSort(itemsArray[leftPosition:len(itemsArray)],0)
    
    newArray = subArrayLeft[0] + subArrayRight[0]
    recursionCounter = recursionCounter + subArrayLeft[1] + subArrayRight[1]

    return [newArray,recursionCounter]

def mergeSort(itemsArray, recursionCounter):
    recursionCounter += 1
    if(len(itemsArray) == 1):
        return [itemsArray,recursionCounter]
    
    leftHalf = mergeSort(itemsArray[0:(len(itemsArray)//2)], 0)
    rightHalf = mergeSort(itemsArray[len(itemsArray)//2:len(itemsArray)], 0)
    recursionCounter = recursionCounter + leftHalf[1] + rightHalf[1]
    return [merger(leftHalf[0],rightHalf[0]),recursionCounter]

def merger(leftArray,rightArray):
    leftIndex = 0
    rightIndex = 0
    itemsArray = []
    while (leftIndex < len(leftArray) and rightIndex < len(rightArray)):
        if leftArray[leftIndex] < rightArray[rightIndex]:
            itemsArray.append(leftArray[leftIndex])
            leftIndex += 1
        else:
            itemsArray.append(rightArray[rightIndex])
            rightIndex += 1
    if(leftIndex == len(leftArray)):
        itemsArray = itemsArray + rightArray[rightIndex:len(rightArray)]
    else:
        itemsArray = itemsArray + leftArray[leftIndex:len(leftArray)]
    return itemsArray
        

def swap(itemsArray, indexA, indexB):
    holdValue = itemsArray[indexA]
    itemsArray[indexA] = itemsArray[indexB]
    itemsArray[indexB] = holdValue
    return itemsArray

def resetIntArray(lowerRangeBound,upperRangeBound,lowestInt,highestInt):
    interval = randint(lowerRangeBound,upperRangeBound)
    x = 0
    array = []
    while x < interval:
        array.append(randint(lowestInt,highestInt))
        x += 1
    return array