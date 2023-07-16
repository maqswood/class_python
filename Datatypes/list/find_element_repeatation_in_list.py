arr = [1, 2, 3, 7, 4, 5, 6, 7, 4, 8]
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            print("repeated value", arr[j])
