
def convolution_1d(x, w, b=0.0):
    ## n la len(x)
    n = len(x)

    ## k la len(w)
    k = len(w)

    if k > n:
        return []

    ## Tinh toan
    result = [0.0 for _ in range(n - k + 1)]
    for i in range(n - k + 1):
        for j in range(k):
            # print(f"w-{w[j]}, x-{x[i+j]}")
            result[i] += w[j] * x[i+j]

        result[i] = round(result[i] + b, 2)
    return result

x = [1,2,3,4,5]
w = [0.2, 0.5, 0.8]
b = 1.0
print(convolution_1d(x, w, b))
