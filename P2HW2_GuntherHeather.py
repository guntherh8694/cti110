#CTI-110
#P2HW2 - Score Avg
#Heather Gunther
#2/25/2022
#

score_1 = float(input('Enter score #1: '))
score_2 = float(input('Enter score #2: '))
score_3 = float(input('Enter score #3: '))
score_4 = float(input('Enter score #4: '))
score_5 = float(input('Enter score #5: '))
score_6 = float(input('Enter score #6: '))
score_7 = float(input('Enter score #7: '))

score_series = [score_1, score_2, score_3, score_4, score_5, score_6, score_7]

print('-------Results-------')

lowest_score = min(score_series)
score_series.remove(lowest_score)

print('Lowest Score:', lowest_score)

print('Modified list:', score_series)

score_avg = sum(score_series)/ len(score_series)

print('Scores Average: ', score_avg)

#Create input commands for scores 1 - 7
#Create and mame a list to save the scores in
#use min method to determine the lowest score
#Then use the remove method to update the list
#Then create commands to print the results for
   #the lowest score, the modified list, and average score.

