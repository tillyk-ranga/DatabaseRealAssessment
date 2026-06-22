# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Football_girls_team_info.db'

# This is the SQL to connect to all the tables in the database - only needed if you are using a parameter query (Excellence)
TABLES = (" fast_cars "
           "LEFT JOIN makes ON fast_cars.make_id = makes.make_id "
           "LEFT JOIN aspiration ON fast_cars.aspiration_id = aspiration.aspiration_id "
           "LEFT JOIN cylinders ON fast_cars.cylinders_id = cylinders.cylinders_id ")


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

