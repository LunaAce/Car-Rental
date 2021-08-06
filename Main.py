# Chew Jin Ye  
# TP059578
# Chew Eng Sen 
# TP053939
import datetime

def login(): # Fixed
    authenticate = False
    admin = False
    customer = False
    guest = True
    userInfo = []
    while not authenticate:
        with open("user.txt", "r") as f:
            username = input("Please Enter Your Username: ").strip()
            password = input("Please Enter Your Password: ").strip()
            print(f"Authorising...{username}")
            for line in f.readlines():
                line = line.strip()
                loginInfo = line.split(",")
                if loginInfo[0] == "Admin" and username == loginInfo[1] and password == loginInfo[2]:
                    print(f"Authorised \nWelcome {username}.\n")
                    input("Press any key to continue: ")
                    authenticate = True
                    admin = True
                    guest = False
                    userInfo += loginInfo
                elif loginInfo[0] == "Customer" and username == loginInfo[1] and password == loginInfo[2]:
                    print(f"Authorised \nWelcome {username}.\n")
                    input("Press any key to continue: ")
                    authenticate = True
                    customer = True
                    guest = False
                    userInfo += loginInfo
            if not authenticate:
                print("\nInvalid Username or Password, Please Try again.\n")

    return userInfo, authenticate, admin, customer, guest

def run(): # Checked Fixed
    menu_list = "--------------------------------------------------------------\n"
    menu_list += "Welcome to SUPER CAR RENTAL SERVICES (SCRS)\n"
    menu_list += "-------------------------------------------------------------\n"
    menu_list += "Your Options are: \n "
    menu_list += "1.Login. \n "
    menu_list += "2.View available cars for rent. \n "
    menu_list += "3.Register. \n "
    menu_list += "0.Exit. \n "
    print(menu_list)
    choice = ""
    authenticate = False
    admin = False
    customer = False
    guest = True
    userInfo = []
    while not authenticate:
        while not choice.isnumeric():
            choice = input("Please Enter Your Choices: ")
            if choice.isnumeric():
                user_choice = int(choice)
                if user_choice == 1:  # Login
                    user = login()
                    userInfo = user[0]
                    authenticate = user[1]
                    admin = user[2]
                    customer = user[3]
                    guest = user[4]

                elif user_choice == 2:  # Guest
                    search_vehicle(authenticate,admin,customer,guest,userInfo)

                elif user_choice == 3:  # Register
                    acc_register()

                elif user_choice == 0:  # Exit
                    exit()

            else:
                print("Invalid Command! \n")

        if authenticated:
            authenticated (authenticate,admin,customer,guest,userInfo)  
        
def authenticated(authenticate,admin,customer,guest,userInfo):
    if authenticate and admin:  # Admin
        adm_menu = ""
        adm_menu += f"\nHello {userInfo[1]}!\nWhat you wish to proceed?:\n"
        adm_menu += "1. Add Cars to be rented out.\n"
        adm_menu += "2. Modify Car Details.\n"
        adm_menu += "3. Display vehicles Records.\n"
        adm_menu += "4. Search Specific record.\n"
        adm_menu += "5. Return Rented Car.\n"
        adm_menu += "0. Exit.\n"
        print(adm_menu)
        choice = ""
        while not choice.isnumeric():
            choice = input("Please Enter your Choice: ")
            if choice.isnumeric():
                user_choice = int(choice)
                if user_choice == 1: 
                    add_vehicle(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 2: 
                    update_vehicle(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 3: 
                    search_vehicle(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 4:  
                    print("Display all record of\n"
                            "1.Customer Booking\n"
                            "2.Customer Payment\n"
                            "0.Back\n")
                    choice = ""
                    while not choice.isnumeric():
                        choice = input("What record you looking for? Choice: ")
                        if choice.isnumeric():
                            user_choice = int(choice)
                        if user_choice == 1:
                            get_book2(authenticate,admin,customer,guest,userInfo)
                        elif user_choice == 2:
                            get_payment(authenticate,admin,customer,guest,userInfo)
                        elif user_choice == 0:
                            authenticated(authenticate,admin,customer,guest,userInfo)
                        else:
                            print("Please Input a valid decision")
                elif user_choice == 5:  
                    return_vehicle(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 0:  
                    exit()
                else:
                    print("Invalid Command! \n")

    elif authenticate and customer:  # Customer
        r_customer_menu = ""
        r_customer_menu += f"\nWelcome back {userInfo[1]}!\nWhat you wish to proceed?:\n"
        r_customer_menu += "1. Access your page.\n"
        r_customer_menu += "2. Modified Personal Details.\n"
        r_customer_menu += "3. View Personal Rental History.\n"
        r_customer_menu += "4. Cars to be Rented Out.\n"
        r_customer_menu += "5. Book a Car.\n"
        r_customer_menu += "6. Make a Payment.\n"
        r_customer_menu += "0. Exit.\n"
        print(r_customer_menu)
        choice = ""
        while not choice.isnumeric():
            choice = input("Please Enter your Choice: ")
            if choice.isnumeric():
                user_choice = int(choice)
                if user_choice == 1:  
                    acc_access(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 2: 
                    acc_update(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 3:  
                    get_history(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 4: 
                    get_book(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 5: 
                    search_vehicle(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 6: 
                    get_payment(authenticate,admin,customer,guest,userInfo)
                elif user_choice == 0: 
                    exit()
            else:
                print("Invalid Command! \n")
    elif guest:
        run()

# Customer
def acc_access(authenticate,admin,customer,guest,user): # Checked
    with open("user.txt", "r") as ru:
        rur = ru.readlines()
        for info in rur:
            info = info.strip()
            accInfo = info.split(",")
            if accInfo[1] == user[1]:
                print(f"Welcome {accInfo[1]}!\n"
                        f"======================\n"
                        f"| Name: {accInfo[3]}\n"
                        f"| Gender:  {accInfo[4]}\n"
                        f"| Location:  {accInfo[5]}\n"
                        f"| Contact:  {accInfo[6]}\n"
                        f"======================\n")
    choice = input("Do you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

def acc_update(authenticate,admin,customer,guest,user): # Checked
    cache_Info = user
    line = 0
    with open("user.txt", "r") as cr:
        crr = cr.readlines()
        for info in crr:
            line += 1
            info = info.strip()
            accInfo = info.split(",")
            if accInfo == cache_Info:
                with open("user.txt", "w") as cw:
                    edit_choice = ""
                    while not edit_choice.isnumeric():
                        edit_choice = input("Which detail you want to edit?\n"
                                            "1. Username\n"
                                            "2. Password\n"
                                            "3. Location\n"
                                            "4. Contact\n"
                                            "Choice: ")
                        if edit_choice.isnumeric():
                            edit_choices = int(edit_choice)
                            if edit_choices == 1:
                                cache_Info[1] = input("Please Enter Your New Username: ")
                            elif edit_choices == 2:
                                cache_Info[2] = input("Please Enter Your New Password: ")
                            elif edit_choices == 3:
                                cache_Info[5] = input("Please Enter Your New Location: ")
                            elif edit_choices == 4:
                                cache_Info[6] = input("Please Enter Your New Contact: ")                                
                            crr[line - 1] = ",".join(str(Info) for Info in cache_Info) + "\n"
                        else:
                            print("Please input a valid choice!")
                    for lines in crr:
                        cw.writelines(lines)
    choice = input("Do you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

def acc_register(): # Checked
    New_Account = [0, 1, 2, 3, 4, 5, 6, 7]
    customer_register = open("user.txt", "a")
    with customer_register as r:
        New_Account[0] = "Customer"
        New_Account[1] = input("Please Enter Your Account Username: ").strip()
        New_Account[2] = input("Please Enter Your Account Password: ").strip()
        New_Account[3] = input("Please Enter Your Name: ").strip()
        New_Account[4] = input("What is your Gender: ").strip()
        New_Account[5] = input("Location: ").strip()
        New_Account[6] = input("Please Enter Your contact: ").strip()
        r.write("\n" + ",".join(str(Info) for Info in New_Account))
        print("Register Successfully")
    choice = input("Do you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        run()
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

# # Vehicles
def search_vehicle(authenticate,admin,customer,guest,user): # Checked Guest Admin Customer
    counter =0
    if guest:
        car_src = input("What Vehicle brand looking for?: ").strip()
        with open("vehicles.txt", "r") as v:
            for line in v.readlines():
                line = line.strip()
                vehicleInfo = line.split(",")
                if car_src == vehicleInfo[1]:
                    counter += 1
                    print(
                        f"Brand       : {vehicleInfo[1]}\n"
                        f"Model       : {vehicleInfo[2]}\n"
                        f"Price       : {vehicleInfo[5]}\n"
                        f"Availability: {vehicleInfo[0]}\n")
                elif car_src != vehicleInfo[0]:
                    continue
            if counter == 0:
                print("Invalid Vehicle! ")
            elif counter > 0:
                choice = input("You need to register to rent a vehicle.\nProceed to register?[Y/N]").capitalize()
                if choice == "Y":
                    acc_register()
                elif choice == "N":
                    exit()
    elif customer:
        with open("vehicles.txt", "r") as vr:
            vrr = vr.readlines()
            for line in vrr:
                line = line.strip()
                vehicleInfo = line.split(",")
                if "Available" == vehicleInfo[0]:
                    counter += 1
                    print(
                        f"\nPlate No  : {vehicleInfo[3]}\n"
                        f"Brand       : {vehicleInfo[1]}\n"
                        f"Model       : {vehicleInfo[2]} \n"
                        f"Day Rate    : {vehicleInfo[5]}\n"
                        f"Availability: {vehicleInfo[0]}")
                elif "Available" != vehicleInfo[0]:
                    continue
                else:
                    print("Invalid Vehicles for Rent")

        if counter > 0:
            choice = input("\nProceed to booking? [Y/N]: ").capitalize()
            if choice == "Y":
                get_available(authenticate, guest, customer, admin, user)
            elif choice == "N":
                run()
            else:
                print("Please Input a Valid Choice!")
        else:
            print("Invalid Vehicle For Booking!:")

    elif admin:
        print("Display all record of\n"
              "1.Cars Rented Out\n"
              "2.Cars available for Rent\n"
              "3.Customers Bookings\n"
              "4.Customer Payment for a specific duration\n"
              "0.Back\n")
        choice = ""
        while not choice.isnumeric():
            choice = input("Which record you want to display?: ")
            print("\n")
            if choice.isnumeric():
                user_choice = int(choice)
                if user_choice == 1:
                    get_rent(authenticate,admin,customer,guest,user)
                elif user_choice == 2:
                    get_available(authenticate,admin,customer,guest,user)
                elif user_choice == 3:
                    get_book(authenticate,admin,customer,guest,user)
                elif user_choice == 4:
                    get_paymentdate(authenticate,admin,customer,guest,user)
                elif user_choice == 0:
                   authenticated(authenticate,admin,customer,guest,user)
                else:
                    print("Please Input a valid decision")

    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")
# # Get Data
def get_book(authenticate,admin,customer,guest,user): # Checked Admin Customer
    rent_counter = 0
    if admin:
        with open("vehicles.txt", "r") as v:
            for rent in v.readlines():
                rent = rent.strip()
                vehicleInfo = rent.split(",")
                if vehicleInfo[0] == "Booked":
                    rent_counter += 1
                    print(
                    f"{rent_counter} {vehicleInfo[3]}\n" 
                    f"Brand: {vehicleInfo[1]}\n"
                    f"Model: {vehicleInfo[2]}\n"
                    f"Year : {vehicleInfo[4]}\n"
                    f"Rate : {vehicleInfo[5]}\n"
                    f"Status: {vehicleInfo[0]}")

            if rent_counter == 0:
                print("No vehicle had been rent!\n")
            print(f"\nThere is {rent_counter} vehicles has been booked.")

    elif customer:
        with open("vehicles.txt", "r") as v:
            for rent in v.readlines():
                rent = rent.strip()
                vehicleInfo = rent.split(",")
                if vehicleInfo[0] == "Booked" and user[1] == vehicleInfo[6]:
                    rent_counter += 1
                    print(
                    f"\n{rent_counter} {vehicleInfo[3]}\n" 
                    f"Brand: {vehicleInfo[1]}\n"
                    f"Model: {vehicleInfo[2]}\n"
                    f"Year : {vehicleInfo[4]}\n"
                    f"Rate : {vehicleInfo[5]}\n"
                    f"Status: {vehicleInfo[0]}")

            if rent_counter == 0:
                print("No vehicle had been rent!\n")
            print(f"\nThere is {rent_counter} vehicles has been booked.")
    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

def get_book2(authenticate,admin,customer,guest,user): # Checked Admin Customer
    rent_counter = 0
    if admin:
        with open("vehicles.txt", "r") as v:
            for rent in v.readlines():
                rent = rent.strip()
                vehicleInfo = rent.split(",")
                if vehicleInfo[0] == "Booked":
                    rent_counter += 1
                    print(
                    f"\n{rent_counter} {vehicleInfo[3]}\n" 
                    f"Customer       : {vehicleInfo[6]}\n"
                    f"Rent Day       : {vehicleInfo[9]}\n"
                    f"Remain Payment : {vehicleInfo[7]}\n"
                    f"Status         : {vehicleInfo[0]}")

            if rent_counter == 0:
                print("No vehicle had been rent!\n")
            print(f"\nThere is {rent_counter} vehicles has been booked.")

    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

def get_rent(authenticate,admin,customer,guest,user): # Checked
    rent_counter = 0
    with open("vehicles.txt", "r") as v:
        for rent in v.readlines():
            rent = rent.strip()
            vehicleInfo = rent.split(",")
            if vehicleInfo[0] == "Rented":
                rent_counter += 1
                print(
                    f"{rent_counter} {vehicleInfo[3]}\n" 
                    f"Brand: {vehicleInfo[1]}\n"
                    f"Model: {vehicleInfo[2]}\n"
                    f"Year : {vehicleInfo[4]}\n"
                    f"Rate : {vehicleInfo[5]}\n"
                    f"Status: {vehicleInfo[0]}")
        if rent_counter == 0:
            print("\nNo vehicle had been rent!\n")
        print(f"\nThere is {rent_counter} vehicles has been rented.")
    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

def get_payment(authenticate,admin,customer,guest,user): # Checked Admin Customer
    remaining = 0
    total = 0
    line = 0
    payment = False
    if admin:
        with open("vehicles.txt", "r") as vp:
            vpr = vp.readlines()
            for payment in vpr:
                payment = payment.strip()
                vehicleInfo = payment.split(',')
                if vehicleInfo[7] != "0":
                    remaining += 1
                    print(
                        f"{remaining} {vehicleInfo[6]}\n"
                        f"Remaining Payment: {vehicleInfo[7]}")
            if remaining == 0:
                print("\nNo Remaining Payment")
    elif customer:
        with open("vehicles.txt", "r") as vp:
            vpr = vp.readlines()
            for payment in vpr:
                payment = payment.strip()
                vehicleInfo = payment.split(',')
                if vehicleInfo[6] == user[1] and vehicleInfo[7] != "0":
                    remaining += 1
                    total += int(vehicleInfo[7])
                    print(
                        f"\n{remaining}\n"
                        f"Plate: {vehicleInfo[3]}\n" 
                        f"Brand: {vehicleInfo[1]}\n"
                        f"Model: {vehicleInfo[2]}\n"
                        f"Year : {vehicleInfo[4]}\n"
                        f"Rate : {vehicleInfo[5]}\n"
                        f"Status: {vehicleInfo[0]}\n"
                        f"Remaining Payment: {vehicleInfo[7]}")
                
            if total == 0:
                print("\nNo Remaining Payment")

            elif total > 0: 
                print(f"\nYou have {remaining} for payment, Total: {total}\n")
                plate = input("Please Enter Vehicle Plate for Payment: ") 
                for made_payment in vpr:
                    line += 1
                    made_payment = made_payment.strip()
                    vehicleInfo = made_payment.split(',')      
                    if vehicleInfo[3] == plate and vehicleInfo[6] == user[1]:
                        with open("vehicles.txt", "w") as wvr:
                            print(f"Your remaining payment is {int(vehicleInfo[7])}")
                            payment_made = int(input("Please Enter Amount pay: "))
                            if payment_made == int(vehicleInfo[7]):
                                vehicleInfo[7] = int(vehicleInfo[7]) - payment_made
                                vehicleInfo[8] = datetime.date.today()
                                vpr[line - 1] = ",".join(str(Info) for Info in vehicleInfo) + "\n"
                                print("\nPaid Successfully")
                                for lines in vpr: 
                                    wvr.writelines(lines)
                                return payment == True
                    
                            elif payment_made < int(vehicleInfo[7]):
                                print("You must pay remaining amount!")


                            elif payment_made > int(vehicleInfo[7]):
                                print("Please Input an Valid Amount!")

                if payment:
                    print("\nPlease Input a valid Vehicle!") 

                        
                        
    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

def get_paymentdate(authenticate,admin,customer,guest,user): # Checked Admin
    remaining = 0
    if admin:
        inputdate = int(input("What duration of payment you're looking for?: "))
        time_delta = datetime.timedelta(days=1)
        startdate = datetime.date.today()
        enddate = startdate + inputdate*time_delta
        with open("vehicles.txt", "r") as vp:
            vpr = vp.readlines()
            for payment in vpr:
                payment = payment.strip()
                paymentInfo = payment.split(',')
                for i in range((enddate - startdate).days):
                    if paymentInfo[8] == str(startdate - i*time_delta):
                        remaining += 1
                        print(
                            f"\n{remaining} {paymentInfo[6]}\n"
                            f"Last Payment Date: {paymentInfo[8]}\n"
                            f"Remaining Payment: {paymentInfo[7]}")
                    elif paymentInfo[8] == "time":
                        continue

            if remaining == 0:
                print(f"\nNo Payment Record for Recent {inputdate} days.")

    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")
    
def get_available(authenticate,admin,customer,guest,user): # Bugged Triggered
    line = 0
    counter = 0
    vehicle = []
    if customer:
        plate = input("Which vehicle you would like to rent?\nEnter Car Plate No: ")
        with open("vehicles.txt", "r") as v:
            get_vr = v.readlines()
            for rent in  get_vr:
                line += 1
                rent = rent.strip()
                rentInfo = rent.split(",")
                if rentInfo[3] == plate and rentInfo[0] == "Available":
                    days = int(input("\nHow Many days you want to rent: "))
                    with open ("vehicles.txt", "w+") as vw:
                        vehicle += rentInfo
                        vehicle[0] = "Booked"
                        vehicle[6] = user[1]
                        vehicle[7] = (int(rentInfo[5]) * days)
                        vehicle[8] = datetime.date.today()
                        vehicle[9] = days
                        print(f"\nYour Total Payment is {vehicle[7]}\n"
                            "\nPlease choose your payment method.\n"
                            "1. Down-Payment\n"
                            "2. Full-Payment ")
                        payment_choice = ""
                        while not payment_choice.isnumeric():
                            payment_choice = input("Choice:  ")
                            if payment_choice.isnumeric():
                                choice = int(payment_choice)
                                min = int(int(vehicle[7]) * 20/100)
                                convert_payment = ""
                                while not convert_payment.isnumeric():
                                    if choice == 1: 
                                        print(f"\nPlease pay your Down payment with minimum {min}") 
                                        convert_payment = input("Please enter Amount: ")
                                        if convert_payment.isnumeric():
                                            payment = int(convert_payment)
                                            if payment >= min and not payment >= int(vehicle[7]):
                                                vehicle[7] = int(vehicle[7]) - payment
                                                get_vr[line - 1] = ",".join(str(Info) for Info in vehicle) + "\n"
                                                print("\nBook Successfully")
                                                for lines in get_vr:
                                                    vw.writelines(lines)

                                            elif payment > int(vehicle[7]):
                                                print("\nBooked Fail! You've overpaid!")

                                            elif payment < min:
                                                print(f"\nBooked Fail! You must pay a minimum {int(vehicle[7])*20/100}!")
                                            
                                            else: 
                                                print("\nPlease Input a valid Amount!")

                                    elif choice == 2:
                                        print(f"Your Total Payment is {int(vehicle[7])}") 
                                        payment = int(input("Please enter Amount: "))
                                        if payment == int(vehicle[7]):
                                            vehicle[7] = int(vehicle[7]) - payment
                                            get_vr[line - 1] = ",".join(str(Info) for Info in vehicle) + "\n"
                                            print("\nBook Successfully")
                                            for lines in get_vr:
                                                vw.writelines(lines)
                                            break
                                        elif payment > int(vehicle[7]):
                                            print("\nBooked Fail! You've overpaid!")

                                        elif payment < int(vehicle[7]):
                                            print(f"\nYou must pay full!")
                                            
                                        else: 
                                            print("\nPlease Input a valid Amount!")

                            else: 
                                print("Please input a valid Choice!")

                    if counter < 0 :
                        print("\nPlease Input a Valid Vehicle Plate No.!!!")
                                                                                                                    
    elif admin:
        counter = 0 
        with open("vehicles.txt", "r") as vr:
            vrr = vr.readlines()
            for line in vrr:
                line = line.strip()
                vehicleInfo = line.split(",")
                if "Available" == vehicleInfo[0]:
                    counter += 1
                    print(
                        f"\n{counter}\n"
                        f"Plate: {vehicleInfo[3]}\n" 
                        f"Brand: {vehicleInfo[1]}\n"
                        f"Model: {vehicleInfo[2]}\n"
                        f"Year : {vehicleInfo[4]}\n"
                        f"Rate : {vehicleInfo[5]}\n"
                        f"Status: {vehicleInfo[0]}")
                elif "Available" != vehicleInfo[0]:
                    continue
                else:
                    print("Invalid Vehicles for Rent")
            print(f"\nThere is {counter} vehicles available for rent.\n")
    
    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

def get_history(authenticate,admin,customer,guest,user): # Checked
    his_counter = 0
    if customer:
        with open("history.txt", "r") as v:
            vr = v.readlines()
            for history in vr:
                history = history.strip()
                hisInfo = history.split(",")
                if hisInfo[6] == user[1]:
                    his_counter += 1
                    print( 
                        f"\n{his_counter} {hisInfo[3]}\n" 
                        f"Brand: {hisInfo[1]}\n"
                        f"Model: {hisInfo[2]}\n"
                        f"Year : {hisInfo[4]}\n"
                        f"Rate : {hisInfo[5]}\n"
                        f"Status: {hisInfo[0]}")    

            if his_counter == 0:
                print("No vehicle had been rent before!\n")
            print(f"\nYou have rented {his_counter} vehicles before.")

    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

    choice = input("Do you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

# # For Adming Only
def add_vehicle(authenticate,admin,customer,guest,user): # Checked # 1 Bug Found input Y/N
    Admin_Add = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    New_Add = []
    Add = True
    Count = 0
    while Add:
        if Add:
            Admin_vehicles = open ("vehicles.txt", "a")
            with Admin_vehicles as r:
                Count += 1
                Admin_Add[0] = "Available"
                Admin_Add[1] = input("Enter Car Brand: ")
                Admin_Add[2] = input("Enter Car Model: ")
                Admin_Add[3] = input("Enter Car Plate Number: ")
                Admin_Add[4] = input("Enter Car Year: ")
                Admin_Add[5] = input("How much is the Car Price: ")
                Admin_Add[6] = "'customer'"
                Admin_Add[7] = "0"
                Admin_Add[8] = "'time'"
                New_Add.append(",".join(str(Info) for Info in Admin_Add))
                choice = ""
                while not choice: 
                    choice = input("\nDo you want to continue add more vehicles?[Y/N]: ").capitalize()
                    if choice == "Y":
                        continue
                    elif choice == "N": 
                        Add = False
                        for v_element in New_Add:
                            r.write("".join(str(Info) for Info in v_element)+ "\n")
                    else:
                        print("Please input [Y/N]!!!")
                
    if not Add:
        choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
        if choice == "Y":
            authenticated(authenticate,admin,customer,guest,user)
            
        elif choice == "N": 
            exit()
        else:
            print("Please input [Y/N]!!!")
            
def update_vehicle(authenticate,admin,customer,guest,user): # Checked
    line = 0
    edit = False
    cache_vehicle = []
    with open("vehicles.txt", "r") as uv:
        uvr = uv.readlines()
        for vehicles in uvr:
            vehicles = vehicles.strip()
            vehicleInfo = vehicles.split(",")
            if vehicles:
                line +=1
                print( 
                    f"Plate: {vehicleInfo[3]}\n" 
                    f"Brand: {vehicleInfo[1]}\n"
                    f"Model: {vehicleInfo[2]}\n"
                    f"Year : {vehicleInfo[4]}\n"
                    f"Rate : {vehicleInfo[5]}\n"
                    f"Status: {vehicleInfo[0]}\n")

    while not edit:
        plate = input("\nPlease enter vehicle plate you want to modify: ")
        with open("vehicles.txt", "r") as uv:
            uvr = uv.readlines()
            for vehicles in uvr:
                vehicles = vehicles.strip()
                vehiclesInfo = vehicles.split(",")
                if plate == vehiclesInfo[3]:
                    edit = True
                    cache_vehicle = vehiclesInfo
                    if edit:
                        with open ("vehicles.txt", "w") as vw:
                            choice = ""
                            while not choice.isnumeric():
                                print("\nWhich Vehicle you want to modified?\n"
                                                "1.Brand\n"
                                                "2.Model\n"
                                                "3.Plate\n"
                                                "4.Year\n"
                                                "5.Rate\n"
                                                "0.Cancel Modify")
                                choice = input("Input your Choice: ")
                                if choice.isnumeric():
                                    choices = int(choice)
                                    if choices == 1:
                                        cache_vehicle[1] = input("Please Enter Your New Car Brand: ")
                                    elif choices == 2:
                                        cache_vehicle[2] = input("Please Input Your New Car Model: ")
                                    elif choices == 3:
                                        cache_vehicle[3] = input("Please Input Your New Car Plate: ")
                                    elif choices == 4:
                                        cache_vehicle[4] = input("Please Input Your Year Made: ")
                                    elif choices == 5:
                                        cache_vehicle[5] = input("Please Input New Day Rates: ")
                                    elif choices == 0:
                                        exit()   
                                    else:
                                        print("Invalid Choice! Please Input again")
                                uvr[line - 1] = (",".join(str(info) for info in cache_vehicle)+ "\n")
                            for lines in uvr:
                                vw.writelines(lines)
                    
                elif plate == "0":
                    exit()
                else:
                    print("\nInvalid Vehicle for modified")
            
    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
        
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")

def return_vehicle(authenticate,admin,customer,guest,user): # Checked
    rent_counter = 0
    returned_vehicle = []
    history_vehicle = []
    line = 0
    with open("vehicles.txt", "r") as rev:
        get_rev = rev.readlines()
        for rented in get_rev:
            rented = rented.strip()
            vehicleInfo = rented.split(",")
            if vehicleInfo[0] == "Rented":
                rent_counter += 1
                print( 
                f"\n{rent_counter} {vehicleInfo[6]}\n" 
                f"Plate     : {vehicleInfo[3]}\n"
                f"Brand     : {vehicleInfo[1]}\n"
                f"Model     : {vehicleInfo[2]}\n"
                f"Year      : {vehicleInfo[4]}\n"
                f"Remaining : {vehicleInfo[7]}\n"
                f"Status    : {vehicleInfo[0]}")               

    plate = input("\nPlease Enter Returned Vehicle Plate No: ")          
    with open("vehicles.txt", "r") as rev:
        get_rev = rev.readlines()
        for rented in get_rev:
            line += 1
            rented = rented.strip()
            vehicleInfo = rented.split(",")
            if vehicleInfo[3] == plate:
                with open("vehicles.txt", "w") as wev:
                    returned_vehicle += vehicleInfo
                    history_vehicle += vehicleInfo
                    if int(vehicleInfo[7]) != 0:
                        print( 
                            f"\n{rent_counter} {vehicleInfo[6]}\n" 
                            f"Remaining : {vehicleInfo[7]}\n"
                            f"Status    : {vehicleInfo[0]}")

                        Payment = int(input("\nHow much customer Pay?: "))
                        if Payment == int(vehicleInfo[7]):
                            print("\nPayment Resolve")
                            Remaining = int(returned_vehicle[7]) - Payment
                            returned_vehicle[0] = "Available"
                            returned_vehicle[6] = "''"
                            returned_vehicle[7] = Remaining
                            returned_vehicle[8] = "Time"
                            returned_vehicle[9] = "Day"
                        get_rev[line - 1] = ",".join(str(returned) for returned in returned_vehicle) + "\n"
                    elif int(vehicleInfo[7]) == 0:
                        print("Payment Resolve")
                        returned_vehicle[0] = "Available"
                        returned_vehicle[6] = "'customer'"
                        returned_vehicle[7] = "0"
                        returned_vehicle[8] = "Time"
                        returned_vehicle[9] = "Day"
                        get_rev[line - 1] = ",".join(str(returned) for returned in returned_vehicle) + "\n"
                    for lines in get_rev:
                        wev.writelines(lines)
                    
                    with open("history.txt", "a") as ah:
                        history_vehicle[0] = "Returned"
                        history_vehicle[7] = int(history_vehicle[5]) * int(history_vehicle[9])
                        history_vehicle[8] = datetime.date.today()
                        ah.write(",".join(str(returned) for returned in history_vehicle) + "\n")
    
    choice = input("\nDo you want proceed to main menu or exit?[Y/N]: ").capitalize()
    if choice == "Y":
        authenticated(authenticate,admin,customer,guest,user)
    elif choice == "N": 
        exit()
    else:
        print("Please input [Y/N]!!!")


run()