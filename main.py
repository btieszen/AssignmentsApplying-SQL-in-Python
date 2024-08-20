#Lesson 3: Applying SQL in Python
import re

#Task 1 add a member
#ADDS A MEMBER
def add_member(name,age):    
    from connect_mysql import connect_database 
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            new_member=name
            new_age=age
        #Checks to see if member exist  from MySql  
            check_query="SELECT name FROM Members WHERE name =%s"
            cursor.execute(check_query,(new_member,))
            members = cursor.fetchone()
            if  members:
                print("Member already exist")
        #Adds new member to database
            else:
                cursor=conn.cursor()
                member_age=(name),(age)
                query = "INSERT INTO Members (name,age) VALUES (%s,%s)"
                cursor.execute(query,member_age)
                conn.commit()
                print("New member has been added")
        finally:
            cursor.close()
            conn.close()
            
 # Adds workout session    
def add_workout_session(date,duration_minutes,calories_burned,member_id):
    from connect_mysql import connect_database 
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
        #Checks to see if workout session exist fro MySql
            new_session=member_id
            check_query="SELECT member_id FROM Workoutsessions WHERE member_id =%s"
            cursor.execute(check_query,(new_session,))
            workoutsessions = cursor.fetchone()
            if not workoutsessions:
                print("Member id does not exist")
            else:
        #Adds new workout session to database
                cursor=conn.cursor()
                dates=(date)
                minutes=(duration_minutes)
                calories=(calories_burned)
                new_session=(member_id)
                query = "INSERT INTO Workoutsessions (date,duration_minutes,calories_burned,member_id) VALUES (%s,%s,%s,%s)"
                cursor.execute(query, (dates,minutes,calories,new_session, ))
                conn.commit()
                print("New Workout session has been added")
        finally:
            cursor.close()
            conn.close()
            
#UPDATES MEMBERS AGE
def update_member_age(id,age):
    from connect_mysql import connect_database 
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
        #Checks to see if member is in database
            new_member=id
            check_query="SELECT name FROM Members WHERE id =%s"
            cursor.execute(check_query,(new_member,))
            members = cursor.fetchone()
            if  not members:
                print("Member does not exist")
            else:
        #updates members age
                cursor=conn.cursor()
                update_age=(age),(id)
                query = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(query,update_age)
                conn.commit()
                print("Members age has been updated")
        finally:
            cursor.close()
            conn.close()
            
#DELETES WORKOUT SESSIONS

def delete_workout_session(session_id):
            
    from connect_mysql import connect_database 
    conn = connect_database()
    if conn is not None:
        try:
        #Checks to see if workoutsession exist in database
            cursor=conn.cursor()
            session=session_id
            check_query="SELECT id FROM Workoutsessions WHERE id =%s"
            cursor.execute(check_query,(session, ))
            workoutsessions = cursor.fetchone()
            if  not workoutsessions:
                print("Workout Sessions does not exist")
            else:
        #Deletes session from database
                cursor=conn.cursor()
                sessions= (session_id)
                query = "Delete FROM workoutsessions WHERE id = %s"
                cursor.execute(query,(sessions, ))
                conn.commit()
                print("Deleted")
        finally:
            cursor.close()
            conn.close()

# Displays All Members

def display_all_members():
    from connect_mysql import connect_database
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query ="SELECT * FROM Members"
            cursor.execute(query)
            for row in cursor.fetchall():
                print("Member Id,Name,Age")
                print (row)
        finally:
            cursor.close()
            conn.close()
            
#DISPLAYS ALL WOROUT SESSSIONS
def display_workoutsessions():
    from connect_mysql import connect_database
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query ="SELECT * FROM Workoutsessions"
            cursor.execute(query)
            for row in cursor.fetchall():
                print('Date,minutes,calories burned, member id')
                print (row)
        finally:
            cursor.close()
            conn.close()
            
# finds members with a date range            
def get_members_in_age_range(start_age, end_age):
   
    from connect_mysql import connect_database
    conn = connect_database()
    start_age="25"
    end_age="30"
    if conn is not None:
        try:
            cursor=conn.cursor()
            query ="SELECT * FROM Members WHERE age BETWEEN 25 and 30"
            cursor.execute(query)
            for row in cursor.fetchall():
                print("Member Id,Name,Age")
                print (row)
        finally:
            cursor.close()
            conn.close()





#Main Menu
def main():
    while True:
        print("\nWelcome to the Gym")
        print("1. Add a member")
        print("2. Add Workout Session")
        print("3. Update member Info")
        print("4. Delete workout Session")
        print("5. Display all Members")
        print("6: Display all workout sessions")
        print("7. Display members with age from 25-30")
        print("8. Exit")
        choice = input("Please make a selection (1-8) ")
        
        if choice ==("1"):
            name=input("Please enter the new members name: ")
            age=input("Please enter age: ")
            add_member(name,age)
            
        elif choice ==("2"):
            member_id=input("What is the member id: ")
            date = input("Enter date as (year-month-day, 2024-10-11) ")
            if re.search(r'\d{4}-\d{2}-\d{2}', date):
                print()
            else: 
                print("invalid format please enter as ####_##_##")
                date = input("Enter date as (year-month-day, 2024-10-11) ")
                
            duration_minutes= input("How long was the workout session: (enter in minutes)")
            calories_burned=input("How many calories burned: ")
            add_workout_session(date,duration_minutes,calories_burned,member_id)
            
        elif choice ==("3"):
            id = input("What is the Members id you would like to update: ")
            age = input("What is the age of the member: ")
            update_member_age(id,age)
            
        elif choice ==("4"):
            session_id = input("What workout session id do you want to delete: ")
            #members_id =input("What member id do you want to delete")
            delete_workout_session(session_id)
        elif choice ==("5"):
           display_all_members()
        elif choice ==("6"):
            display_workoutsessions()
        elif choice ==("7"):
            start_age=(25)
            end_age=(30)
            get_members_in_age_range(start_age, end_age)
        elif choice ==("8"):
            break
        else:
            print("Please enter a numner 1-7")
main()