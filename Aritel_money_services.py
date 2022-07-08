from select import select
import time

from sympy import Ei

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
            elif more_selection == '2':
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
                    data_select = input(' ')
                    if data_select == '1':
                        print("""
                        1 Daily_500MB @ 2K/-
                        2 Weekly 3.5GB @ 10K/-
                        3 Monthly_12GB @ 30K/-
                        * Back
                        """)
                        data_select_then = input(' ')
                        if data_select_then == '1':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '2':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '3':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '*':
                            print("""
                            1 Airtel TV Bundles
                            2 DSTV Bundles
                            3 Afro Media Bundles
                            * Back
                            """)
                            data_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif data_select == '2':
                        print("""
                        1 Daily_500MB @ 2K/-
                        2 Weekly 3.5GB @ 10K/-
                        3 Monthly_12GB @ 30K/-
                        * Back
                        """)
                        data_select_then = input(' ')
                        if data_select_then == '1':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '2':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '3':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '*':
                            print("""
                            1 Airtel TV Bundles
                            2 DSTV Bundles
                            3 Afro Media Bundles
                            * Back
                            """)
                            data_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif data_select == '3':
                        print("""
                        1 Daily_500MB @ 2K/-
                        2 Weekly 3.5GB @ 10K/-
                        3 Monthly_12GB @ 30K/-
                        * Back
                        """)
                        data_select_then = input(' ')
                        if data_select_then == '1':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '2':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '3':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '*':
                            print("""
                            1 Airtel TV Bundles
                            2 DSTV Bundles
                            3 Afro Media Bundles
                            * Back
                            """)
                            data_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif data_select == '*':
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
                elif further_selection == '5':
                    print("""
                    1 100,000/- for 45GB
                    2 50,000/- for 20GB
                    3 25,000/- for 9GB
                    4 16,000/- for 5.5GB
                    5 7,500/- for 2.5GB
                    6 5,000/- for 1.5GB
                    * Back
                    """)
                    chillax_selection = input(' ')
                    if chillax_selection == '1':
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '2':
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '3':
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '4':
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '5':
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '6':
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '*':
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
                elif further_selection == '6':
                    print("""
                    1 Roaming Data Bundles
                    2 Postpaid CAP limit
                    * Back
                    """)
                    roam_selection = input(' ')
                    if roam_selection == '1':
                        print("""
                        1 One Network Bundles
                        2 Global Bundles
                        * Back
                        """)
                    elif roam_selection == '2':
                        print("""

                        """)
                    elif roam_selection == '*':
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
                elif further_selection =='*':
                    print("""
                    Data Bundles 
                    1.Buy for Self
                    2.Buy for Another

                    0.Back 00.Main Menu
                    """)
                    more_selection = input(' ')
                else:
                    print('Invalid selection.')
            elif more_selection == '2':
                print("""
                1 Daily 
                2 Weekly
                3 Monthly
                4 TV Bundles
                5 Chillax Bundles
                6 Roaming Data
                7 WIFI Indoor bundles
                * Back
                """)
                other_selection = input(' ')
                if other_selection == '1':
                    print("""
                    1 500/- for 80MB
                    2 1k/- for 180MB
                    3 2k/- for 400MB
                    4 5000/- for 2GB
                    5 250/- for 30MB
                    6 11500/- for 4GB (3Days)
                    7 7500/- for 2GB (3Days)
                    8 Night 2GB @ 2K
                    9 Night 5GB @ 4K
                    * Back
                    """)
                    data_selection = input(' ')
                    if data_selection == '1':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '2':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '3':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '4':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '5':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '6':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '7':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '8':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '9':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print(""""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif data_selection == '*':
                        print("""
                        1 Daily 
                        2 Weekly
                        3 Monthly
                        4 TV Bundles
                        5 Chillax Bundles
                        6 Roaming Data
                        7 WIFI Indoor bundles
                        * Back
                        """)
                        other_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif other_selection == '2':
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
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '2':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '3':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '4':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
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
                        7 WIFI Indoor bundles
                        * Back
                        """)
                        other_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif other_selection == '3':
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
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '2':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '3':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '4':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '5':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                        Please Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif then_select == '6':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
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
                        7 WIFI Indoor bundles
                        * Back
                        """)
                        other_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif other_selection == '4':
                    print("""
                    1 Airtel TV Bundles
                    2 DSTV Bundles
                    3 Afro Media Bundles
                    * Back
                    """)
                    data_select = input(' ')
                    if data_select == '1':
                        print("""
                        1 Daily_500MB @ 2K/-
                        2 Weekly 3.5GB @ 10K/-
                        3 Monthly_12GB @ 30K/-
                        * Back
                        """)
                        data_select_then = input(' ')
                        if data_select_then == '1':
                            print("""
                            Please enter other number (070xxx 075xx or 020xx or 0740xx)
                            """)
                            number = input(' ')
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '2':
                            print("""
                            Please enter other number (070xxx 075xx or 020xx or 0740xx)
                            """)
                            number = input(' ')
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '3':
                            print("""
                            Please enter other number (070xxx 075xx or 020xx or 0740xx)
                            """)
                            number = input(' ')
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '*':
                            print("""
                            1 Airtel TV Bundles
                            2 DSTV Bundles
                            3 Afro Media Bundles
                            * Back
                            """)
                            data_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif data_select == '2':
                        print("""
                        1 Daily_500MB @ 2K/-
                        2 Weekly 3.5GB @ 10K/-
                        3 Monthly_12GB @ 30K/-
                        * Back
                        """)
                        data_select_then = input(' ')
                        if data_select_then == '1':
                            print("""
                            Please enter other number (070xxx 075xx or 020xx or 0740xx)
                            """)
                            number = input(' ')
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '2':
                            print("""
                            Please enter other number (070xxx 075xx or 020xx or 0740xx)
                            """)
                            number = input(' ')
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '3':
                            print("""
                            Please enter other number (070xxx 075xx or 020xx or 0740xx)
                            """)
                            number = input(' ')
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '*':
                            print("""
                            1 Airtel TV Bundles
                            2 DSTV Bundles
                            3 Afro Media Bundles
                            * Back
                            """)
                            data_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif data_select == '3':
                        print("""
                        1 Daily_500MB @ 2K/-
                        2 Weekly 3.5GB @ 10K/-
                        3 Monthly_12GB @ 30K/-
                        * Back
                        """)
                        data_select_then = input(' ')
                        if data_select_then == '1':
                            print("""
                            Please enter other number (070xxx 075xx or 020xx or 0740xx)
                            """)
                            number = input(' ')
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '2':
                            print("""
                            Please enter other number (070xxx 075xx or 020xx or 0740xx)
                            """)
                            number = input(' ')
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '3':
                            print("""
                            Please enter other number (070xxx 075xx or 020xx or 0740xx)
                            """)
                            number = input(' ')
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_select_then == '*':
                            print("""
                            1 Airtel TV Bundles
                            2 DSTV Bundles
                            3 Afro Media Bundles
                            * Back
                            """)
                            data_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif data_select == '*':
                        print("""
                        1 Daily
                        2 Weekly
                        3 Monthly
                        4 TV Bundles
                        5 Chillax Bundles
                        6 Roaming Data
                        7 WIFI Indoor bundles
                        * Back
                        """)
                        further_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif other_selection == '5':
                    print("""
                    1 100,000/- for 45GB
                    2 50,000/- for 20GB
                    3 25,000/- for 9GB
                    4 16,000/- for 5.5GB
                    5 7,500/- for 2.5GB
                    6 5,000/- for 1.5GB
                    * Back
                    """)
                    chillax_selection = input(' ')
                    if chillax_selection == '1':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '2':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '3':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '4':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '5':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '6':
                        print("""
                        Please enter other number (070xxx 075xx or 020xx or 0740xx)
                        """)
                        number = input(' ')
                        print("""
                            Enter PIN
                            """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif chillax_selection == '*':
                        print("""
                        1 Daily
                        2 Weekly
                        3 Monthly
                        4 TV Bundles
                        5 Chillax Bundles
                        6 Roaming Data
                        7 WIFI Indoor bundles
                        * Back
                        """)
                        further_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif other_selection == '6':
                    print("""
                    1 One Network Bundles
                    2 Global Bundles
                    * Back
                    """)
                    roam_select = input(' ')
                    if roam_select == '1':
                        print("""
                        1
                        KE,RW,TZ,DRC,NG,IND,RC,GB,NI,SEY,MD,ZM,CH,MU,BA,SR
                        * Back
                        """)
                        roam_further_select = input(' ')
                        if roam_further_select == '1':
                            print("""
                            1 Daily 400MB:4K
                            2 Weekly 1GB:8K
                            3 Weekly 3GB:40K (15 Days)
                            4 Monthly 10GB:5K
                            * Back
                            """)
                            duration_select = input(' ')
                            if duration_select == '1':
                                print("""
                                Enter PIN
                                """)
                                pin = input(' ')
                                prin("""
                                Transaction in progress.
                                """)
                            elif duration_select == '2':
                                print("""
                                Enter PIN
                                """)
                                pin = input(' ')
                                prin("""
                                Transaction in progress.
                                """)
                            elif duration_select == '3':
                                print("""
                                Enter PIN
                                """)
                                pin = input(' ')
                                prin("""
                                Transaction in progress.
                                """)
                            elif duration_select == '4':
                                print("""
                                Enter PIN
                                """)
                                pin = input(' ')
                                prin("""
                                Transaction in progress.
                                """)
                            elif duration_select == '*':
                                print("""
                                1
                                KE,RW,TZ,DRC,NG,IND,RC,GB,NI,SEY,MD,ZM,CH,MU,BA,SR
                                * Back
                                """)
                                roam_further_select = input(' ')
                            else:
                                print('Invalid selection.')
                        elif roam_further_select == '*':
                            print("""
                            1 One Network Bundles
                            2 Global Bundles
                            * Back
                            """)
                            roam_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif roam_select == '2':
                        print("""
                        1 Daily 400MB:40K
                        2 Weekly 1GB:110k
                        3 Weekly 3GB:185k
                        4 Monthly 10GB:550k
                        * Back
                        """)
                        data_roam_select = input(' ')
                        if data_roam_select == '1':
                            print("""
                            Enter pin
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_roam_select == '2':
                            print("""
                            Enter pin
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_roam_select == '3':
                            print("""
                            Enter pin
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_roam_select == '4':
                            print("""
                            Enter pin
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif data_roam_select == '*':
                            print("""
                            1 One Network Bundles
                            2 Global Bundles
                            * Back
                            """)
                            roam_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif roam_select == '*':
                        print("""
                        1 Daily 
                        2 Weekly
                        3 Monthly
                        4 TV Bundles
                        5 Chillax Bundles
                        6 Roaming Data
                        7 WIFI Indoor bundles
                        * Back
                        """)
                        other_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif other_selection == '7':
                    print("""
                    1 WIFI_50GB_Indoor@100k
                    2 Wifi_120GB_Indoor@20k
                    3 Wifi_200GB_Indoor@30k
                    * Back
                    """)
                    wifi_select = input(' ')
                    if wifi_select == '1':
                        print("""
                        Please enter bnumber (075xxx, 070xxx or 020xxx):
                        #.to quit
                        """)
                        bnumber = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif wifi_select == '2':
                        print("""
                        Please enter bnumber (075xxx, 070xxx or 020xxx):
                        #.to quit
                        """)
                        bnumber = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif wifi_select == '3':
                        print("""
                        Please enter bnumber (075xxx, 070xxx or 020xxx):
                        #.to quit
                        """)
                        bnumber = input(' ')
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif wifi_select == '*':
                        print("""
                        1 Daily 
                        2 Weekly
                        3 Monthly
                        4 TV Bundles
                        5 Chillax Bundles
                        6 Roaming Data
                        7 WIFI Indoor bundles
                        * Back
                        """)
                        other_selection = input(' ')
                    else:
                        print('Invalid selection.')
                elif other_selection == '*':
                    print("""
                    Data Bundles 
                    1.Buy for Self
                    2.Buy for Another

                    0.Back 00.Main Menu
                    """)
                    more_selection = input(' ')
                else:
                    print('Invalid selection.')
        elif selection == '3':
            print("""
            Voice Bundles
            0 Monthly 300Mins@10k
            1 Buy For Self
            2  Buy for Another
            """)
            part_selection = input(' ')
            if part_selection == '0':
                print("""
                Enter PIN
                """)
                pin = input(' ')
                print("""
                Transaction in progress.
                """)
            elif part_selection == '1':
                print("""
                1 Daily Bundles
                2 Weekly Bundle
                3 Monthly  Bundle
                4 Supa Combo/Kyabise
                5 Night Bundles(10pm-6am)
                * Back
                """)
                part_select_further = input(' ')
                if part_select_further == '1':
                    print("""
                    0 Monthly 300Mins@10K
                    1 Pakalast 30mins @1000
                    2 100mins@2000
                    3 300mins@5000-3days
                    4 kawa 10mins @500
                    5 Power Tooti
                    * Back
                    """)
                    final_further = input(' ')
                    if final_further == '0':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '1':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '2':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '3':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '4':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '5':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '2':
                    print("""
                    1 45mins@2000
                    2 Kawa 90Mins @3500
                    3 Pakalast 225Mins@6000
                    * Back
                    """)
                    final_further = input(' ')
                    if final_further == '1':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '2':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '3':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '3':
                    print("""
                    1 CMB 4500Mins@50K
                    2 CMB 200Mins@30K
                    3 CMB 750Mins@10k 2 Weeks
                    4 125Mins@5K
                    5 300Mins@10K
                    6 CMB 360Mins@75k(90 days)
                    * Back
                    """)
                    monthly_select = input(' ')
                    if monthly_select == '1':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '2':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '3':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '4':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '5':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '6':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '4':
                    print("""
                    1 Daily 
                    2 Weekly 
                    3 Monthly 
                    * Back
                    """)
                    supa_select = input(' ')
                    if supa_select == '1':
                        print("""
                        1 300 MBs + 35Mins@ 2,500 Daily
                        2 100 MBs + 15Mins @ 1,000
                        * Back
                        """)
                        supa_further = input(' ')
                        if supa_further == '1':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_further == '2':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_further == '*':
                            print("""
                            1 Daily 
                            2 Weekly 
                            3 Monthly 
                            * Back
                            """)
                            supa_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif supa_select == '2':
                        print("""
                        1 2GB+ 100Mins@ 10,000 Weekly
                        2 1.5GB+ 50 Mins @7500 Weekly
                        * Back
                        """)
                        supa_weekly = input(' ')
                        if supa_weekly == '1':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_weekly == '2':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_weekly == '*':
                            print("""
                            1 Daily 
                            2 Weekly 
                            3 Monthly 
                            * Back
                            """)
                            supa_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif supa_select == '3':
                        print("""
                        1 10GB+ 1200 Mins @50,000 Monthly
                        2 4GB+ 500 Mins@ 25,000 Monthly
                        * Back
                        """)
                        supa_weekly = input(' ')
                        if supa_weekly == '1':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_weekly == '2':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_weekly == '*':
                            print("""
                            1 Daily 
                            2 Weekly 
                            3 Monthly 
                            * Back
                            """)
                            supa_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif supa_select == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '5':
                    print("""
                    1 Paka Night 20Min@300
                    * Back
                    """)
                    further_night = input(' ')
                    if further_night == '1':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif further_night == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '*':
                    print("""
                    Voice Bundles
                    0 Monthly 300Mins@10k
                    1 Buy For Self
                    2  Buy for Another
                    """)
                    part_selection = input(' ')
                else:
                    print('Invalid selection.')
            elif part_selection == '2':
                print("""
                1 Daily Bundles
                2 Weekly Bundle
                3 Monthly  Bundle
                4 Supa Combo/Kyabise
                5 Night Bundles(10pm-6am)
                * Back
                """)
                part_select_further = input(' ')
                if part_select_further == '1':
                    print("""
                    0 Monthly 300Mins@10K
                    1 Pakalast 30mins @1000
                    2 100mins@2000
                    3 300mins@5000-3days
                    4 kawa 10mins @500
                    5 Power Tooti
                    * Back
                    """)
                    final_further = input(' ')
                    if final_further == '0':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '1':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '2':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '3':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '4':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '5':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '2':
                    print("""
                    1 45mins@2000
                    2 Kawa 90Mins @3500
                    3 Pakalast 225Mins@6000
                    * Back
                    """)
                    final_further = input(' ')
                    if final_further == '1':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '2':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '3':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif final_further == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '3':
                    print("""
                    1 CMB 4500Mins@50K
                    2 CMB 200Mins@30K
                    3 CMB 750Mins@10k 2 Weeks
                    4 125Mins@5K
                    5 300Mins@10K
                    6 CMB 360Mins@75k(90 days)
                    * Back
                    """)
                    monthly_select = input(' ')
                    if monthly_select == '1':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '2':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '3':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '4':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '5':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '6':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif monthly_select == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '4':
                    print("""
                    1 Daily 
                    2 Weekly 
                    3 Monthly 
                    * Back
                    """)
                    supa_select = input(' ')
                    if supa_select == '1':
                        print("""
                        1 300 MBs + 35Mins@ 2,500 Daily
                        2 100 MBs + 15Mins @ 1,000
                        * Back
                        """)
                        supa_further = input(' ')
                        if supa_further == '1':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Enter Receive Number
                            """)
                            receive_number = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_further == '2':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Enter Receive Number
                            """)
                            receive_number = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_further == '*':
                            print("""
                            1 Daily 
                            2 Weekly 
                            3 Monthly 
                            * Back
                            """)
                            supa_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif supa_select == '2':
                        print("""
                        1 2GB+ 100Mins@ 10,000 Weekly
                        2 1.5GB+ 50 Mins @7500 Weekly
                        * Back
                        """)
                        supa_weekly = input(' ')
                        if supa_weekly == '1':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Enter Receive Number
                            """)
                            receive_number = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_weekly == '2':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Enter Receive Number
                            """)
                            receive_number = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_weekly == '*':
                            print("""
                            1 Daily 
                            2 Weekly 
                            3 Monthly 
                            * Back
                            """)
                            supa_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif supa_select == '3':
                        print("""
                        1 10GB+ 1200 Mins @50,000 Monthly
                        2 4GB+ 500 Mins@ 25,000 Monthly
                        * Back
                        """)
                        supa_weekly = input(' ')
                        if supa_weekly == '1':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Enter Receive Number
                            """)
                            receive_number = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_weekly == '2':
                            print("""
                            Enter PIN
                            """)
                            pin = input(' ')
                            print("""
                            Enter Receive Number
                            """)
                            receive_number = input(' ')
                            print("""
                            Transaction in progress.
                            """)
                        elif supa_weekly == '*':
                            print("""
                            1 Daily 
                            2 Weekly 
                            3 Monthly 
                            * Back
                            """)
                            supa_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif supa_select == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '5':
                    print("""
                    1 Paka Night 20Min@300
                    * Back
                    """)
                    further_night = input(' ')
                    if further_night == '1':
                        print("""
                        Enter PIN
                        """)
                        pin = input(' ')
                        print("""
                        Enter Receive Number
                        """)
                        receive_number = input(' ')
                        print("""
                        Transaction in progress.
                        """)
                    elif further_night == '*':
                        print("""
                        1 Daily Bundles
                        2 Weekly Bundle
                        3 Monthly  Bundle
                        4 Supa Combo/Kyabise
                        5 Night Bundles(10pm-6am)
                        * Back
                        """)
                        part_select_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif part_select_further == '*':
                    print("""
                    Voice Bundles
                    0 Monthly 300Mins@10k
                    1 Buy For Self
                    2  Buy for Another
                    """)
                    part_selection = input(' ')
                else:
                    print('Invalid selection.')
        elif selection == '4':
            print("""
            IControl
            1.Subscribe
            2.Make Payment

            0.Back 00.Main Menu
            """)
            i_select = input(' ')
            if i_select == '1':
                print("""
                Subscribe
                1.IControl 60k
                2.IControl 200k
                3.IControl 300k
                4.IControl 500k

                0.Back 00.Main Menu
                """)
                i_select_further = input(' ')
                if i_select_further == '1':
                    print("""
                    Subscribing for IControl of UGX60,000 Enter your PIN to confirm

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print(""""
                    Transaction in progress.
                    """)
                elif i_select_further == '2':
                    print("""
                    Subscribing for IControl of UGX200,000 Enter your PIN to confirm

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print(""""
                    Transaction in progress.
                    """)
                elif i_select_further == '3':
                    print("""
                    Subscribing for IControl of UGX300,000 Enter your PIN to confirm

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print(""""
                    Transaction in progress.
                    """)
                elif i_select_further == '4':
                    print("""
                    Subscribing for IControl of UGX500,000 Enter your PIN to confirm

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print(""""
                    Transaction in progress.
                    """)
                elif i_select_further == '0':
                    print("""
                    IControl
                    1.Subscribe
                    2.Make Payment

                    0.Back 00.Main Menu
                    """)
                    i_select = input(' ')
                else:
                    print('Invalid selection.')
            elif i_select == '2':
                print("""
                Sorry, we failed to lookup your information. Please try again later.
                                                                                   0k
                """)
            elif i_select == '0':
                print("""
                Airtime / Bundles
                1.Buy Airtime
                2.Buy Data Bundles(Offers Inside)
                3.Buy Voice Bundles
                4.IControl

                0.Back 00.Main Menu
                """)
                selection = input(' ')
            else:
                print('Invalid selection.')
        elif selection == '0':
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
        else:
            print('Invalid selection.')
    elif first_qn == '3':
        print("""
        Enter amount

        0.Back 00.Main Menu
        """)
        with_draw_amount = input(' ')
        print("""
        You have initiated withdraw of {with_draw_amount} and charged UGX 880.
        Confirm your PIN.
         0.Back 00.Main Menu
        """)
        pin = input(' ')
        print("""
        Transaction in progress.
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
        pay_bill = input(' ')
        if pay_bill == '1':
            print("""
            1.Pay Bill
            2.Buy Yaka
            3.New Connection Payment
            4.Token Enquiry
            5.Check UMEME balance

            0.Back 00.Main Menu
            """)
        elif pay_bill == '2':
            print("""
            Water 
            1.Pay NWSC
            2.Check NWSC Balance

            0.Back 00.Main Menu
            """)
        elif pay_bill == '3':
            print("""
            Pay TV
            1.DSTV / GOTV
            2.STARTIMES TV
            3.AZAM TV
            4.SIMBA TV
            5.Zuku 

            0.Back 00.Main Menu
            """)
        elif pay_bill == '4':
            print("""
            Pay Solar
            1.MKOPA Solar
            2.DLIGHT Solar
            3.Sun King
            4.SOLAR Now
            5.VILLAGE Power
            6.Startimes Solar
            7.BrightLife
            8.Tulima Solar
            9.GNU Grid Africa
            10.MySolo(ReadyPay)
            11.WASSHA
            n Next
            """)
        elif pay_bill == '5':
            print("""
            Enter meter number

            0.Back 00.Main Menu
            """)
            meter_number = input(' ')
            print("""
            Meter not FoundSystem
            Unvailable 
                                OK
            """)
        elif pay_bill == '6':
            print("""
            Enter Your Reference Number

            0.Back 00.Main Menu
            """)
            reference_number = input(' ')
            print("""
            Enter amount

            0.Back 00.Main menu
            """)
            amount = input(' ')
            print(f"""
            Pay KCCA for {reference_number}. Charge UGX 0. Confirm with your PIN

            0.Back 00.Main Menu 
            """)
            pin = input(' ')
            print("""
            Transaction in progress.
            """)
        elif pay_bill == '7':
            print("""
            URA
            1.Pay Registered 
            2.Pay Without PRN
            3.Verify Code
            4.Search PRN

            0.Back 00.Main Menu
            """)
        elif pay_bill == '8':
            print("""
            1.Airtel Postpaid
            2.Fixed Data

            0.Back 00.Main Menu
            """)
        elif pay_bill == '9':
            print("""
            Enter Business Number 

            0.Back 00.Main Menu
            """)
            business_number = input(' ')
            print("""
            You are not Register with Airtel Money
                                              OK
            """)
        elif pay_bill == '10':
            print("""
            1.WENRECO
            2.Local Government Payments
            3.SAVE ELECTRICITY

            0.Back 00.Main Menu
            """)
        else:
            print("""
            Invalid selection.
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
        school_fees = input(' ')
        if school_fees == '1':
            print("""
            Enter pupil Id

            0.Back 00.Main Menu
            """)
            pupil_id = input(' ')
            print("""
            Please enter a valid 9 digit numeric pupil id.
            Re-Enter pupil Id

            Cancel Send
            """)
        elif school_fees == '2':
            print("""
            School Pay
            1.Pay Fees

            0.Back 00.Main Menu
            """)
            school_pay_further = input(' ')
            if school_pay_further == '1':
                print("""
                Enter Student Number

                0.Back 00.Main Menu
                """)
                student_number = input(' ')
                print("""
                Enter amount

                0.Back 00.Main Menu
                """)
                school_amount = input(' ')
                print("""
                No student was found with the specified payment code or registration number.. 
                Help: Visit https://schoolpay.co.ug/stusearch or Call: 0200.502.140
                                                                              OK
                """)
            elif school_pay_further == '0':
                print("""
                School Fees
                1.Bridge Schools
                2.School Pay
                3.PegPay

                0.Back 00.Main Menu
                """)
                school_fees = input(' ') 
            else:
                print('Invalid selection.')
        elif school_fees == '3':
            print("""
            Enter School Code

            0.Back 00.Main Menu
            """)
            school_code = input(' ')
            print("""
            Enter Student Number

            0.Back 00.Main Menu
            """)
            student_number = input(' ')
            print("""
            STUDENT NOT FOUND
                           OK
            """)
        elif school_fees == '0':
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
        else:
            print('Invalid selection.')
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
        financial_services = input(' ')
        if financial_services == '1':
            print("""
            Banks
            1.Equity
            2.Centenary
            3.Pride Microfinance
            4.Absa Bank
            5.DFCU
            6.Bank Of Africa
            7.STANBIC
            8.NC Bank
            9.Standard Chartered
            10.NEXT
            11.BRAC

            0.Back 00.Main Menu

            """)
            banks = input(' ')
            if banks == '1':
                print("""
                1.Airtel Money to Bank 
                2.Bank to Airtel Money
                3.Account balance

                0.Back 00.Main Menu
                """)
                equity = input(' ')
                if equity == '1':
                    print("""
                    1.On my account
                    2.On another account

                    0.Back 00.Main Menu
                    """)
                    equity_further = input(' ')
                    if equity_further == '1':
                        print("""
                        Enter amount

                        0.Back 00.Main Menu
                        """)
                        amount = input(' ')
                        print("""
                        No Accounts Found
                                         OK
                        """)
                    elif equity_further == '2':
                        print("""
                        Enter Account number

                        0.Back 00.Main menu
                        """)
                        account_number = input(' ')
                        print("""
                        Enter amount

                        0.Back 00.Main Menu
                        """)
                        amount = input(' ')
                        print(f"""
                        Send UGX {amount} to {account_number}. Charge UGX 0. Enter your PIN to confirm

                        0. Back 00.Main Menu
                        """)
                        pin = input(' ')
                        print("""
                        Dear customer, the  transaction amount you have entered is insufficient. Thank you.
                                                                                                                  OK
                        """)
                    elif equity_further == '0':
                        print("""
                        1.Airtel Money to Bank 
                        2.Bank to Airtel Money
                        3.Account balance

                        0.Back 00.Main Menu
                        """)
                        equity = input(' ')
                    else:
                        print('Invalid selection.')
                elif equity == '2':
                    print("""
                    Enter amount

                    0.Back 00.Main Menu
                    """)
                    amount = input(' ')
                    print("""
                    No Accounts Found
                                OK
                    """)
                elif equity == '3':
                    print("""
                    Charge UGX 0. Confirm with your PIN

                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    No Accounts Found
                                    OK
                    """)
                elif equity == '0':
                    print("""
                    Banks
                    1.Equity
                    2.Centenary
                    3.Pride Microfinance
                    4.Absa Bank
                    5.DFCU
                    6.Bank Of Africa
                    7.STANBIC
                    8.NC Bank
                    9.Standard Chartered
                    10.NEXT
                    11.BRAC

                    0.Back 00.Main Menu

                    """)
                    banks = input(' ')
                else:
                    print('Invalid selection.')
            elif banks == '2':
                print("""
                Enter Account Number

                0.Back 00.Main Menu
                """)
                account_number = input(' ')
                print("""
                Enter amount

                0.Back  00.Main Menu
                """)
                amount = input(' ')
                print(f"""
                Send UGX {amount} to Centenary bank {account_number}. Charge UGX 0. Enter your PIN to confirm

                0.Back 00.Main Menu
                """)
                pin = input(' ')
                print("""
                Transaction Failed with TXN Id: 72226316599, You do not have sufficient money on your account. You qualify for Quick Loan to complete transaction.
                                                                                                                            OK
                """)
            elif banks == '3':
                print("""
                Enter Account number

                0.Back 00.Main Menu
                """)
                account_number = input('')
                print("""
                Enter amount

                0.Back 00.Main Menu
                """)
                amount = input(' ')
                print(f"""
                Send UGX {amount} to Pride Microfinance bank {account_number}. Charge UGX 0. Enter your PIN to confirm

                0.Back 00.Main Menu
                """)
                pin = input(' ')
                print("""
                Transaction Failed with TXN Id : 72226759813, You do not have sufficient money on your account. You qualify for Quick Loan to complete transaction.
                                                                                                                                        OK
                """)
            elif banks == '4':
                print("""
                Enter Account Number

                0.Back 00.Main Menu
                """)
                account_number = input(' ')
                print("""
                Enter amount

                0.Back 00.Main Menu
                """)
                amount = input(' ')
                print(f"""
                Send UGX {amount} to {account_number}. Charge UGX 0. Enter your PIN to confirm

                0.Back 00.Main Menu
                """)
                pin = input(' ')
                print("""
                Transaction Failed with TXN Id :
                72226994681, You do not have sufficient money on your account. You qualify for Quick Loan to complete transaction.
                                                                                                                   OK
                """)
            elif banks == '5':
                print("""
                1.Airtel Money To Bank 
                2.Bank To Airtel Money
                
                0.Back 00.Main Menu
                """)
                choice_bank = input(' ')
                if choice_bank == '1':
                    print("""
                    Enter Account Number

                    0.Back 00.Main Menu
                    """)
                    account_number = input(' ')
                    print("""
                    Enter amount to send
                    """)
            elif banks == '6':
                print("""
                Enter Account Number

                0.Back 00.Main Menu
                """)
                account_number = input(' ')
                print("""
                Enter amount 

                0.Back 00.Main Menu
                """)
                amount = input(' ')
                print("""

                """)


    elif first_qn == '8':
        print("""
        Please accept the JUMO Terms & Conditions to access the Wewole service.
        tc.jumo.world/aug
        1.Accept
        2.View Key TandCs
        3.Cancel

        """)
        wewole_select =input(' ')
        if wewole_select == '1':
            print("""
            Enter the PIN to confirm
            """)
            pin = input(' ')
            print("""
            Would you like to receive marketing SMS's about our products and offers, including qualification notifications for a new loan?
            1 Yes 
            2 No
            """)
            notification = input(' ')
            if notification == '1':
                print("""
                Welcome to the Wewole loan service by JUMO.
                1.Get a loan
                2.Repay my loan
                3.Check my loan balance
                4.About Wewole
                5.View Key TandCs
                """)
                notification_further = input(' ')
                if notification_further == '1':
                    print("""
                    You do not qualify for a loan at the moment. Frequently use Airtel Money and other Airtel services and you may qualify in future.
                    0. Back
                    """)
                    back_select = input(' ')
                    if back_select == '0':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif notification_further == '2':
                    print("""
                    You do not have a loan right now. 
                    1. Request loan
                    0. Back
                    """)
                    loan_option = input(' ')
                    if loan_option == '1':
                        print("""
                        You do not qualify for a loan at the moment. Frequently use Airtel Money and other Airtel services and you may qualify in future.
                        0. Back
                        """)
                        back_select = input(' ')
                    elif loan_option == '0':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif notification_further == '3':
                    print("""
                    Enter the PIN to confirm
                    """)
                    pin = input(' ')
                    print("""
                    You do not have a loan right now. 
                    1. Get a loan
                    0. Back
                    """)
                    get_loan = input(' ')
                    if get_loan == '1':
                        print("""
                        You do not qualify for a loan at the moment. Frequently use Airtel Money and other Airtel services and you may qualify in future.
                        0. Back
                        """)
                        back_select = input(' ')
                    elif get_loan == '0':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif notification_further == '4':
                    print("""
                    1.What is Wewole?
                    2. How do I qualify?
                    3. Fees 
                    4. How do I pay?
                    5. Getting bigger loans
                    6. What happens if I pay late?
                    7. Marketing
                    8. Give Feedback
                    0. Back
                    """)
                    wewole_info = input(' ')
                    if wewole_info == '1':
                        print("""
                        Wewole offers loans to selected Airtel customers. No savings or paperwork needed and paid directly into your Airtel Money account.
                        0. Back
                        """)
                        wewole_info_further = input(' ')
                        if wewole_info_further == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '2':
                        print("""
                        To qualify for Wewole you must frequently recharge with talktime and use your Airtel Money.
                        0. Back
                        """)
                        qualify_info = input(' ')
                        if qualify_info == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '3':
                        print("""
                        Fees vary according to your Airtel Money account usage and your Wewole loan payment history. All fees are shown during your loan application process.
                        0. Back
                        """)
                        fees_info = input(' ')
                        if fees_info == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '4':
                        print("""
                        You can repay your loan at any time
                        1. Full payment
                        2. Part payment
                        0. Back
                        """)
                        repay_info = input(' ')
                        if repay_info == '1':
                            print("""
                            To pay your loan in full select "Repay my loan" on the main menu.
                            1. Next
                            0. Back
                            """)
                            repay_info_further = input(' ')
                            if repay_info_further == '1':
                                print("""
                                If your loan is overdue, we may auto deduct money from your MM account to repay your loan, either on a specific date or when you do a deposit.
                                0. Back
                                """)
                                repay_further_more = input(' ')
                                if repay_further_more == '0':
                                    print("""
                                    To pay your loan in full select "Repay my loan" on the main menu.
                                    1. Next
                                    0. Back
                                    """)
                                    repay_info_further = input(' ')
                                else:
                                    print('Invalid selection.')
                            elif repay_info_further == '0':
                                print("""
                                You can repay your loan at any time
                                1. Full payment
                                2. Part payment
                                0. Back
                                """)
                                repay_info = input(' ')
                            else:
                                print('Invalid selection.')
                        elif repay_info == '2':
                            print("""
                            To make a loan repayment at anytime, select "Repay my loan" on the main menu. Make sure you pay your full loan balance by the due date.
                            1. Next 
                            0. Back
                            """)
                            repay_info_part = input(' ')
                            if repay_info_part == '1':
                                print("""
                                If you loan is overdue, we may auto deduct money from your Airtel Money account to repay your loan, either on a specific date or when you do a deposit.
                                0. Back
                                """)
                                repay_info_back = input(' ')
                                if repay_info_back == '0':
                                    print("""
                                    To make a loan repayment at anytime, select "Repay my loan" on the main menu. Make sure you pay your full loan balance by the due date.
                                    1. Next 
                                    0. Back
                                    """)
                                    repay_info_part = input(' ')
                                else:
                                    print('Invalid selection.')
                            elif repay_info_part == '0':
                                print("""
                                You can repay your loan at any time
                                1. Full payment
                                2. Part payment
                                0. Back
                                """)
                                repay_info = input(' ')
                            else:
                                print('Invalid selection.')
                        elif repay_info == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '5':
                        print("""
                        Pay your Wewole loan on time, everytime and keep using your Airtel Money and you may qualify for bigger loans in future.
                        0. Back
                        """)
                        bigger_back = input(' ')
                        if bigger_back == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '6':
                        print("""
                        If you do not pay the loan balance by the due date, a late payment fee will be charged as shown when you applied fofr the laon.
                        0. Back
                        """)
                        not_pay = input(' ')
                        if not_pay == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '7':
                        print("""
                        Current Status: NO to marketing messages including loan qualification. 
                        1. I want to receive messages
                        2. I don't want to receive messages
                        0. Back
                        """)
                        marketing = input(' ')
                        if marketing == '1':
                            print("""
                            You have chosen to receive marketing SMS's about all products and offers including loan qualification. You can change your choice at any time.
                                                                                                                                                                  OK
                            """)
                        elif marketing == '2':
                            print("""
                            You have chosen not to receive marketing SMS's about all products and offers including laon qualification. You can change your choice at any time.
                                                                                                                                                                        OK
                            """)
                        elif marketing == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '8':
                        print("""
                        How would you describe you overall satisfaction with Wewole?
                        1. Dissatisfied
                        2. Neither satisfied nor dissatisfied
                        3. Satisfied
                        4. Very satisfied
                        """)
                        feed_back = input(' ')
                        if feed_back == '1':
                            print("""
                            Have you ever recommended Wewole to anyone else? Reply with a number.
                            1. Yes, to many people
                            2. Yes, to 1 or 2 people
                            3. No
                            """)
                            feed_back_further = input(' ')
                            if feed_back_further == '1':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '2':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '3':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            else:
                                print('Invalid selection.')
                        elif feed_back == '2':
                            print("""
                            Have you ever recommended Wewole to anyone else? Reply with a number.
                            1. Yes, to many people
                            2. Yes, to 1 or 2 people
                            3. No
                            """)
                            feed_back_further = input(' ')
                            if feed_back_further == '1':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '2':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '3':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            else:
                                print('Invalid selection.')
                        elif feed_back == '3':
                            print("""
                            Have you ever recommended Wewole to anyone else? Reply with a number.
                            1. Yes, to many people
                            2. Yes, to 1 or 2 people
                            3. No
                            """)
                            feed_back_further = input(' ')
                            if feed_back_further == '1':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '2':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '3':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            else:
                                print('Invalid selection.')
                        elif feed_back == '4':
                            print("""
                            Have you ever recommended Wewole to anyone else? Reply with a number.
                            1. Yes, to many people
                            2. Yes, to 1 or 2 people
                            3. No
                            """)
                            feed_back_further = input(' ')
                            if feed_back_further == '1':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '2':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '3':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            else:
                                print('Invalid selection.')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '0':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif notification_further == '5':
                    print("""
                    1. Wewole Key TandCs
                    2. Service Key TandCs
                    0. Back
                    """)
                    terms_select = input(' ')
                    if terms_select == '1':
                        print("""
                        When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                        1. Next
                        0. Back
                        """)
                        terms_select_further = input(' ')
                        if terms_select_further == '1':
                            print("""
                            All fees are shown during the loan application process. The loan amount, fees and due date will be sent by SMS after your loan application. 
                            1. Next
                            0. Back
                            """)
                            further_further = input(' ')
                            if further_further == '1':
                                print("""
                                Your loan repayment method is agreed when you apply. To make a loan repayment at anytime, select "Repay my loan".
                                1. Next 
                                0. Back
                                """)
                                further_1 = input(' ')
                                if further_1 == '1':
                                    print("""
                                    A late payment fee will be charged, and added to your loan balance if you do not pay your loan on the due date.
                                    0. Back
                                    """)
                                    further_2 = input(' ')
                                    if further_2 == '0':
                                        print("""
                                        Your loan repayment method is agreed when you apply. To make a loan repayment at anytime, select "Repay my loan".
                                        1. Next 
                                        0. Back
                                        """)
                                        further_1 = input(' ')
                                    else:
                                        print('Invalid selection.')
                                elif further_1 == '0':
                                    print("""
                                    All fees are shown during the loan application process. The loan amount, fees and due date will be sent by SMS after your loan application. 
                                    1. Next
                                    0. Back
                                    """)
                                    further_further = input(' ')
                                else:
                                    print('Invalid selection.')
                            elif further_further == '0':
                                print("""
                                When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                                1. Next
                                0. Back
                                """)
                                terms_select_further = input(' ')
                            else:
                                print('Invalid selection.')
                        elif terms_select_further == '0':
                            print("""
                            1. Wewole Key TandCs
                            2. Service Key TandCs
                            0. Back
                            """)
                            terms_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif terms_select == '2':
                        print("""
                        When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                        1. Next
                        0. Back
                        """)
                        terms_select_further = input(' ')
                        if terms_select_further == '1':
                            print("""
                            JUMO will share your personal information and usage with authorised parties (eg. FSPs) for regulatory and commercial purposes.
                            1. Next
                            0. Back
                            """)
                            further_terms = input(' ')
                            if further_terms == '1':
                                print("""
                                If you apply for a mobile financial services product you will have to accept the terms and conditions when applying for the product.
                                0. Back
                                """)
                            elif further_terms == '0':
                                print("""
                                When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                                1. Next
                                0. Back
                                """)
                                terms_select_further = input(' ')
                            else:
                                print('Invalid selection.')
                        elif terms_select_further == '0':
                            print("""
                            1. Wewole Key TandCs
                            2. Service Key TandCs
                            0. Back
                            """)
                            terms_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif terms_select == '0':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                else:
                    print('Invalid selection.')
            elif notification == '2':
                print("""
                Welcome to the Wewole loan service by JUMO.
                1.Get a loan
                2.Repay my loan
                3.Check my loan balance
                4.About Wewole
                5.View Key TandCs
                """)
                notification_further = input(' ')
                if notification_further == '1':
                    print("""
                    You do not qualify for a loan at the moment. Frequently use Airtel Money and other Airtel services and you may qualify in future.
                    0. Back
                    """)
                    back_select = input(' ')
                    if back_select == '0':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif notification_further == '2':
                    print("""
                    You do not have a loan right now. 
                    1. Request loan
                    0. Back
                    """)
                    loan_option = input(' ')
                    if loan_option == '1':
                        print("""
                        You do not qualify for a loan at the moment. Frequently use Airtel Money and other Airtel services and you may qualify in future.
                        0. Back
                        """)
                        back_select = input(' ')
                    elif loan_option == '2':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif notification_further == '3':
                    print("""
                    Enter the PIN to confirm
                    """)
                    pin = input(' ')
                    print("""
                    You do not have a loan right now. 
                    1. Get a loan
                    0. Back
                    """)
                    get_loan = input(' ')
                    if get_loan == '1':
                        print("""
                        You do not qualify for a loan at the moment. Frequently use Airtel Money and other Airtel services and you may qualify in future.
                        0. Back
                        """)
                        back_select = input(' ')
                    elif get_loan == '0':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif notification_further == '4':
                    print("""
                    1.What is Wewole?
                    2. How do I qualify?
                    3. Fees 
                    4. How do I pay?
                    5. Getting bigger loans
                    6. What happens if I pay late?
                    7. Marketing
                    8. Give Feedback
                    0. Back
                    """)
                    wewole_info = input(' ')
                    if wewole_info == '1':
                        print("""
                        Wewole offers loans to selected Airtel customers. No savings or paperwork needed and paid directly into your Airtel Money account.
                        0. Back
                        """)
                        wewole_info_further = input(' ')
                        if wewole_info_further == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '2':
                        print("""
                        To qualify for Wewole you must frequently recharge with talktime and use your Airtel Money.
                        0. Back
                        """)
                        qualify_info = input(' ')
                        if qualify_info == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '3':
                        print("""
                        Fees vary according to your Airtel Money account usage and your Wewole loan payment history. All fees are shown during your loan application process.
                        0. Back
                        """)
                        fees_info = input(' ')
                        if fees_info == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '4':
                        print("""
                        You can repay your loan at any time
                        1. Full payment
                        2. Part payment
                        0. Back
                        """)
                        repay_info = input(' ')
                        if repay_info == '1':
                            print("""
                            To pay your loan in full select "Repay my loan" on the main menu.
                            1. Next
                            0. Back
                            """)
                            repay_info_further = input(' ')
                            if repay_info_further == '1':
                                print("""
                                If your loan is overdue, we may auto deduct money from your MM account to repay your loan, either on a specific date or when you do a deposit.
                                0. Back
                                """)
                                repay_further_more = input(' ')
                                if repay_further_more == '0':
                                    print("""
                                    To pay your loan in full select "Repay my loan" on the main menu.
                                    1. Next
                                    0. Back
                                    """)
                                    repay_info_further = input(' ')
                                else:
                                    print('Invalid selection.')
                            elif repay_info_further == '0':
                                print("""
                                You can repay your loan at any time
                                1. Full payment
                                2. Part payment
                                0. Back
                                """)
                                repay_info = input(' ')
                            else:
                                print('Invalid selection.')
                        elif repay_info == '2':
                            print("""
                            To make a loan repayment at anytime, select "Repay my loan" on the main menu. Make sure you pay your full loan balance by the due date.
                            1. Next 
                            0. Back
                            """)
                            repay_info_part = input(' ')
                            if repay_info_part == '1':
                                print("""
                                If you loan is overdue, we may auto deduct money from your Airtel Money account to repay your loan, either on a specific date or when you do a deposit.
                                0. Back
                                """)
                                repay_info_back = input(' ')
                                if repay_info_back == '0':
                                    print("""
                                    To make a loan repayment at anytime, select "Repay my loan" on the main menu. Make sure you pay your full loan balance by the due date.
                                    1. Next 
                                    0. Back
                                    """)
                                    repay_info_part = input(' ')
                                else:
                                    print('Invalid selection.')
                            elif repay_info_part == '0':
                                print("""
                                You can repay your loan at any time
                                1. Full payment
                                2. Part payment
                                0. Back
                                """)
                                repay_info = input(' ')
                            else:
                                print('Invalid selection.')
                        elif repay_info == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '5':
                        print("""
                        Pay your Wewole loan on time, everytime and keep using your Airtel Money and you may qualify for bigger loans in future.
                        0. Back
                        """)
                        bigger_back = input(' ')
                        if bigger_back == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '6':
                        print("""
                        If you do not pay the loan balance by the due date, a late payment fee will be charged as shown when you applied fofr the laon.
                        0. Back
                        """)
                        not_pay = input(' ')
                        if not_pay == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '7':
                        print("""
                        Current Status: NO to marketing messages including loan qualification. 
                        1. I want to receive messages
                        2. I don't want to receive messages
                        0. Back
                        """)
                        marketing = input(' ')
                        if marketing == '1':
                            print("""
                            You have chosen to receive marketing SMS's about all products and offers including loan qualification. You can change your choice at any time.
                                                                                                                                                                  OK
                            """)
                        elif marketing == '2':
                            print("""
                            You have chosen not to receive marketing SMS's about all products and offers including laon qualification. You can change your choice at any time.
                                                                                                                                                                        OK
                            """)
                        elif marketing == '0':
                            print("""
                            1.What is Wewole?
                            2. How do I qualify?
                            3. Fees 
                            4. How do I pay?
                            5. Getting bigger loans
                            6. What happens if I pay late?
                            7. Marketing
                            8. Give Feedback
                            0. Back
                            """)
                            wewole_info = input(' ')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '8':
                        print("""
                        How would you describe you overall satisfaction with Wewole?
                        1. Dissatisfied
                        2. Neither satisfied nor dissatisfied
                        3. Satisfied
                        4. Very satisfied
                        """)
                        feed_back = input(' ')
                        if feed_back == '1':
                            print("""
                            Have you ever recommended Wewole to anyone else? Reply with a number.
                            1. Yes, to many people
                            2. Yes, to 1 or 2 people
                            3. No
                            """)
                            feed_back_further = input(' ')
                            if feed_back_further == '1':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '2':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '3':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            else:
                                print('Invalid selection.')
                        elif feed_back == '2':
                            print("""
                            Have you ever recommended Wewole to anyone else? Reply with a number.
                            1. Yes, to many people
                            2. Yes, to 1 or 2 people
                            3. No
                            """)
                            feed_back_further = input(' ')
                            if feed_back_further == '1':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '2':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '3':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            else:
                                print('Invalid selection.')
                        elif feed_back == '3':
                            print("""
                            Have you ever recommended Wewole to anyone else? Reply with a number.
                            1. Yes, to many people
                            2. Yes, to 1 or 2 people
                            3. No
                            """)
                            feed_back_further = input(' ')
                            if feed_back_further == '1':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '2':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '3':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            else:
                                print('Invalid selection.')
                        elif feed_back == '4':
                            print("""
                            Have you ever recommended Wewole to anyone else? Reply with a number.
                            1. Yes, to many people
                            2. Yes, to 1 or 2 people
                            3. No
                            """)
                            feed_back_further = input(' ')
                            if feed_back_further == '1':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '2':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            elif feed_back_further == '3':
                                print("""
                                Thank you for your valuable feedback.
                                                                   Ok
                                """)
                            else:
                                print('Invalid selection.')
                        else:
                            print('Invalid selection.')
                    elif wewole_info == '0':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                elif notification_further == '5':
                    print("""
                    1. Wewole Key TandCs
                    2. Service Key TandCs
                    0. Back
                    """)
                    terms_select = input(' ')
                    if terms_select == '1':
                        print("""
                        When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                        1. Next
                        0. Back
                        """)
                        terms_select_further = input(' ')
                        if terms_select_further == '1':
                            print("""
                            All fees are shown during the loan application process. The loan amount, fees and due date will be sent by SMS after your loan application. 
                            1. Next
                            0. Back
                            """)
                            further_further = input(' ')
                            if further_further == '1':
                                print("""
                                Your loan repayment method is agreed when you apply. To make a loan repayment at anytime, select "Repay my loan".
                                1. Next 
                                0. Back
                                """)
                                further_1 = input(' ')
                                if further_1 == '1':
                                    print("""
                                    A late payment fee will be charged, and added to your loan balance if you do not pay your loan on the due date.
                                    0. Back
                                    """)
                                    further_2 = input(' ')
                                    if further_2 == '0':
                                        print("""
                                        Your loan repayment method is agreed when you apply. To make a loan repayment at anytime, select "Repay my loan".
                                        1. Next 
                                        0. Back
                                        """)
                                        further_1 = input(' ')
                                    else:
                                        print('Invalid selection.')
                                elif further_1 == '0':
                                    print("""
                                    All fees are shown during the loan application process. The loan amount, fees and due date will be sent by SMS after your loan application. 
                                    1. Next
                                    0. Back
                                    """)
                                    further_further = input(' ')
                                else:
                                    print('Invalid selection.')
                            elif further_further == '0':
                                print("""
                                When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                                1. Next
                                0. Back
                                """)
                                terms_select_further = input(' ')
                            else:
                                print('Invalid selection.')
                        elif terms_select_further == '0':
                            print("""
                            1. Wewole Key TandCs
                            2. Service Key TandCs
                            0. Back
                            """)
                            terms_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif terms_select == '2':
                        print("""
                        When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                        1. Next
                        0. Back
                        """)
                        terms_select_further = input(' ')
                        if terms_select_further == '1':
                            print("""
                            JUMO will share your personal information and usage with authorised parties (eg. FSPs) for regulatory and commercial purposes.
                            1. Next
                            0. Back
                            """)
                            further_terms = input(' ')
                            if further_terms == '1':
                                print("""
                                If you apply for a mobile financial services product you will have to accept the terms and conditions when applying for the product.
                                0. Back
                                """)
                            elif further_terms == '0':
                                print("""
                                When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                                1. Next
                                0. Back
                                """)
                                terms_select_further = input(' ')
                            else:
                                print('Invalid selection.')
                        elif terms_select_further == '0':
                            print("""
                            1. Wewole Key TandCs
                            2. Service Key TandCs
                            0. Back
                            """)
                            terms_select = input(' ')
                        else:
                            print('Invalid selection.')
                    elif terms_select == '0':
                        print("""
                        Welcome to the Wewole loan service by JUMO.
                        1.Get a loan
                        2.Repay my loan
                        3.Check my loan balance
                        4.About Wewole
                        5.View Key TandCs
                        """)
                        notification_further = input(' ')
                    else:
                        print('Invalid selection.')
                else:
                    print('Invalid selection.')
            else:
                print('Invalid selection.')
        elif wewole_select == '2':
            print("""
            When you accept the TandCs, you consent to receiving SMS's and Airtel sharing your personal information with JUMO.
            1. Next 
            0. Back
            """)
            terms_and_conditions = input(' ')
            if terms_and_conditions == '1':
                print("""
                1. Wewole Key TandCs
                2. Service Key TandCs
                0. Back
                """)
                terms_select = input(' ')
                if terms_select == '1':
                    print("""
                    When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                    1. Next
                    0. Back
                    """)
                    terms_select_further = input(' ')
                    if terms_select_further == '1':
                        print("""
                        All fees are shown during the loan application process. The loan amount, fees and due date will be sent by SMS after your loan application. 
                        1. Next
                        0. Back
                        """)
                        further_further = input(' ')
                        if further_further == '1':
                            print("""
                            Your loan repayment method is agreed when you apply. To make a loan repayment at anytime, select "Repay my loan".
                            1. Next 
                            0. Back
                            """)
                            further_1 = input(' ')
                            if further_1 == '1':
                                print("""
                                A late payment fee will be charged, and added to your loan balance if you do not pay your loan on the due date.
                                0. Back
                                """)
                                further_2 = input(' ')
                                if further_2 == '0':
                                    print("""
                                    Your loan repayment method is agreed when you apply. To make a loan repayment at anytime, select "Repay my loan".
                                    1. Next 
                                    0. Back
                                    """)
                                    further_1 = input(' ')
                                else:
                                    print('Invalid selection.')
                            elif further_1 == '0':
                                print("""
                                All fees are shown during the loan application process. The loan amount, fees and due date will be sent by SMS after your loan application. 
                                1. Next
                                0. Back
                                """)
                                further_further = input(' ')
                            else:
                                print('Invalid selection.')
                        elif further_further == '0':
                            print("""
                            When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                            1. Next
                            0. Back
                            """)
                            terms_select_further = input(' ')
                        else:
                            print('Invalid selection.')
                    elif terms_select_further == '0':
                        print("""
                        1. Wewole Key TandCs
                        2. Service Key TandCs
                        0. Back
                        """)
                        terms_select = input(' ')
                    else:
                        print('Invalid selection.')
                elif terms_select == '2':
                    print("""
                    When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                    1. Next
                    0. Back
                    """)
                    terms_select_further = input(' ')
                    if terms_select_further == '1':
                        print("""
                        JUMO will share your personal information and usage with authorised parties (eg. FSPs) for regulatory and commercial purposes.
                        1. Next
                        0. Back
                        """)
                        further_terms = input(' ')
                        if further_terms == '1':
                            print("""
                            If you apply for a mobile financial services product you will have to accept the terms and conditions when applying for the product.
                            0. Back
                            """)
                        elif further_terms == '0':
                            print("""
                            When you accept the JUMO TandCs, you consent to receiving SMSs and Airtel sharing your personal information with JUMO tc.jumo.world/augl
                            1. Next
                            0. Back
                            """)
                            terms_select_further = input(' ')
                        else:
                            print('Invalid selection.')
                    elif terms_select_further == '0':
                        print("""
                        1. Wewole Key TandCs
                        2. Service Key TandCs
                        0. Back
                        """)
                        terms_select = input(' ')
                    else:
                        print('Invalid selection.')
                elif terms_select == '0':
                    print("""
                    Welcome to the Wewole loan service by JUMO.
                    1.Get a loan
                    2.Repay my loan
                    3.Check my loan balance
                    4.About Wewole
                    5.View Key TandCs
                    """)
                    notification_further = input(' ')
                else:
                    print('Invalid selection.')
            else:
                print('Invalid selection.')
        elif wewole_select == '3':
            print("""
            Your application was cancelled. Please select "View Key TandC's" or visit tc.jumo.world/aug to view the Terms and Conditions. For more info call 100.
                                                                                                                                                     OK
            """)
        else:
            print('Invalid selection.')
    elif first_qn == '9':
        print("""
        Enter Merchant ID

        0.Back 00.Main Menu

        """)
        merchant = input(' ')
        print("""
        You are not Register With Airtel Money
                                          OK
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
        account = input(' ')
        if account == '1':
            print("""
            1.Change PIN 
            2.Reset PIN/ Forgot PIN
            3.View Security Questions
            4.Set/ Change Security Question
            5.Learn More
            6.Reset PIN/ Forgot PIN

            0.Back 00.Main Menu
            """)
            account_further = input(' ')
            if account_further == '1':
                print("""
                Enter Old PIN:

                0.Back 00.Main Menu
                """)
                old_pin = input(' ')
                print("""
                Enter new PIN:

                0.Back 00.Main Menu
                """)
                new_pin = input(' ')
                print("""
                Re-enter New PIN:

                0.Back 00.Main Menu
                """)
                confirm_new_pin = input(' ')
                print("""
                Success 
                                      OK
                """)
            elif account_further == '2':
                print("""
                Security Question: Primary school name 
                Enter Security Answer:

                0.Back 00.Main Men
                """)
                security_qn = input(' ')
                print("""
                Dear customer, set your new PIN to enjoy Airtel Money services your temporary pin is 9726.
                                                                                           OK
                """)
            elif account_further == '3':
                print("""
                Enter PIN:

                0.Back 00.Main Menu
                """)
                pin_rest = input(' ')
                print("""
                Your Security Question is :
                Primary school name 
                                        OK
                """)
        elif account == '2':
            print("""
            Enter your PIN to confirm

            0.Back 00.Main Menu
            """)
            pin = input(' ')
            print(f"""
            Balance: UGX
            """)
        elif account == '3':
            print("""
            Enter Your Email ID

            0.Back 00.Main Menu
            """)
            email = input(' ')
            print("""
            Enter the From Date (DDMMYYYY)

            0.Back 00.Main Menu
            """)
            from_date = input(' ')
            print("""
            Enter Your PIN to confirm

            0.Back 00.Main Menu
            """)
            pin = input(' ')
            print(f"""
            Statement will be sent to {email}.
                                         OK
            """)
        elif account == '4':
            print("""
            Enter your PIN to confirm 

            0.Back 00.Main Menu
            """)
            pin = input(' ')
            print("""
            Ministatement sent on SMS
                                 OK
            """)
        elif account == '5':
            print("""
            Enter the Mobile Number you wish to invite to AirtelMoney

            0.Back 00.Main menu
            """)
            invite_number = input(' ')
            print("""
            Enter your PIN to confirm

            0.Back 00.Main Menu
            """)
            pin = input(' ')
            print("""
            Transaction Failed with TXN Id : 71862325138. Sorry, this number has already been invited. Please invite anohtetr numbe3r
                                                                                                                           OK
            """)
        elif account == '6':
            print("""
            Messages
            1.Viral Secret Code
            2.Resend Recent message

            0.Back 00.Main Menu
            """)
            messages = input(' ')
            print("""
            Enter Transaction Amount

            0.Back 00.Main Menu
            """)
            transaction_amount = input(' ')
            print("""
            Enter recipient Mobile Number

            0.Back 00.Main Menu
            """)
            recipient_number = input(' ')
            print("""
            Transaction Failed with TXN Id: 71862523568. No viral send  request found for the given inputs.
                                                                                                 OK
            """)
        elif account == '7':
            print("""
            Enter Transaction ID

            0.Back 00.Main Menu
            """)
            transaction_id = input(' ')
            print("""
            Enter your PIN to confirm

            0.Back 00.Main Menu
            """)
            pin = input(' ')
            print("""
            Dear customer, the transaction Id does not exist.
                                                 OK
            """)
        elif account == '8':
            print("""
            My Transaction Reversals
            1.Initiate Transaction Reversal
            2.Approve Pending Reversal

            0.Back 00.Main Menu
            """)
            transaction_reversal = input(' ')
            if transaction_reversal == '1':
                print("""
                Select Transaction:
                1.Other Send Transactions

                0.Back 00.Main Menu
                """)
                further_transaction = input(' ')
                if further_transaction == '1':
                    print("""
                    Enter Transaction ID:
                    """)
                    transaction_id_required = input(' ')
                    print("""
                    Enter PIN to confirm:
                    
                    0.Back 00.Main Menu
                    """)
                    pin = input(' ')
                    print("""
                    There is problem in application.
                                              OK
                    """)
                elif further_transaction == '0':
                    print("""
                    My Transaction Reversals
                    1.Initiate Transaction Reversal
                    2.Approve Pending Reversal

                    0.Back 00.Main Menu
                    """)
                    transaction_reversal = input(' ')
                else:
                    print('Invalid selection.')
            elif transaction_reversal == '2':
                print("""
                No transaction pending for approval
                                             OK
                """)
            elif transaction_reversal == '0':
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
                account = input(' ')
            else:
                print('Invalid selection.')
        elif account == '9':
            print("""
            1.Airtel Money Branch
            0.Back 00.Main Menu
            """)
            mobile_money_branch = input(' ')
            print("""
            Enter first 4 letters of your District: e.g Waki for Wakiso 

            0.Back 00.Main Menu
            """)
            district_letters = input(' ')
            print("""
            Please wait for SMS.
            """)
        elif account == 'n':
            print("""
            0.Back 00.Main Menu
            """)
            n = input(' ')
            if n == '0':
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

                first_qn = input(' ')
            elif n == '00':
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
        else:
            print('Invalid selection.')
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




            
          


    
