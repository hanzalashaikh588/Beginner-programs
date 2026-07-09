def main_program():
    name = input("enter your name : ")
    print("hello welcome to the game who wants to be a millionaire", name)
    print("today you will be asked 3 questions for a chance to win 1 million dollars!\n but remember if you get a question wrong you lose it all", name)

    print("who lost the fifa worldcup in 2018?")
    print(["brazil", "argentina", "france", "croatia"])
    correctans = "croatia"
    answer1 = input("enter your option : ").strip().lower()
    if answer1 == correctans:
        print("that is correct!")
    else:
        print("that is unfortunately incorrect")
        restart = input("would you like to retry?(yes/no) : ").strip().lower()
        if restart == 'yes':
            return True
        else:
            print("goodbye")
            return False

    print("Now for the 2nd question you may use a lifeline. but remember you only have 1 lifeline")
    print("What is the capital of Russia")
    print(["petersburg", "moscow", "poland", "czech"])
    correctans2 = "moscow"
    lifeline = input("do you want to use your lifeline? (yes/no) : ").strip().lower()
    if lifeline == 'yes':
        print("the correct ans is either moscow or petersburg")
    else:
        print("okay you can carry on")
    ans2 = input("enter your answer : ").strip().lower()
    if ans2 == correctans2:
        print("that is correct")
    else:
        print("that's wrong too bad")
        retry = input("would you like to retry?(yes/no) : ").strip().lower()
        if retry == 'yes':
            return True
        else:
            print("goodbye")
            return False

    print("Now for the 3rd question")
    print("What is the largest planet in our solar system?")
    print(["earth", "mars", "jupiter", "venus"])
    correctans3 = "jupiter"
    ans3 = input("enter your answer : ").strip().lower()
    if ans3 == correctans3:
        print("congratulations, you won 1 million dollars!")
    else:
        print("that's incorrect, you lose it all")
        retry = input("would you like to retry?(yes/no) : ").strip().lower()
        if retry == 'yes':
            return True
        else:
            print("goodbye")
            return False
while True:
    should_restart=main_program()
    if not should_restart:
        break

main_program()




            
