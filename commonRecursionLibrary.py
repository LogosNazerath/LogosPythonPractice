def fib(interval):
    if(interval == 1):
        return 1
    elif(interval == 2 ):
        return 1
    else:
        return (fib(interval-1)+fib(interval-2))

def fibMemoize(seqMemo):
    fibSeq = seqMemo[0]
    memo = seqMemo[1]

    if(fibSeq == 1):
        return [1,memo]
    elif(fibSeq == 2 ):
        return [1,memo]
    elif(str(fibSeq) in memo):
        pass
    else:
        memo[str(fibSeq)] = fibMemoize([fibSeq-1,memo])[0] + fibMemoize([fibSeq-2,memo])[0]
    return [memo[str(fibSeq)],memo]