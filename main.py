score = 0
QUESTION_FORMAT ="{}\na.{} b.{} c.{} d.{}"

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

# multi question 

question = "what bread of cat is the longest?"
a = "Ragdoll"
b = "Maine Coon"
c = "British Shorthair"
d = "Scottish Fold"
answer = input(QUESTION_FORMAT.format(question,a, b, c, d,)) .lower()
if answer == "b" .lower() or answer == b. lower():

# the end
print ("Goodjob {} you got {} pionts.\ngood-bye" .format(name, score))



