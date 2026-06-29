# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Football_girls_team_info.db'

# This is the SQL to connect to all the tables in the database - only needed if you are using a parameter query (Excellence)
TABLES = (" Football_team_info "
           "LEFT JOIN Goals_scored ON Football_team_info.Goals_scored_id = Goals_scored.Goals_scored_id "
           "LEFT JOIN Positions ON Football_team_info.Position_id = Positions.Position_id ")


def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()


def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. 
        Only required for Excellence """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()  

menu_choice = ''
while menu_choice != "Z":
    menu_choice = input('\n\nWelcome to the FC twenty eleven U15 girls football team database!\n\n'
                        'Type the letter for the information you want:\n'
                        'A: All_data\n'
                        'B: Club_veterans\n'
                        'C: Girls_injuries\n'
                        'D: No_shirt_num\n'
                        'E: Scout_qualifications\n'
                        'F: Shirt_num\n'
                        'Z: To Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('All_data')
    elif menu_choice == 'B':
        print_query('Club_veterans')
    elif menu_choice == 'C':
        print_query('Girls_injuries')
    elif menu_choice == 'D':
        print_query('No_shirt_num')
    elif menu_choice == 'E':
        print_query('Scout_qualifications')
    elif menu_choice == 'F':
        print_query('Shirt_num')        