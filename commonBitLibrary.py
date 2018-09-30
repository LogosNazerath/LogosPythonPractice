def loneyInteger(arrayOfLoneyInteger):
    result = 0
    for item in arrayOfLoneyInteger:
        result ^= item
        print result
    return result