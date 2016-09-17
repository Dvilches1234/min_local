import math
from random import randint
from itertools import accumulate

def find_min(arr):
	n=len(arr)
	mid=math.floor(n/2)
	first=0
	last=n-1
	return search_min(arr,first,mid,last,n)

def search_min(arr,first,mid,last,n):
	if mid==0 or mid==n-1:
		return mid
	if mid==first and mid!=0:
		return last	
	elif arr[mid]<=arr[mid-1] and arr[mid]<=arr[mid+1]:
		return mid
	elif arr[mid-1]>arr[mid] and arr[mid]>arr[mid+1]:
		first=mid
		mid=math.floor((last+mid)/2)
		return search_min(arr,first,mid,last,n)
	elif arr[mid-1]<arr[mid] and arr[mid]<arr[mid+1]:
		last=mid
		mid=math.floor(mid/2)
		return search_min(arr,first,mid,last,n)
	elif arr[mid-1]<arr[mid] and arr[mid+1]<arr[mid]:
		if n-mid<mid:
			first=mid
			mid=math.floor((last+mid)/2)
			return search_min(arr,first,mid,last,n)
		else:	
			last=mid
			mid=math.floor(mid/2)
			return search_min(arr,first,mid,last,n)



def randomwalk(N):
    W = [ randint(-1, 1) for _ in range(N)]
    A = list(accumulate(W))
    return A			
			

if __name__ == '__main__':
    from timeit import Timer
    # from sys import argv
    b = [10000, 100000, 500000, 1000000, 2000000, 4000000, 8000000,16000000,25000000]
    for test in b:
        print('{} integers test'.format(test))
        #a = randomwalk(test)
        a=[i for i in range(test,0,-1)]
    # a = []
    # fi = open(argv[1], 'r')
    # for line in fi:
    #     num = int(line)
    #     a.append(num)
        samples = 500
        t = Timer("find_min(a)", "from __main__ import find_min, a")
        took = t.timeit(samples)/samples
        print("find_min for {} integers took {:8f} secs".format(len(a), took))