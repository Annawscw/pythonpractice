
play = "yes"
QUESTION_FORMAT = "{}\na:{}\nb:{}\nc:{}\nd:{}"

# ask the user their name and store it 

name = input ("what is your name?")

# greet user and interduce quiz

print ("Hello welcome to the quizz ", name)

while True: 
    try:

        tries=input("how many trys do you wont for the question")
        tries=int(tries)
        break
    except:
        print("thats nont a number")

        GOOD_COMMENTS = ["good job","keep going","you can do it", ]
        BAD_COMMENTS = ["keep trying", "dont give up","you can do better",]



while play == "yes":
    score = 0 
    # question

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

