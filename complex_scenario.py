# code snippet (from Kalshi_client)
while True:
    if break_outer is False:
        try:
            market_choice = int(input("Please choose a market:\n(1) for Nasdaq100(QQQ)\n(2) for S&P500(SPY)\nYour choice here: "))

            if 2 < market_choice < 1:  # user enters number that's not 1 or 2
                print()  # style
                print("Please enter 1 for Nasdaq100 market or 2 for S&P500 market.")
                continue

            elif market_choice == 1:  # user chooses 1 for Nasdaq100
                # ######################################--- "Market choice pattern" ---################################
                # ########################################\\\ (Repeat for S&P500) \\\##################################
                print()  # style
                print("You chose the Nasdaq100.")
                print()  # style
                while True:
                    if break_mid is False:
                        try:
                            event_type = int(input("Please choose your Nasdaq100 Event...\n(1) for 'Daily Bracket'\n(2) for 'Daily Up/Down'\n(3) for 'Weekly'\n(4) for 'Monthly'\n(5) for 'End of Year'\nYour choice here: "))

                            if 1 > event_type > 5:  # User did not type a number between 1-5
                                print()  # style
                                print("Please enter an integer value between 1 and 5.")
                                print()  # style
                                continue
                            elif event_type == 1:
                                print()  # style
                                print("---Daily Bracket---")
                                print()  # style
                                while True:
                                    event_date = input("Please enter the year/month/day (of the daily bracket you want to work with) in this exact format...\nYY/MON/DD\nExample: 23/DEC/10\n*If you do not enter the year/month/day in the exact format mentioned, the program will break and you will have to start over.\n*If you choose a date on which the market is not open for trading, the program will break and you will have to start over.\nYou enter here: ")
                                    # Remove "/" characters from the user input
                                    event_date = event_date.replace("/", "")
                                    print(event_date)  # comment out when not testing
                                    break_mid = True
                                    break
                            # elif choice is 2:
                                # do stuff
                                # another possible 'while True:'
                                    # possibly more choices (to get specific event ticker narrowed down (because the DATE changes))
                                    # another break
                            # elif choice is 3:
                                # do stuff
                                # another possible 'while True:'
                                    # possibly more choices (to get specific event ticker narrowed down (because the DATE changes))
                                    # another break
                            # elif choice is 4:
                                # do stuff
                                # another possible 'while True:'
                                    # possibly more choices (to get specific event ticker narrowed down (because the DATE changes))
                                    # another break
                            # elif choice is 5:
                                # do stuff
                                # another possible 'while True:'
                                    # possibly more choices (to get specific event ticker narrowed down (because the DATE changes))
                                    # another break
                        except ValueError:  # User did not type an integer
                            print()  # style
                            print("Invalid entry. Please type in a valid integer.")
                            print()  # style
                    else:
                        break_outer = True
                        break
