def quick_short(arr, low=0, high=None):
    if high is None:
        high = len(arr) -1
    if high - low <= 1:return

    swap = low-1
    for cur in range(low,high):
        if arr[cur] <= arr[high]:
            swap += 1
            if cur > swap:
                arr[cur], arr[swap] = arr[swap], arr[cur]
    arr[swap +1], arr[high] = arr[high], arr[swap +1]
    
    quick_short(arr, low, swap)
    quick_short(arr, swap+2, high)

@lambda _:__name__ == "__main__" and _()
def main():
    arr = list(map(int, input().split(" ")))
    quick_short(arr)
    print(arr)