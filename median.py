def median(seq):
    #float med=0
    seq=sorted(seq)
    if (len(seq)%2!=0):
        med=seq[(int(len(seq)/2))]
    else:
        med=seq[(int(len(seq)/2))]+seq[int((len(seq)/2)-1)]
        print (med)
        med=med/2
    return med


print(median([4,5,5,4]))