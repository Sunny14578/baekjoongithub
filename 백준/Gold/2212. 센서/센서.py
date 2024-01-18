import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

arr = list(map(int, input().split()))

arr.sort()
length = []

for i in range(len(arr)-1):
    length.append(arr[i+1] - arr[i])
    
length.sort()

print(sum(length[:n-k]))