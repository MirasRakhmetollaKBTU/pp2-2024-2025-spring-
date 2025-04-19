

from   functions import *


if __name__ == '__main__':

    going = True
    while going:
        print('Choose an option\n\n1 - Insert from console\n2 - Upload from CSV file\n3 - Update date\n4 - Query Date\n5 - Deletion\n6 - custom commands\n7 - Select part of date (offset / limit)\n8 - Exit')
        choice = input("\nEnter option [1/2/3/4/5/6/7/8]: ")

        if   choice == '1': insert_from_console()
        elif choice == '2': insert_from_csv('CSV_DATA.csv')
        elif choice == '3': update_date()
        elif choice == '4': query_data()
        elif choice == '5': delete_entry()
        elif choice == '6': run_custom_sql()
        elif choice == '7': select_part_of_data()
        elif choice == '8': print("\nProcess ended.\n"); going = False
        else: print("\nInvalid choice.\n")
