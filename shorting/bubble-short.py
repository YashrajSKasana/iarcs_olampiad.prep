def bubble_short(num_list):
    unsorted_list_len = len(num_list)
    while unsorted_list_len > 0:
        for i in range(1,unsorted_list_len):
            pre = num_list[i-1]
            cur = num_list[i]
            if pre > cur:
                num_list[i], num_list[i-1] = pre, cur
        unsorted_list_len -= 1
    return num_list

@lambda _: __name__ == "__main__" and _()
def main():
    num_list = list(map(int, filter(None, input().split(" "))))
    print(bubble_short(num_list))