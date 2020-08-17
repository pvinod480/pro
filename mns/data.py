# import sqlite3

# try:
#     sqliteConnection = sqlite3.connect('mns_database.db')
#     sqlite_create_table_query = '''CREATE TABLE Agent (
#                                 sno INTEGER ,
#                                 agent TEXT NOT NULL PRIMARY KEY,
#                                 amount text NOT NULL );'''
#
#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")
#     cursor.execute(sqlite_create_table_query)
#     sqliteConnection.commit()
#     print("SQLite table created")
#
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Error while creating a sqlite table", error)
# finally:
#     if (sqliteConnection):
#         sqliteConnection.close()
#         print("sqlite connection is closed")


import sqlite3
import traceback
import sys

try:
    sqliteConnection = sqlite3.connect('mns_database.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = "deletebyagent(vinod)"

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table")
    print("Exception class is: ", error.__class__)
    print("Exception is", error.args)
    print('Printing detailed SQLite exception traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
