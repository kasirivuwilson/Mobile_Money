from select import select
import time

print('\t welcome to airtel money services.'.upper())
print()
time.sleep(1)

your_phone_number = input('Enter your phone number please: ')
code = input('Enter mobile money code: ')
code_list = list(code)
space = ' ' in code_list

while space == True:
    code_list.remove(" ")
    space = " " in code_list

if "".join(code_list) == '*185#':
    time.sleep(1)
    print()
    print("""
    1.Send Money
    2.Airtime/Bundles
    3.Withdraw cash
    4.Pay Bill
    5.Payments
    6.School Fees
    7.Financial services
    8.Wewole
    9.AirtelMoney Pay
    10.My account

                 Cancel  SEND
    """)

    first_qn = input('')
    if first_qn == '1':
        print("""
        Send Money
        1.Airtel and other number
        2.MTN number
        3.UTL Number
        4.International Transfer
        
        0.Back 00.Main Menu""")
        send_money = input(' ')
        if send_money == '1':
            print("""
            Enter Mobile Number

            0.Back 00.Main Menu
            """)
            mobile_number = input(' ')
            print("""
            Enter Amount

            0.Back 00.Main Menu
            """)
            mobile_number_amount = input(' ')
            print(f"""
            Sending {mobile_number_amount} to {mobile_number}
            Confirm with your PIN

            0.Back 00.Main Menu
            """)
            pin = input(' ')
            print("""
            Transaction in progress.
            """)

        elif send_money == '2':
            print("""
            Send Money
            Enter MTN Number

            0.Back 00.Main Menu
            """)
            mobile_number = input(' ')
            print("""
            Enter Amount

            0.Back 00.Main Menu
            """)
            mobile_number_amount = input(' ')
            print(f"""
            Sending {int(mobile_number_amount)} to {mobile_number}
            Confirm with your PIN

            0.Back 00.Main Menu
            """)
            pin = input(' ')
            print("""
            Transaction in progress.
            """)


        elif send_money == '3':
            print("""
            Enter UTL Customer Number

            0.Back 00.Main Menu
            """)
            mobile_number = input(' ')
            print("""
            Enter Amount

            0.Back 00.Main Menu
            """)
            mobile_number_amount = input(' ')
            print(f"""
            Sending {int(mobile_number_amount)} to {mobile_number}
            Confirm with your PIN

            0.Back 00.Main Menu
            """)
            pin = input(' ')
            print("""
            Transaction in progress.
            """)

        elif send_money == '4':
            print("""
            1.Rwanda
            2.Zambia
            3.Tanzania
            4.Malawi
            5.Burundi
            6.Zimbabwe
            7.Ethiopia
            8.Botswana
            9.Kenya
            10.DRC
            11.South Sudan
            12.Congo B
            13.Ghana
            14.CHINA

            0.Back 00.Main Menu
            """)
            country_transfer = input(' ')
            if country_transfer == '1':
                print("""
                1.Airtel
                2.MTN Mobile Money

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter Rwanda number

                    0.Back 00.Main Menu
                    """)
                    rwanda_number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount_to_send = input(' ')
                    print(f"""
                    Sending {amount_to_send} to {rwanda_number}
                    Confirm with your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)

                elif selection == '2':
                    print("""
                    Enter MTN Number

                    0.Back 00.Main Menu
                    """)
                    mtn_number = input(' ')
                    print("""
                    Enter amount in UGX

                    0.Back 00.Main Menu
                    """)
                    amount_to_send = input(' ')
                    print(f"""
                    Sending {amount_to_send} to {mtn_number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                else:
                    print("Invalid selection.")

            elif country_transfer == '2':
                print("""
                1.Airtel
                2.MTN

                0.Back 00.Main Menu
                """)
                service_provider = input(' ')
                if service_provider == '1':
                    print("""
                    Enter Zambia number

                    0.Back 00.Main Menu
                    """)
                    zambia_number = input(' ')
                    print("""
                    Enter amount to send

                    0.Back 00.Main Menu
                    """)
                    amount_to_send = input(' ')
                    print(f"""
                    Sending {amount_to_send} to {zambia_number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)

                elif service_provider == '2':
                    print("""
                    Enter MTN Number

                    0.Back 00.Main Menu
                    """)
                    
                else:
                    print('Invalid selection.')
            elif country_transfer == '3':
                print("""
                1.Airtel
                2.Mpesa
                3.Tigo Pesa

                0.Back 00.Main Menu
                """)
                service_provider = input(' ')
                if service_provider == '1':
                    print("""
                    Enter Tanzanian number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                elif service_provider == '2':
                    print("""
                    Enter Mpesa Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                elif service_provider == '3':
                    print("""
                    Enter Tigo Pesa Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                else:
                    print('Invalid selection.')

            elif country_transfer == '4':
                print("""
                1.Airtel
                2.TNM

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter Malawi number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                elif selection == '2':
                    print("""
                    Enter TNM Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX
                    
                    0.Back 00. Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                else:
                    print('Invalid selection.')
            elif country_transfer == '5':
                print("""
                1.EcoCash
                
                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter EcoCash Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                else:
                    print('Invalid selection.')
            elif country_transfer == '6':
                print("""
                1.EcoCash

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter EcoCash Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """) 
                else:
                    print('Invalid selection.')
            elif country_transfer == '7':
                print("""
                1.HelloCash

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter Hellocash Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """) 
                else:
                    print('Invalid selection.')

            elif country_transfer == '8':
                print("""
                1.Orange Money

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter Orange Money Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """) 
                else:
                    print('Invalid selection.')

            elif country_transfer == '9':
                print("""
                1.Safaricom MPESA
                2.Airtel Kenya

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter MPESA Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                elif selection == '2':
                    print("""
                    Enter Airtel Kenya Number(Without Country Code)
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """) 
                else:
                    print('Invalid selection.')

            elif country_transfer == '10':
                print("""
                1.Airtel
                2.Orange
                3.Illico

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter Airtel Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                elif selection == '2':
                    print("""
                    Enter Orange Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """) 
                elif selection == '3':
                    print("""
                    Enter Illico Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """) 
                else:
                    print('Invalid selection.')

            elif country_transfer == '11':
                print("""
                1.MGurush
                2.NilePay

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter MGurush Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                elif selection == '2':
                    print("""
                    Enter NilePay Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """) 
                else:
                    print('Invalid selection.')

            elif country_transfer == '12':
                print("""
                1.MTN Mobile Money

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter MTN Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """) 
                else:
                    print('Invalid selection.')

            elif country_transfer == '13':
                print("""
                1.MTN Mobile Money

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter MTN Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """)
                else:
                    print('Invalid selection.')

            elif country_transfer == '14':
                print("""
                1.Alipay Wallet china

                0.Back 00.Main Menu
                """)
                selection = input(' ')
                if selection == '1':
                    print("""
                    Enter Alipay Number

                    0.Back 00.Main Menu
                    """)
                    number = input(' ')
                    print("""
                    Enter amount to send in UGX

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print(f"""
                    Sending {amount} to {number}
                    Confirm your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    Transaction in progress.
                    """) 
                else:
                    print('Invalid selection.')
            else:
                print('Invalid selection.')
        else:
            print('Invalid selection.')
    elif first_qn == '2':
        print("""
        Airtime / Bundles
        1.Buy Airtime
        2.Buy Data Bundles(Offers Inside)
        3.Buy Voice Bundles
        4.IControl

        0.Back 00.Main Menu
        """)
        selection = input(' ')
        if selection == '1':
            print("""
            Buy Airtime 
            1.For Myself
            2.For Another Number

            0.Back 00.Main Menu
            """)
            more_selection = input(' ')
            if more_selection == '1':
                print("""
                Enter Amount

                0.Back 00.Main Menu
                """)
                amount = input(' ')
                print(f"""
                Airtime Top of UGX {amount} for {your_phone_number}.
                Confirm with your PIN

                0.Back 00.Main Menu
                """)
                pin = input(' ')
                print("""
                Transaction in progress.
                """)
            elif selection == '2':
                print("""
                Enter Mobile Number

                0.Back 00.Main Menu
                """)
                number = input(' ')
                print("""
                Enter Amount

                0.Back 00.Main Menu
                """)
                amount = input(' ')
                print("""
                Airtime Top up of UGX {amount} for ABEJA AGATHA  {number}.
                Confirm with your PIN

                0.Back 00.Main Menu
                """)
                pin = input(' ')
                print("""
                Transaction in progress.
                """)
            else:
                print('Invalid selection.')
        elif selection == '2':
            print("""
            Data Bundles 
            1.Buy for Self
            2.Buy for Another

            0.Back 00.Main Menu
            """)
            more_selection = input(' ')
            if more_selection == '1':
                print("""
                1 Daily
                2 Weekly
                3 Monthly
                4 TV Bundles
                5 Chillax Bundles
                6 Roaming Data
                * Back
                """)
                further_selection = input(' ')
                if further_selection == '1':
                    print("""
                    1 500/- for 80MB
                    2 1000/- for 180MB
                    3 2000/- for 400MB
                    4 5000/- for 2GB
                    5 250/- for 30MB
                    6 11500/- for 4GB (3Days)
                    7 7500/- for 2GB (3Days)
                    8 Night 2GB @ 2K
                    n next
                    * Back
                    """)
                    data_selection = input(' ')
                    if data_selection == '1':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '2':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '3':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '4':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '5':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '6':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '7':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '8':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == 'n':
                        print("""
                        9 Night 5GB @ 4K
                        0 Prev
                        * Back
                        """)
                        select_then = input(' ')
                        if select_then == '9':
                            print("""
                            Enter PIN
                            """)
                        elif select_then == '0':
                            print("""
                            1 500/- for 80MB
                            2 1000/- for 180MB
                            3 2000/- for 400MB
                            4 5000/- for 2GB
                            5 250/- for 30MB
                            6 11500/- for 4GB (3Days)
                            7 7500/- for 2GB (3Days)
                            8 Night 2GB @ 2K
                            n next
                            * Back
                            """)
                            data_selection = input(' ')
                        else:
                            print('Invalid selection.')
                    elif data_selection == '*':
                        print("""
                        1 Daily
                        2 Weekly
                        3 Monthly
                        4 TV Bundles
                        5 Chillax Bundles
                        6 Roaming Data
                        * Back
                        """)
                        further_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif further_selection == '2':
                    print("""
                    1 5000/- for 1.5GB
                    2 10000/- for 3GB
                    3 15000/- for 5.5GB
                    4 22500/- for 9GB
                    * Back
                    """)
                    then_select = input(' ')
                    if then_select == '1':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '2':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '3':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '4':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '*':
                        print("""
                        1 Daily
                        2 Weekly
                        3 Monthly
                        4 TV Bundles
                        5 Chillax Bundles
                        6 Roaming Data
                        * Back
                        """)
                        further_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif further_selection == '3':
                    print("""
                    1 10000/- for 2.5GB
                    2 15000/- for 5GB
                    3 30000/- for 12GB
                    4 50000/- for 22GB
                    5 100000/- for 50GB
                    6 150000/- for 81GB
                    * Back
                    """)
                    then_select = input(' ')
                    if then_select == '1':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '2':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '3':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '4':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '5':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '6':
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '*':
                        print("""
                        1 Daily
                        2 Weekly
                        3 Monthly
                        4 TV Bundles
                        5 Chillax Bundles
                        6 Roaming Data
                        * Back
                        """)
                        further_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif further_selection == '4':
                    print("""
                    1 Airtel TV Bundles
                    2 DSTV Bundles
                    3 Afro Media Bundles
                    * Back
                    """)


    elif first_qn == '3':
        print("""
        Enter amount

        0.Back 00.Main Menu
        """)
    elif first_qn == '4':
        print("""
        Pay Bill
        1.UMEME TouchPay
        2.Water
        3.Pay TV
        4.Pay Solar
        5.UEDCL
        6.KCCA
        7.URA
        8.Airtel Business
        9.Others
        10.Next

        0.Back 00.Main Menu
        """)
    elif first_qn == '5':
        print("""
        Payments
        1.PayEasy
        2.Multiplex
        3.BETTING and GAMING
        4.Uganda Cranes
        5.Kabaka Run
        6.UNEB
        7.Mobipay
        8.YETU
        9.WEZIMBE
        10.Religious Institution
        11.Liquid Telecom
        12.Platinum
        n Next
        """)
    elif first_qn == '6':
        print("""
        School Fees
        1.Bridge Schools
        2.School Pay
        3.PegPay

        0.Back 00.Main Menu
        """)
    elif first_qn == '7':
        print("""
        Financial Services
        1.Banks
        2.Group Collections
        3.M-SACCO
        4.ATM Withdraw
        5.NSSF Savings
        6.Insurance
        7.Yassako Loans
        8.SACCO
        9.AirtelMoney MasterCard
        10.Loans
        11.Savings
        n Next
    
        """)
    elif first_qn == '8':
        print("""
        Please accept the JUMO Terms & Conditions to access the Wewole service.
        tc.jumo.world/aug
        1.Accept
        2.View Key TandCs
        3.Cancel

        """)
    elif first_qn == '9':
        print("""
        Enter Merchant ID

        0.Back 00.Main Menu

        """)
    elif first_qn == '10':
        print("""
        My account
        1.My Pin
        2.Check Balance
        3.Request Statement
        4.Last 4 Transactions
        5.Invite a Friend
        6.Messages
        7.Transaction Status
        8.My Transaction Reversals
        9.Agent Locator
        n Next

        """)
    else:
        print('Invalid selection')
else:
    while(1):
        time.sleep(0.5)
        print()
        print('Dial *185# to use Airtel Money.')
        print()
        time.sleep(0.5)
        
        code = input('Enter mobile money code: ')
        code_list = list(code)
        space = ' ' in code_list

        while space == True:
            code_list.remove(" ")
            space = " " in code_list

        if "".join(code_list) == '*185#':
            print('Welcome to Airtel Money')
            break




            
          


    
