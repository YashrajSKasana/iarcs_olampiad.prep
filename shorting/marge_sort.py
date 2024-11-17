def merge_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr)
    if high - low <= 1:return
    mid = low + ((high-low)//2)
    merge_sort(arr, low, mid)
    merge_sort(arr, mid, high)
    merge_list(arr, low, mid, high)

def merge_list(arr, low, mid, high):
    i, j = low, mid
    rtn_arr = []
    while i<mid and j<high:
        if arr[i] <= arr[j]:
            rtn_arr.append(arr[i])
            i += 1
        else:
            rtn_arr.append(arr[j])
            j += 1
    i<mid and rtn_arr.extend(arr[i:mid])
    j<high and rtn_arr.extend(arr[j:high])
    arr[low:high] = rtn_arr

@lambda _: __name__ == "__main__" and _()
def main():
    arr = list(map(int, input().split(" ")))
    merge_sort(arr)
    print(arr)