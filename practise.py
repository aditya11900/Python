import numpy as np

scores = np.empty((4, 5), dtype=float)

for subject in range(4):
    for student in range(5):
        score = float(input(f"Enter the score for Subject {subject + 1}, Student {student + 1}: "))
        scores[subject, student] = score
        
studentAvg = np.mean(scores, axis=0)
print(studentAvg)
studentAvg = np.reshape(studentAvg, (1, 5))
scores = np.append(scores, studentAvg, axis=1)

print(scores)
