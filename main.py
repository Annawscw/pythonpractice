import random 

QUESTION_FORMAT = "{}\na:{}\nb:{}\nc:{}\nd:{}"

GOOD_COMMENTS = ["good job","keep going","you can do it", ]
BAD_COMMENTS = ["keep trying", "dont give up","you can do better",]

QUESTIONS = ["do you think cats are cute?",
            "In 1963 did a cat go to space?",
            "what bread of cat is the longest?",]
OPTIONS = [["yes", "no"]
           ["yes","no"]
           ["Ragdoll","Maine Coon","British Shorthair","Scottish Fold"]]
ANSWERS = [1,1,2]

play = "yes"

name = input ("what is your name?")

print ("Hello welcome to the quizz ", name)

while True: 
    try:
        tries=input("how many trys do you wont for the question")
        tries=int(tries)
        break
    except:
        print("thats not a number")

while play == "yes":
    score = 0 
    # question

    for i in range (len(question)):
        question_attempts = tries
        while question_attempts > 0:
            answer = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0], OPTIONS[i][1], OPTIONS [i][2],OPTIONS [i][3])).lower()

            











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
        print(random.choice(GOOD_COMMENTS[0]))
    elif answer == "wrong":
        print ("correct")
        print(random.choice(BAD_COMMENTS[0]))
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
    if answer == "b" .lower() or answer == b.lower():
        print("correct")
    score += 5
    if answer == "yes" .lower():
        print("Correct")
        score += 5
    elif answer == "":
        print ("correct")
    else :
        print("Incorrect!")
        print ("The answer was correct")

    # the end

    play = input("you got {} points do you want to play again?".format(score ))

