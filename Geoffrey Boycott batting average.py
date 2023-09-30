#In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
#times, was not out 162 times, and scored 48426 runs. Write a program to calculate
#and display Boycott's batting average
#batting average = number of runs/number of completed innings
#completed innings = total times batted - times not out
#geoffrey boycott played 609 matches, batted 1014 times, was not out 162 times and scored 48426 runs.

#need to calculate completed innings
compInn = 1014-162
battAv = 48426/compInn
avRounded = round(battAv, 2)
print("Geoffrey Boycott played 609 matches, batting 1014 times, being not out 142 times and scoring 48426 runs, this results in a batting average of",battAv,"which can be rounded to",avRounded)
 