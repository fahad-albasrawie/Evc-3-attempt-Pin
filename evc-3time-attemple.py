# !pthon 3.11.
# This program lets EVC-user to attempt their PIN more than one 

# this code make connection to the EVC DB
db_code = '*770#'
user_db_pin = '1234'

# display keybad
print('Welcome to HORMUUD EVC Plus Dachboard')
print("1\t2\t3\n4\t5\t6\t\n7\t8\t9\t\n*\t0\t#\n")

# ask your db code
user_db_code = input("")

if user_db_code == db_code:

    # allow the user to try entering pin another time
    for attempt in range(3):
        print("Fadlan geli binkaaga (PIN): ")
        # ask your pin
        user_pin = input()
        if user_pin == user_db_pin:
            print("1. Intus haraagaaga.")
            print("2. Kaarka hadalka.")
            print("3. Bixi biil.")
            print("4. U wareeji EVC PLus.")
            print("5. Warbixin kooban.")
            break
    else:
        print('Macsalama')
        
else:
    print("MISS connection Error")



    

