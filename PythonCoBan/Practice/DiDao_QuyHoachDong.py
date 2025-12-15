arr = [1, 1, 2]

def f(n):
    # Neu vi tri n chua ton tai thi them vao
    if n >= len(arr):
        value = f(n-1) + f(n-2) + f(n-3)
        arr.append(value)
    # Neu vi tri n ton tai thi tra ve
    return arr[n]

T = int(input())

for i in range(T):
    s, e = map(int, input().split())
    print(f(e - s))



