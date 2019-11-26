# running_up.py
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    high_score = max(arr)
    new_arr = [arr[i] for i in range(len(arr)) if (arr[i] < high_score)]
    # print(new_arr)
    print(max(new_arr))
