
scores = [-0.1, 1, -0.1, -0.1, -0.1]

best = -1
for i, score in enumerate(scores):
    if score > best:
        best = score
        bestIndex = i

print(bestIndex)