def count(sequence,item):
    count=0
    for a in sequence:
        if a==item:
            count+=1 
    return count

print(count([1, 2, 1, 1], 1))