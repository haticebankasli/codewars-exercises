def find_outlier(integers):
    odd = []
    even = []
    for n in integers :
        if n % 2 != 0 :
            odd.append(n)
        else : 
            even.append(n)
    if len(odd) > 1:
        return even[0]
    else :
        return odd[0]
            