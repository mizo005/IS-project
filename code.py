with open('users.txt', "r") as userFile:
    all_user_content = userFile.readlines()

with open('admins.txt', 'r') as adminFile:
    all_admin_content = adminFile.readlines()

with open("Centers.txt", 'r') as centersFile:
    all_centers_content = centersFile.readlines()

with open("requests.txt", 'r') as requestsFile:
    all_requests = requestsFile.readlines()

with open("reservation.txt") as allReservations:
    all_reservations = allReservations.readlines()

user_names = []
for i in range(0, len(all_user_content), 7):
    user_names.append(all_user_content[i].rstrip('\n'))
user_id = []
for i in range(1, len(all_user_content), 7):
    user_id.append(all_user_content[i].rstrip('\n'))
user_nat_id = []
for i in range(2, len(all_user_content), 7):
    user_nat_id.append(all_user_content[i].rstrip('\n'))
user_passwords = []
for i in range(3, len(all_user_content), 7):
    user_passwords.append(all_user_content[i].rstrip('\n'))
user_email = []
for i in range(4, len(all_user_content), 7):
    user_email.append(all_user_content[i].rstrip('\n'))
user_phone = []
for i in range(5, len(all_user_content), 7):
    user_phone.append(all_user_content[i].rstrip('\n'))

admin_names = []
for i in range(0, len(all_admin_content), 5):
    admin_names.append(all_admin_content[i].rstrip('\n'))
admin_id = []
for i in range(1, len(all_admin_content), 5):
    admin_id.append(all_admin_content[i].rstrip('\n'))
admin_passwords = []
for i in range(2, len(all_admin_content), 5):
    admin_passwords.append(all_admin_content[i].rstrip('\n'))
admin_email = []
for i in range(3, len(all_admin_content), 5):
    admin_email.append(all_admin_content[i].rstrip('\n'))

centers_names = []
for i in range(0, len(all_centers_content), 5):
    centers_names.append(all_centers_content[i].rstrip('\n'))

reserve_names = []
for i in range(0, len(all_reservations), 5):
    reserve_names.append(all_reservations[i].rstrip('\n'))

rqst_names= []
for i in range(0, len(all_requests), 4):
    rqst_names.append(all_requests[i].rstrip('\n'))

def admin_do():
    while True:
        print("\nHere is the options menu: \n1. Vaccination Centers\n2. Search Centers\n3. Edit Centers\
\n4. See Reservations\n5. See Requests\n6. Approve Requests\n7. List Users\n8. Exit")
        option = input("Enter your choice: ")
        if option.strip() == '1': # OPTION 1 print Vaccination Centers
            with open("Centers.txt", 'r') as centersFile:
                all_centers_content = centersFile.readlines()
            for item in all_centers_content:
                print(item.rstrip("\n"))

        elif option.strip() == '2': # OPTION 2 Search
            with open("Centers.txt", 'r') as centersFile:
                all_centers_content = centersFile.readlines()
            centers_names = []
            for i in range(0, len(all_centers_content), 5):
                centers_names.append(all_centers_content[i].rstrip('\n'))

            try:
                choice = input("Enter the name of the center: ")
                cntr_indx = centers_names.index(choice) * 5 # multiply because at slicing the indexes doesn't match
                # and it will give an error if i used the returned list from readlines() directly due to missing ('\n')
                output = all_centers_content[cntr_indx:cntr_indx+5] # +5 to get the next 4
                for i in output:
                    print(i.strip('\n'))
            except:
                print("Not Found")

        elif option.strip() == '3': # OPTION 3 Edit
            with open("Centers.txt", 'r') as centersFile:
                all_centers_content = centersFile.readlines()
                centers_names = []
                for i in range(0, len(all_centers_content), 5):
                    centers_names.append(all_centers_content[i].rstrip('\n'))

            print("1) Add\n2) Remove\n3) Exit")
            choice = input("Your choice: ")
            if choice.strip() == '1':
                print("You have to specify the name, ID, address and vaccines of the Center: ")
                center_name = input("Enter the Center name: ")
                center_id = input("Enter the Center ID: ")
                center_address = input("Enter the Center address: ")
                center_vaccines = input("Enter the Center vaccines: ")
                with open("Centers.txt", 'a') as addCenter:
                    addCenter.write(f"\n{center_name}")
                    addCenter.write(f"\n{center_id}")
                    addCenter.write(f"\n{center_address}")
                    addCenter.write(f"\n{center_vaccines}\n")
            elif choice.strip() == '2':
                ask = input("Enter the name of the Center you want to delete: ")
                try:
                    cntr_indx = centers_names.index(ask) * 5
                except:
                    print("Not Found")
                del all_centers_content[cntr_indx:cntr_indx+5]
                with open("Centers.txt", 'w') as f:
                    for i in all_centers_content:
                        f.write(i)

            elif choice.strip() == '3':
                pass
            else:
                print("\nInvalid Value")

        elif option.strip() == '4': # OPTION 4 Reservations
            with open("reservation.txt") as allReservations:
                all_reservations = allReservations.readlines()
            for reservation in all_reservations:
                print(reservation.strip('\n'))
        elif option.strip() == '5': # OPTION 5 Requests
            with open("requests.txt", 'r') as requestsFile:
                all_requests = requestsFile.readlines()
            for rqst in all_requests:
                print(rqst.rstrip("\n"))
        elif option.strip() == '6': # OPTION Add Date
            with open("requests.txt", 'r') as requestsFile:
                all_requests = requestsFile.readlines()
            rqst_names= []
            for i in range(0, len(all_requests), 4):
                rqst_names.append(all_requests[i].rstrip('\n'))
            print("First you have to specify the name of the user and the date:")
            user = input("Enter the name of the user: ")
            date = input("Specify the date: ")
            usr_indx = rqst_names.index(user) * 4
            rqst_slice = all_requests[usr_indx:usr_indx+4]
            rqst_slice.append(date)

            del all_requests[usr_indx:usr_indx+4]
            with open("requests.txt", 'w') as f:
                for i in all_requests:
                    f.write(i)

            with open("reservation.txt", 'a') as f:
                for i in rqst_slice:
                    f.write(i)
        elif option.strip() == '7': # OPTION 7 Users
            for usr in user_names:
                print(usr)
        elif option.strip() == '8': # OPTION 8 Exit
            break
        else:
            print("Invalid value")

def user_do(user_name):
    while True:
        print("\nHere is the options menu: \n1. Vaccination Centers\n2. Reserve a vaccination\n3. See Resevation details\n4. Exit")
        option = input("Enter your choice: ")

        if option.strip() == '1':
            with open("Centers.txt", 'r') as centersFile:
                all_centers_content = centersFile.readlines()
            for item in all_centers_content:
                print(item.rstrip("\n"))

        elif option.strip() == '2':
            print("To reserve a vaccination you should specify where the center is and the vaccine name: ")
            get_center = input("Enter the name of the center: ")
            get_vaccine = input("Enter the name of the vaccine: ")
            ch = input("Do you want to proceed in reservation? (y/n): ").strip().lower()
            if ch == 'y':
                f = open('requests.txt', 'a')
                f.write(f"\n{user_name}")
                f.write(f"\n{get_center}")
                f.write(f"\n{get_vaccine}\n")
                f.close()
                print("Reservation finished, Wait for determining the date")
            elif ch == 'n':
                pass
            else: print("Invalid input")

        elif option.strip() == '3':
            with open("requests.txt", 'r') as requestsFile:
                all_requests = requestsFile.readlines()
            with open("reservation.txt") as allReservations:
                all_reservations = allReservations.readlines()

            reserve_names = []
            for i in range(0, len(all_reservations), 5):
                reserve_names.append(all_reservations[i].rstrip('\n'))
            rqst_names= []
            for i in range(0, len(all_requests), 4):
                rqst_names.append(all_requests[i].rstrip('\n'))


            try:
                rsv_indx = reserve_names.index(user_name) * 5
                reserve_details = all_reservations[rsv_indx:rsv_indx+5]
                for det in reserve_details:
                    print(det.rstrip("\n"))
            except:
                try: 
                    rqst_indx = rqst_names.index(user_name) * 4
                    rqst_details = all_requests[rqst_indx:rqst_indx+4]
                    print("\nStill waiting for determining the date")
                    for i in rqst_details:
                        print(i.rstrip("\n"))
                except:
                    print('\nNot Found')
        elif option.strip() == '4':
            break
        else: print("Invalid input")

def register():
    name = input("Please Enter a username: ")
    f = open('users.txt', 'a')
    f.write(f"\n{name}")

    user_id = input("Please Enter your ID: ")
    f.write(f"\n{user_id}")

    national_id = input("Please enter your national id: ")
    f.write(f"\n{national_id}")

    password = input("Please Enter a strong password: ")
    f.write(f"\n{password}")

    email = input("Please Enter your email: ")
    f.write(f"\n{email}")

    phone_number = input("Please enter your phone number: ")
    f.write(f"\n{phone_number}\n")
    f.close()

def login():
    while True:
        option = input("Do you want to log in as an admin or a user?\nType 'a' for admin and 'u' for user: ")
        if option.strip().lower() == 'a':
            get_name = input("Enter your name: ")
            get_id = input("Enter your ID: ")
            get_password = input("Enter your password: ")
            if admin_names.count(get_name) and admin_id.count(get_id) and admin_passwords.count(get_password):
                print(f'\nWelcome {get_name}')
                admin_do()
                break
            else:
                print('\nNot found')

        elif option.strip().lower() == 'u':
            get_name = input("Enter your username: ")
            get_id = input("Enter your ID: ")
            get_password = input("Enter your password: ")
            if user_names.count(get_name) and user_id.count(get_id) and user_passwords.count(get_password):
                print(f"\nWelcome {get_name}")
                user_do(get_name)
                break
            else:
                print("\nNot foud")
        else:
            print("\nInvalid value")

print("Welcome to the Vaccination Scheduling Program!")
print("First you need to Sign in or Sign up\n")

while True:
    option = input("To Sign in press 1\nTo Sign up press 2\nTo exit press 0\n\nYour choice: ")
    if option.strip() == '1':
        login()
        break
    elif option.strip() == '2':
        register()
        break
    elif option.strip() == '0':
        break
    else:
        print("\nInvalid value")
