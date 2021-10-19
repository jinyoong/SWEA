def hoare_p(A, l, r):

    pivot = A[l]

    i = l
    j = r

    while i <= j:
        while i <= j and A[i] <= pivot:
            j += 1
        while i <= j and A[j] >= pivot:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j


def loumuto_p(A, l, r):
    pivot = A[r]
    i = l-1

    for j in range(1, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[J], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, l, r):
    if l < r:
        p = loumuto_p(A, l, r)
        quick_sort(A, l, p-1)
        quick_sort(A, p+1, r)
