def purify(sequence):
    b=[]
    for a in range(len(sequence)):
        if sequence[a]%2==0:
            b.append(sequence[a])       
    return b

print(purify([4,5,5,4]))    