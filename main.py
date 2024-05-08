score = 0
# ask the user their name and store it 
name = input ("what is your name?")
# greet user and interduce quiz
print ("Hello welcome to the quizz ", name)

# ask the user a question and get their response
answer = input ("do you think cats are cute?") .lower() 
# Tell them the correct answer
if answer == "yes" .lower(): 
    print("Correct")
    score += 5
elif answer == "":
    print ("correct")
else :
    print("Incorrect!")
    print ("The answer was correct")

# a question 
answer = input (" In 1963 did a cat go to space? ") .lower()
# answer to the question
if answer == "yes" .lower() :
    print("Correct")
    score += 5
elif answer == "":
    print ("correct")
else :
    print("Incorrect!")
    print ("The answer was correct")
# the end
print ("Goodjob {} got {} pionts.\ngood-bye" .format(name, score))

