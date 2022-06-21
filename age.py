import time
import random
from datetime import datetime
import trial

def open_message():
    first_message = "\tWelcome dearest"
    second_message = "\tGreetings bretheren"
    third_message = "\tHello there"
    fourth_message = "\tWarm welcome"
    welcome_message = [first_message, second_message, third_message, fourth_message]
    print(random.choice(welcome_message), 'and', trial.greetings)
    time.sleep(0.5)
    print()

def main_body():
    date_today = time.strftime("%D")
    day = time.strftime("%A")
    time_now = time.strftime("%I:%M %p")
    deciding_time = int(time.strftime("%M"))
    next_time = deciding_time + 1
    hour_now = time.strftime("%I : ")
    meridian = time.strftime("%p")


    odd_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37,
            39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
    if deciding_time in odd_list:
        print("The time is",time_now, "This program only runs when the minutes are even numbers.")
        time.sleep(0.5)
        print("Run the program again at", hour_now, next_time, meridian)
        time.sleep(3)
    else:
        print('\t Three attempt(s).')
        password = input("Enter the password: ")
        time.sleep(0.5)
        if password.upper() == "KKWILSOWN1431":
            print()
            print("Date: ",date_today, "\t Day: ", day)
            print("Time: ", time_now)
            print()
            name = input("Enter your full name: ")
            name_list = list(name) 
            space_index = name_list.index(" ")
            first_name = name_list[0:space_index:1]
            time.sleep(0.5)
            
            try:
                age = int(input("How old are you? "))
                year_of_birth = 2022 - age
                time.sleep(0.5)
            except:
                print()
                print("Enter numbers only !")
                try:
                    age = int(input("How old are you? "))
                    year_of_birth = 2022 - age
                    time.sleep(0.5)
                except:
                    print()
                    print("Enter numbers only!")
                    age = int(input("How old are you? "))
                    year_of_birth = 2022 - age
                    time.sleep(0.5)

            sex = input("What sex are you? ")
            if sex.upper() == "MALE":
                prefix = "Mr"
            else:
                prefix = "Mrs"
            time.sleep(2)
            print()
            print(prefix,"".join(first_name), "you were born in the year", year_of_birth)
            time.sleep(1)
            print()

            question = input("Whana play a number guessing game? ")
            if question.upper() == "YES":
                print("\t lets get started!")
                time.sleep(0.5)
                print("Only three attempt(s).")
                
                random_number = random.randint(0,5)
                time.sleep(0.5)
                number_guessed = int(input("Guess a number between 0 and 5 that am thinking about: "))
            
                if number_guessed == random_number:
                    print("\t Oh, you guessed it!")
                    time.sleep(0.5)
                else:
                    print("Incorrect! Guess again.")
                    time.sleep(0.5)
                    print('Two attempt(s) remaining')
                    print()
                    time.sleep(0.5)
                    number_guessed = input("Guess a number between 0 and 5 that am thinking about: ")
                    time.sleep(0.5)

                    if number_guessed == random_number:
                        print("\t oh, you guessed it!")
                    else:
                        print("""Incorrect! Guess again.
                        One attempt(s) remaining.""")
                        print()
                        time.sleep(0.5)
                        number_guessed = input('Guess a number between 0 and 5 that am thinking about: ')
                        time.sleep(0.5)
                        if number_guessed == random_number:
                            print('\t oh, you have guessed it!')
                        else:
                            print("""Incorrect! You have failed three times.""")
                            time.sleep(0.5)

            else:
                print()
                time.sleep(0.5)
                print(''.join(first_name),"you don't have to always be so tough.")
                time.sleep(0.5)
        else:
            print("You have entered and incorrect password.")
            print('\t Two attempt(s) remaining.')
            print()
            password = input("Enter the correct password: ")
            if password.upper() == "KKWILSOWN1431":
                print()
                print("Date: ",date_today, "\t Day: ", day)
                print("Time: ", time_now)
                print()
                name = input("Enter your full name: ")
                name_list = list(name)
                space_index = name_list.index(" ")
                first_name = name_list[0:space_index:1]
                time.sleep(0.5)
                
                try:
                    age = int(input("How old are you? "))
                    year_of_birth = 2022 - age
                    time.sleep(0.5)
                except:
                    print()
                    print("Enter numbers only !")
                    try:
                        age = int(input("How old are you? "))
                        year_of_birth = 2022 - age
                        time.sleep(0.5)
                    except:
                        print()
                        print("Enter numbers only !")
                        age = int(input("How old are you? "))

                sex = input("What sex are you? ")
                if sex.upper() == "MALE":
                    prefix = "Mr"
                else:
                    prefix = "Mrs"
                time.sleep(2)
                print()
                print(prefix, "".join(first_name), "you were born in the year", year_of_birth)
                print()

                question = input("Whana play a number guessing game? ")
                if question.upper() == "YES":
                    print("\t lets get started!")
                    time.sleep(0.5)
                    print("Only three attempt(s).")
                    print()
                    
                    random_number = random.randint(0,5)
                    time.sleep(0.5)
                    number_guessed = int(input("Guess a number between 0 and 5 that am thinking about: "))
                    print()
                
                    if number_guessed == random_number:
                        print("\t Oh, you guessed it!")
                        time.sleep(0.5)
                    else:
                        print("Incorrect! Guess again.")
                        print()
                        time.sleep(0.5)
                        print('Two attempt(s) remaining')
                        print()
                        time.sleep(0.5)
                        number_guessed = input("Guess a number between 0 and 5 that am thinking about: ")
                        print()
                        time.sleep(0.5)

                        if number_guessed == random_number:
                            print("\t oh, you guessed it!")
                        else:
                            print("""Incorrect! Guess again.
                            One attempt(s) remaining.""")
                            print()
                            time.sleep(0.5)
                            number_guessed = input('Guess a number between 0 and 5 that am thinking about: ')
                            time.sleep(0.5)
                            if number_guessed == random_number:
                                print('\t oh, you have guessed it!')
                            else:
                                print("""Incorrect! You have failed three times.""")
                                print()
                                time.sleep(0.5)
                                print()
                else:
                    print()
                    time.sleep(0.5)
                    print(''.join(first_name),"you don't have to always be so tough.")
                    time.sleep(0.5)

            else:
                print()
                print("You have entered an incorrect password.")
                print('\t One attempt(s) remaining.')
                print()

                password = input("Enter the correct password: ")
                if password.upper() == "KKWILSOWN1431":
                    print()
                    print("Date: ",date_today, "\t Day: ", day)
                    print("Time: ", time_now)
                    print()
                    name = input("Enter your full name: ")
                    name_list = list(name)
                    space_index = name_list.index(" ")
                    first_name = name_list[0:space_index:1]
                    time.sleep(0.5)
                    
                    try:
                        age = int(input("How old are you? "))
                        year_of_birth = 2022 - age
                        time.sleep(0.5)
                    except:
                        print()
                        print("Enter numbers only !")
                        try:
                            age = int(input("How old are you? "))
                            year_of_birth = 2022 - age
                            time.sleep(0.5)
                        except:
                            print()
                            print("Enter numbers only !")
                            age = int(input("How old are you? "))

                    sex = input("What sex are you? ")
                    if sex.upper() == "MALE":
                        prefix = "Mr"
                    else:
                        prefix = "Mrs"
                    time.sleep(2)
                    print()
                    print(prefix, "".join(first_name), "you were born in the year", year_of_birth)
                    print()

                    question = input("Whana play a number guessing game? ")
                    if question.upper() == "YES":
                        print("\t lets get started!")
                        time.sleep(0.5)
                        print("Only three attempt(s).")
                        print()
                        
                        random_number = random.randint(0,5)
                        time.sleep(0.5)
                        number_guessed = int(input("Guess a number between 0 and 5 that am thinking about: "))
                        print()
                    
                        if number_guessed == random_number:
                            print("\t Oh, you guessed it!")
                            time.sleep(0.5)
                        else:
                            print("Incorrect! Guess again.")
                            print()
                            time.sleep(0.5)
                            print('Two attempt(s) remaining')
                            print()
                            time.sleep(0.5)
                            number_guessed = input("Guess a number between 0 and 5 that am thinking about: ")
                            print()
                            time.sleep(0.5)

                            if number_guessed == random_number:
                                print("\t oh, you guessed it!")
                            else:
                                print("""Incorrect! Guess again.
                                One attempt(s) remaining.""")
                                print()
                                time.sleep(0.5)
                                number_guessed = input('Guess a number between 0 and 5 that am thinking about: ')
                                time.sleep(0.5)
                                if number_guessed == random_number:
                                    print('\t oh, you have guessed it!')
                                else:
                                    print("""Incorrect! You have failed three times.""")
                                    print()
                                    time.sleep(0.5)
                    else:
                        print()
                        time.sleep(0.5)
                        print(''.join(first_name),"you don't have to always be so tough.")
                        time.sleep(0.5)


def count_down():
    print()   
    time.sleep(2)       
    print("\t COUNT DOWN TO AISEC BUSINESS MENTORSHIP.")
    days = datetime.today().day
    hours = datetime.today().hour
    minutes = datetime.today().minute
    seconds = datetime.today().second

    days_remain = 24 - days
    hours_remain = 24 - hours
    minutes_remain = 59 - minutes
    seconds_remain = 59 - seconds

    while days < 24:
        print("Days: ", days_remain, "\t Hours: ",hours_remain, "\t Minutes: ",minutes_remain, "\t Seconds: ", seconds_remain)
        print()
        time.sleep(1)

        days = datetime.today().day
        hours = datetime.today().hour
        minutes = datetime.today().minute
        seconds = datetime.today().second

        days_remain = 24 - days
        hours_remain = 24 - hours
        minutes_remain = 59 - minutes
        seconds_remain = 59 - seconds

def final_fun():
    open_message()
    main_body()
    count_down()


final_fun()







