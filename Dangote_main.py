from Account_function import *


#I have only tested my program on selecting wrong menu number, where
#if you select wrong it is going to get you back,

main()     #calling main function
y = True
while y == y:  # making endless loop
    # prompting user to select Yes to continue or No to exit
    y = input("If you want to CONTINUE enter Y and if  you want to EXIT enter N : ")
    if y.casefold() == "Y".casefold():    #checking if user choose yes
        main()                            #Calling main function
    elif y.casefold() == 'N'.casefold(): #checking if user choose no
        exit_this()                      #calling exit function
    else:

        print("You did not choose any ")
        exit()
