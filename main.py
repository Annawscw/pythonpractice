score = 0
# ask the user their name and store it 
name = input ("what is your name?")
# greet user and interduce quiz
print ("Hello welcome to the quizz ", name)

# ask the user a question and get their response
answer = input ("do you think cats are cute?")
# Tell them the correct answer
print ("The correct answer is ", answer)

# a question 
answer = input (" In 1963 did a cat go to space? ")
# answer to the question
if answer == "Correct":
    print("Correct")
    score += 5
elif answer == "":
    print ("I don't know")
else :
    print("Incorrect!")
    print ("The answer was correct")
# the end
print ("Goodjob you got ", score, "pionts" "goodbye")

