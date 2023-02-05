#Run this file to set up the cockroach database and tables
# uses Sean's cockroach account I think

import DBfunctions as DBfuncs

if __name__=="__main__":
    print("Running ServerSetup.py")
    print("Running set_database()...")
    DBfuncs.set_database()
    print("Running create_tables()...")
    DBfuncs.create_tables()
    print("Finished setup.")


    DBfuncs.print_database_logistics()