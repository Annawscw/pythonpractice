TOP_ANIMALS_GOING_ENDANGERED = ["Avan Rhinos","Amur leopard","Sunda island tiger","mountain gorila","Tapanuli orangutan",
                                "Yangtze Finless Porpoise","Black rhinos","African forest elephants","Sumatran orangutan","Hawksbill turtle",]
score = 0
while 

#---------FUNCTIONS--------#

def intro():
    name = input ("what is your name?")
    print("Welcome to the quiz", name)

#-------password----
def getpassword ():
    while True:
        password = input("what is the password?")
        if password == "cat":
            return
        else :
            print("thats not right")
#-------------how many lives--------
def getlives():
    while True:
        live = input("how many lives do you want?")
        try:
            lives = int(live)
            if lives >= 0:
                return lives
            else: 
                print("Do a even number please")
        except:
            print("thats not a number") 

#---------MAIN CODE--------#

intro()
getpassword
