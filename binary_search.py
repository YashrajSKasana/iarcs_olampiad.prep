from math import floor

def binary_search(num_list: list[int] | list[tuple[int, int]], num_to_find: int) -> int | str:
    if type(num_list[0]) is int:
        if num_list[0] == num_to_find: return 0
        num_list = list(enumerate(num_list))
    if len(num_list) == 1: return "not found"
    mid_index = floor(len(num_list)/2)
    mid_item = num_list[mid_index]
    if mid_item[1] == num_to_find: return mid_item[0]
    elif mid_item[1] > num_to_find: return binary_search(num_list[:mid_index], num_to_find)
    else: return binary_search(num_list[mid_index:], num_to_find)

@lambda _: __name__ == '__main__' and _()
def main() -> None:
    num_list: list[int] = list(map(int, filter(None, input().split(" "))))
    num_to_find: int = int(input())
    print(binary_search(num_list, num_to_find))