import random
import sqlite3

#create database

connetion = sqlite3.connect('scrbs.db')

#cteate tables
with sqlite3.connect() as connection:
    cursor = connection.cursor()

    createResourcesTable = '''
        CREATE TABLEIF NOT EXISTS resources(
            resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
            resource_code TEXT,
            capacity INTEGER DEFAULT 0,
            is_available INTEGER DEFAULT 1,
            FOREIGN KEY (campus_id) REFERENCES campuses(campus_id)
        )   
    '''

    createUsersTable = '''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            name_surname NOT NULL
            email TEXT NOT NULL
            created_at TIMESTAMP DEAFAULT CURRENT_TIMESTAMP
        )
    '''

    createCampusTable = '''
        CREATE TABLE IF NOT EXISTS campuses(
            campus_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT
            )
    '''
    createBookingsTable = '''
        CREATE TABLE IF NOT EXISTS bookings(
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            resource_code TEXT NOT NULL,
            user_id TEXT NOT,
            campus_id INTEGER NOT NULL,
            booking_date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            duraton TEXT NOT NULL,
            status TEXT DEFAULT 'active',
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (resourse_id) REFERENCES resources(resources_id),
            FOREIGN KEY (campus_id) REFERENCES campuses(campus_id)
            )
'''

    cursor.execute(createCampusTable)
    cursor.execute(createUsersTable)
    cursor.execute(createBookingsTable)
    cursor.execute(createBookingsTable)
    connection.commit()