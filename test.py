# from commonSortLibrary import swap, bubbleSort, quickSort, mergeSort, resetIntArray
# from commonRecursionLibrary import fib, fibMemoize
# from commonBitLibrary import loneyInteger
# from datetime import datetime
# from random import randint
# from copy import deepcopy

# sourceArray = resetIntArray(100,400,-1000,1000)
# bubbleArray = deepcopy(sourceArray)
# mergeArray = deepcopy(sourceArray)
# quickArray = deepcopy(sourceArray)

# #SWAP
# #arrayOfThing = resetIntArray(50,100,-1000,1000)
# #print arrayOfThing
# #print swap(arrayOfThing,0,len(arrayOfThing)-1)
# #print '\r\n\r\n'

# #BUBBLE SORT
# a = datetime.now()
# #bubbleArray = resetIntArray(50,100,-1000,1000)
# #print bubbleArray
# print bubbleSort(bubbleArray)
# print '\r\n\r\n'

# #QUICK SORT
# b = datetime.now()
# recursionCounter = -1
# #quickArray = resetIntArray(50,100,-1000,1000)
# #print quickArray
# quickResult = quickSort(quickArray,-1)
# print quickResult[0]
# print '\r\n\r\n'

# #MERGE SORT
# c = datetime.now()
# recursionCounter = -1
# #mergeArray = resetIntArray(50,100,-1000,1000)
# #print mergeArray
# mergeResult = mergeSort(mergeArray, -1)
# print mergeResult[0]
# print '\r\n\r\n'

# d = datetime.now()

# print '----Sort Summary----'
# print 'Array Length: ' + str(len(sourceArray))
# print 'BubbleSort time: ' + str((b-a).microseconds)
# print 'QuickSort time: ' + str((c-b).microseconds)
# print 'QuickSort Recursions: ' + str(quickResult[1])
# print 'MergeSort time: ' + str((d-c).microseconds)
# print 'MergeSort Recursions: ' + str(mergeResult[1])
# print '\r\n\r\n'

# #fibSequence = randint(0,20)
# fibSequence = 25
# memo = {}
# print fibSequence
# e = datetime.now()
# print fibMemoize([fibSequence,memo])[0]
# f = datetime.now()
# print str(fib(fibSequence))
# g = datetime.now()

# print '----Recursion Summary----'
# print str(f-e)
# print str(g-f)
# print '\r\n\r\n'

# loneyIntegerArray = [1,1,2,2,3,3,4,5,5,6,6,7,7]

# print '----Bit Summary----'
# print loneyInteger(loneyIntegerArray)


