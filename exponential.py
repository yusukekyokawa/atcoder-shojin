X = int(input())

max_ = [1]
for b in range(X):
    for p in range(2,   X//2):
        if b**p <=X:
            max_.append(b**p)
        
print(max(max_))