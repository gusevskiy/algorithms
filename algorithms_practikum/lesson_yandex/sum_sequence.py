seq = list(map(int, input().split()))
if len(seq) == 0:
    print(0)
else:
    seqsum = seq[0]
    for i in range(1, len(seq)):
        seqsum += seq[i]
    print(seqsum)