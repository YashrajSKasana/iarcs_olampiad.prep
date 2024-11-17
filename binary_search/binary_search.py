from math import floor
first: bool = True
def binary_search1(num_list: list[tuple[int, int]], num_to_find: int) -> int | str:
    if first:
        if num_list[0][1] == num_to_find: return 0
        first = False
    if len(num_list) == 1: return "not found"
    mid_index = floor(len(num_list)/2)
    mid_item = num_list[mid_index]
    if mid_item[1] == num_to_find: return mid_item[0]
    elif mid_item[1] > num_to_find: return binary_search1(num_list[:mid_index], num_to_find)
    else: return binary_search1(num_list[mid_index:], num_to_find)

def binary_search2(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1  
    while left <= right:  
        mid = left + ((right-left)//2)  
        if arr[mid] == target:
            return mid  
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1  

@lambda _: __name__ == '__main__' and _()
def main() -> None:
    num_list: list[int] = list(map(int, filter(None, input().split(" "))))
    num_to_find: int = int(input())
    print(binary_search2(num_list, num_to_find))