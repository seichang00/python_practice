# Paste your comment for Q1-Q9 in the variable s
s = " For me: 1.1 Q1a (1.0 pts): 1.0, 1.2 Q1b (2.0 pts): 2.0, 1.3 Q1c (1.0 pts): 0.0, 1.4 Q1d (2.0 pts): 0.0, 1.5 Q1e (1.0 pts): 1.0, 1.6 Q1f (2.0 pts): 2.0, 1.7 Q1g (1.0 pts): 0.0, 2.1 Q2a (3.0 pts): 1.5, 2.2 Q2b (2.0 pts): 2.0, 2.3 Q2c (5.0 pts): 4.0, 3.1 Q3a (1.0 pts): 1.0, 3.2 Q3b1 (2.0 pts): 2.0, 3.3 Q3b2 (2.0 pts): 1.0, 3.4 Q3c (5.0 pts): 3.0, 4 Q4 (10.0 pts): 4.0, 5.1 Q5a (1.0 pts): 1.0, 5.2 Q5b (1.0 pts): 1.0, 5.3 Q5c1 (1.0 pts): 1.0, 5.4 Q5c2 (1.0 pts): 0.0, 5.5 Q5c3 (1.0 pts): 1.0, 5.6 Q5d1 (1.0 pts): 1.0, 5.7 Q5d2 (1.0 pts): 1.0, 5.8 Q5d3 (1.0 pts): 0.0, 5.9 Q5d4 (1.0 pts): 0.0, 5.10 Q5d5 (1.0 pts): 1.0, 6.1 countu.c countl.c (2.0 pts): 0.0, 6.2 makefile (2.0 pts): 1.75, 6.3 main.c (6.0 pts): 1.0, 7.1 Q7a Forking (1.0 pts): 0.25, 7.2 Q7b Cloning (2.0 pts): 2.0, 7.3 Q7c Adding Remotes (2.0 pts): 0.0, 7.4 Q7d Creating a Branch (1.0 pts): 1.0, 7.5 Q7e Merge Conflict Causes (1.0 pts): 0.5, 7.6 Q7f Resolving Merge Conflicts (2.0 pts): 0.0, 7.7 Q7g Rebasing (1.0 pts): 0.0, 8.1 Q8a (2.0 pts): 0.0, 8.2 Q8b (2.0 pts): 2.0, 8.3 Q8c (2.0 pts): 0.0, 8.4 Q8d (2.0 pts): 0.0, 8.5 Q8e (2.0 pts): 2.0, 9.1 Q9a1 (1.0 pts): 0.0, 9.2 Q9a2 (1.0 pts): 0.5, 9.3 Q9a3 (2.0 pts): 0.0, 9.4 Q9b (1.0 pts): 0.0, 9.5 Q9c (1.0 pts): 0.0, 9.6 Q9d (2.0 pts): 2.0, 9.7 Q9e (2.0 pts): 0.0,"

def calc_score(s):
    score = 0
    for i in range(len(s)):
        if s[i] == ",":
            temp = s[i-4:i]
            if temp[0] == " ":
                temp = temp[1:]
            temp = float(temp)
            score += temp
    return score

inds = [-1 for i in range(9)]
ind = 1
for i in range(len(s)):
    if s[i:i+3] == str(ind)+".1" or s[i:i+2] == "Q" + str(ind):
        inds[ind-1] = i
        ind += 1
inds.append(len(s))

comments = ["" for i in range(9)]
for i in range(9):
    comments[i] = s[inds[i]:inds[i+1]]

scores = [0 for i in range(9)]

for i in range(9):
    scores[i] = calc_score(comments[i])
print("CS35L Final Score Q1-9: "+str(sum(scores)))
print("Break up:")
print(scores)