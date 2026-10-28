def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# 示例
arr = [2, 3, 4, 10, 40]
x = 10
print(linear_search(arr, x))

