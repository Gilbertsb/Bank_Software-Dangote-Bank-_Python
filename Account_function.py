from saving_acc import*
from current_account import*
from datetime import *

acc=0
def choices():
    global acc
    print("+----------+")
    print('|1.SAVING  |')
    print('|2.CURRENT |')
    print("+----------+")
    acc=eval(input('CHOOSE ACCOUNT (ex: 2): '))

Account_saving = []
Account_current =[]

def create_new_acc():                    #function to create new account
    choices()
    global acc
    date_open=date.today()
    last_vist=date.today()
    acc_number_crnt='000245-'+str(len(Account_current)+1)
    acc_number1_svng='100245-'+str(len(Account_saving)+1)
    acc_nms = input("Enter Clients names: ")           #different prompnt for userto enter
    opened_dt = date_open
    blance = eval(input("Enter Current balance: "))     #Account deteils
    adress = input("Enter address of client: ")
    phone_nm = input("Enter phone number: ")
    last_time_withdrw=last_vist

    current_date=date.today()
    if opened_dt.month-current_date.month>=1:
        intrest_rate_current =blance*1/100
    else:
        intrest_rate_current=0

    if opened_dt.month-current_date.month>=1:
        intrest_rate_saving = blance * 3 / 100
    else:
        intrest_rate_saving=0


    total_saving=blance+intrest_rate_saving

    total_current=blance+intrest_rate_current

    if acc==1:                          #Appending on list bank details
        Account_saving.append(Saving_acc(acc_number1_svng, acc_nms, opened_dt, blance, adress,
                                         phone_nm,last_time_withdrw,intrest_rate_saving,total_saving ))

    elif acc==2:
        Account_current.append(Current_acc(acc_number_crnt, acc_nms, opened_dt, blance, adress,
                                           phone_nm,intrest_rate_current,total_current))

    print('YOU HAVE SUCCESSFULLY ADDED NEW ACCOUNT')

def deposit():                #function to deposit money
    choices()
    global acc
    if acc==1:
        index = 1  # index f
        print('No: Account number -- Account names')
        for x in Account_saving:  # loop to veiw bank details

            print(index,': ',x.acc_number,'--', x.acc_names)  # Generating bank account names
            index += 1

        bank_temp =input("Select Account number(ex:100245-1) you want to deposit on: ")
        #bank_temp = Account_saving[deposit - 1]
        for i in Account_saving:  # Loop to access accounts

            if bank_temp == i.acc_number:  # checking if user enterd correct number

                money = eval(input('Enter amount of money you are Depositing: '))

                i.acc_amount = i.acc_amount + int(money)  # adding money
                print('Added amount are: ', money)
                print("For now")
                print('____________________________________________________________')
                print('Acc_number             Names             Amount ')
                print('------------------------------------------------------------')
                print(i.acc_number, '-------------', i.acc_names, '--------', i.acc_amount, )
                print('____________________________________________________________')
                print('\n')

                print("YOU HAVE SUCCESSFULLY DEPOSITED MONEY!!")
                print('\n')
            else:
                print("WE DON'T HAVE THAT")

    elif acc==2:
        index = 1  # index f
        print('No: Account number -- Account names')
        for x in Account_current:  # loop to veiw bank details

            print(index,': ',x.acc_number,'--', x.acc_names)  # Generating bank account names
            index += 1

        deposit = input("Select Account number(ex:000245-1) you want to deposit on: ")
        #bank_temp = Account_current[deposit - 1]
        for i in Account_current:  # Loop to access accounts

            if deposit == i.acc_number:  # checking if user enterd correct number

                money = eval(input('Enter amount of money you are Depositing: '))

                i.acc_amount = i.acc_amount + int(money)  # adding money
                print('Added amount are: ', money)
                print("For now")
                print('_______________________________________________________')
                print('Acc_number             Names             Amount ')
                print('-------------------------------------------------------')
                print(i.acc_number, '-------', i.acc_names, '-------', i.acc_amount, )
                print('________________________________________________________')
                print('\n')

                print("YOU HAVE SUCCESSFULLY DEPOSITED MONEY!!")
                print('\n')
            else:
                print("WE DON'T HAVE THAT")
#this function helps to withdraw money from account
def withdraw():
    current_date=date.today()
    choices()
    global acc
    if acc==1:
        index = 1
        print('No: Account number -- Account names')
        for x in Account_saving:
            print(index,': ',x.acc_number,'--', x.acc_names)  # Viewing main detail
            index += 1

        bank_temp = input("Select Account number(ex:100245-1) you want to withdraw on: ")
        #bank_temp = Account_saving[withdrw - 1]

        for i in Account_saving:
            last_month=current_date.month - i.last_withdrw_time.month

            if bank_temp == i.acc_number:
                if last_month >= 6:
                    money = input('Enter amount of money you are Withdrawing: ')

                    i.acc_amount = i.acc_amount - int(money)  # Withdrawing money
                    i.last_withdrw_time = date.today()
                    print('Withdrawn amount are: ', money)
                    print("For now")
                    print('______________________________________________________________________________')
                    print('Acc_number             Names             Amount                  Current month')
                    print('------------------------------------------------------------------------------')
                    print(i.acc_number, '--------', i.acc_names, '-------', i.acc_amount, '--------', i.last_withdrw_time)
                    print('\n')

                    print("YOU HAVE SUCCESSFULLY WITHDRAWN MONEY!!")
                else:
                    print("YOU CAN ONLY WITHDRAW AFTER 6 MONTHS!!")

            else:
                print("WE DON'T HAVE THAT ACCOUNT, OR TIME TO WITHDRAW HAS NOT YET COME!!")
    elif acc==2:
        index = 1
        print('No: Account number -- Account names')
        for x in Account_current:
            print(index,': ',x.acc_number,'--', x.acc_names)  # Viewing main detail
            index += 1

        withdrw = input("Select Account number(ex:000245-1) you want to withdraw on: ")
        #bank_temp = Account_current[withdrw - 1]
        for i in Account_current:

            if withdrw == i.acc_number:

                money = input('Enter amount of money you are Withdrawing: ')

                i.acc_amount = i.acc_amount - int(money)  # Withdrawing money
                print('Withdrawn amount are: ', money)
                print("For now")
                print('_________________________________________________')
                print('Acc_number             Names             Amount ')
                print('------------------------------------------------')
                print(i.acc_number, '----', i.acc_names, '----', i.acc_amount, )
                print('\n')

                print("YOU HAVE SUCCESSFULLY WITHDRAWN MONEY!!")
            else:
                print("WE DON'T HAVE THAT")

def transnfer():    #Function to transfer money to any account you want in your categorie
    choices()
    global acc
    if acc == 1:
        index = 1
        print('No: Account number -- Account names')
        for x in Account_saving:
            print(index,': ',x.acc_number,'--', x.acc_names)  # Viewing main details
            index += 1
        bank_temp = input('Select Account number(ex:100245-1) of client who wants to transfer:')
        #bank_temp = Account_saving[acount - 1]
        for x in Account_saving:
            if bank_temp == x.acc_number:
                print('__________________________________________')
                print('Acc_no        Names                Money')
                print('------------------------------------------')
                print(x.acc_number, '----', x.acc_names, '----', x.acc_amount, )
                # Prompting user to enter amount to transifer
                tra_to = input('Select Account number(ex:100245-1) you want to transfer to:')
                #tra_temp = Account_saving[tra_to - 1]

                for i in Account_saving:
                    if tra_to == i.acc_number:
                        amount = eval(input('Enter amount of money you want to transfer: '))
                        if x.acc_amount > amount:
                            x.acc_amount = x.acc_amount - amount  # Removing money for transfer
                            i.acc_amount = i.acc_amount + amount  # Adding money to a receaver
                            print('Client', x.acc_names, 'with Acount number ', x.acc_number, 'has transfered, \n',
                                  amount, 'to ', i.acc_names, 'with', i.acc_number, 'and remaining balance is:',
                                  x.acc_amount)
            else:
                print("WE DON'T HAVE THAT")

    elif acc==2:
        index = 1
        print('No: Account number -- Account names')
        for x in Account_current:
            print(index, ': ', x.acc_number, '--', x.acc_names)  # Viewing main details
            index += 1
        acount = input('Select Account number(ex:000245-1) of client who wants to transfer:')
        #bank_temp = Account_current[acount - 1]
        for x in Account_current:
            if acount == x.acc_number:
                print('__________________________________________')
                print('Acc_no        Names                Money')
                print('------------------------------------------')
                print(x.acc_number, '----', x.acc_names, '----', x.acc_amount, )
                # Prompting user to enter amount to transifer
                tra_temp = input('Select Account number(ex:000245-1) you want to transfer to:')
                #tra_temp = Account_saving[tra_to - 1]

                for i in Account_current:
                    if tra_temp == i.acc_number:
                        amount = eval(input('Enter amount of money you want to transfer: '))
                        if x.acc_amount > amount:
                            x.acc_amount = x.acc_amount - amount  # Removing money for transfer
                            i.acc_amount = i.acc_amount + amount  # Adding money to a receaver
                            print('Client', x.acc_names, 'with Acount number ', x.acc_number, 'has transfered, \n',
                                  amount, 'to ', i.acc_names, 'with', i.acc_number, 'and remaining balance is:',
                                  x.acc_amount)
            else:
                print("WE DON'T HAVE THAT")
#this function helps to check balance of account you can choose
def bank_bal():
    choices()
    global acc
    if acc == 1:
        index = 1
        print('No: Account number -- Account names')
        for x in Account_saving:
            print(index,': ',x.acc_number,'--', x.acc_names)  # Viewing main detail
            index += 1
        bank_ba = input("Select Account number(ex:100245-1) you want to check balance: ")
        #bank_ba = Account_saving[bank_b - 1]
        for i in Account_saving:

            if bank_ba == i.acc_number:

                print("For now")
                print('_________________________________________________')
                print('Acc_number             Names             Amount ')
                print('------------------------------------------------')
                print(i.acc_number, '----', i.acc_names, '----', i.acc_amount, )
                print('\n')
            else:
                print("WE DON'T HAVE THAT")
    elif acc==2:
        index = 1
        print('No: Account number -- Account names')
        for x in Account_current:
            print(index,': ',x.acc_number,'--', x.acc_names)  # Viewing main detail
            index += 1
        bank_b = input("Select Account number(ex:000245-1) you want to check balance: ")
        #bank_ba = Account_current[bank_b - 1]
        for i in Account_current:

            if bank_b == i.acc_number:

                print("For now")
                print('_________________________________________________')
                print('Acc_number             Names             Amount ')
                print('------------------------------------------------')
                print(i.acc_number, '----', i.acc_names, '----', i.acc_amount, )
                print('\n')
            else:
                print("WE DON'T HAVE THAT")

def main():      #main function
    print("USE NUMBER TO SELECT ANY THING FROM MENU")
    print("_______________________________")
    print("|\t 1.CREATE ACCOUNT          |")
    print("|\t 2.DEPOSIT MONEY           |")
    print("|\t 3.WITHDRAW MONEY          |")
    print("|\t 4.TRANSFER MONEY          |")
    print("|\t 5.CHECK BALANCE           |")
    print("|______________________________|")

    selection = input("Select menu with using number(1-5): ")

    if selection == '1':
        create_new_acc()   #Calling function create_new_acc
    elif selection == '2':
        deposit()            #Calling function deposit
    elif selection == '3':
        withdraw()          #Calling function with_draw
    elif selection == '4':
        transnfer()        #Calling function to transifer
    elif selection == '5':
        bank_bal()
    else:
        print(" WE DON'T HAVE CHOICE LOOK LIKE THAT")

def exit_this():            #function to exit program
    exit("THANK YOU FOR USING THIS SOFTWARE SEE YOUUU!!!")