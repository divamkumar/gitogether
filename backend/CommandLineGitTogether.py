import DBfunctions as dbf


if __name__ == '__main__':
    dbf.set_database()
    dbf.create_tables()

    while True:
        command = input("Next command ['i'='new_user', 'p'='print_database_logistics',\
        'q'='quit this program', 'g'='get_matches', 'd'='delete_user']")
        if command == 'q':
            print("End.")
            break
        if command == 'i':
            username = input("Enter Git username: ")
            fullname = input("Enter your full name: ")
            password = input("Set a password: ")
            dbf.new_user(username, fullname, password)
        elif command == 'p':
            dbf.print_database_logistics()
        elif command == 'g':
            username = input("Enter username ")
            matches = dbf.get_matches(username)
            if matches:
                print(matches)
            else:
                print("sorry cap there's no one for this guy")
        elif command == 'd':
            username = input("Enter Git username to erase from db: ")
            dbf.delete_user_completely(username)
            print(username, 'removed from GitTogether')