score = []
for i in range(1,6):
    scor = int(input(f"Enter your score for quiz {i}: "))
    score.append(scor)

print("===QUIZ SCORE REPORT===")
print(f"Quiz scores: {score}")
print(f"Number of quizzes: {len(score)}")
print(f"Total score: {sum(score)}")
print(f"Average score: {sum(score)/len(score):.2f}")
print(f"Ascending score: {sorted(score)}")
print(f"Descending score: {sorted(score,reverse=True)}")
print(f"Original score: {max(score)}")


