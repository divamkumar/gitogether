import DBfunctions as DBfuncs

if __name__=="__main__":
    print("Running ServerSetup.py")
    print("Running set_database()...")
    DBfuncs.set_database()

    print("Running create_tables()...")
    DBfuncs.create_tables()

    print("Finished.")

    DBfuncs.print_database_logistics()