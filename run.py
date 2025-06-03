from config.setup import Session
from lib.models import User, Workout, Exercise

# session instance
session = Session()

# user operations in the CLI

# to list all users
def list_users():
    users = session.query(User).all()
    if not users:
        print("Oops! No users found.")
        return
    for user in users:
        print(f"ID: {user.id}, Username: {user.name}, Email: {user.email}")
       

# to add a user
def add_user():
    name = input("Username: ").strip()
    email = input("Email: ").strip()

    if session.query(User).filter_by(name = name).first():
        print("Username already exists.")
        return
    
    new_user = User(name = name, email = email)
    session.add(new_user)
    session.commit()
    print(f"User '{name}' added.")


# update a user
def update_user():
    user_id = input("Enter User ID to update: ").strip()
    user = session.query(User).filter_by(id = user_id).first()

    if not user:
        print("Oops! User not found.")
        return
    new_username = input(f"New username (leave blank to keep '{user.name}'").strip()
    new_email = input(f"New email (leave blank to keeo '{user.email}'").strip()

    if new_username:
        user.name = new_username
    if new_email:
        user.email = new_email

    session.commit()
    print(f"User ID {user_id} updated successfully.")


# delete a user
def delete_user():
    user_id = input("Enter User ID to delete: ").strip()
    user = session.query(User).filter_by(id = user_id).first()

    if not user:
        print("Oops! User not found.")
        return
    
    confirm = input(f"Are you sure you want to delete user '{user.name}?").strip()

    if confirm == 'y':
        session.delete(user)
        session.commit()
        print(f"User '{user.name}' deleted successfully.")
    else:
        print("Deletion canceled.")

# workouts
# list workouts
def list_workouts():
    workouts = session.query(Workout).all()
    if not workouts:
        print("Oops! No workouts found.")
        return
    for w in workouts:
        print(f"ID: {w.id}, Name: {w.workout_name}, Intensity: {w.intensity}")
       

# add workout
def add_workout():
    user_id = input("Enter User ID: ").strip()
    user = session.query(User).filter_by(id = user_id).first()
    if not user:
        print("Oops! User not found.")
        return
    name = input("Workout name: ").strip()
    intensity = input("Intensity (1-10): ").strip()
    notes = input("Notes (optional): ").strip()
    

    try:
        intensity_val = int(intensity)
    except:
        print("Invalid input for intensity.")
        return
    

    workout = Workout(name = name, intensity = intensity_val, notes = notes, user = user)
    session.add(workout)
    session.commit()
    print("Workout added successfully.")
    

# update workout
def update_workout():
    workout_id = input("Enter workout ID to update: ").strip()
    workout = session.query(Workout).filter_by(id = workout_id).first()
    if not workout:
        print("Oops! Workout not found.")
        return
    
    name = input(f"New name (Leave blank to keep '{workout.name}'): ").strip()
    intensity = input(f"New intensity (Leave blank to keep '{workout.intensity}'): ").strip()
    notes = input(f"New notes (Leave blank to keep the notes): ").strip()

    if name:
        workout.workout_name = name
    if intensity:
        workout.intensity = int(intensity)
    if notes:
        workout.notes = notes
    
    session.commit()
    print("Workout updated successfully.")


# delete workout
def del_workout():
    workout_id = input("Enter Workout ID to delete: ").strip()
    workout = session.query(Workout).filter_by(id = workout_id).first()
    if not workout:
        print("Oops! Workout not found.")
        return
    confirm = input(f"Delete workout '{workout.workout_name}'? (y/n): ").strip().lower()
    if confirm == 'y':
        session.delete(workout)
        session.commit()
        print("Workout added Successfully.")
       

# exercises
# list all exercises
def list_exercise():
    exercises = session.query(Exercise).all()
    if not exercises:
        print("Oops! No exercises found.")
        return
    for e in exercises:
        print(f"ID: {e.id}, Name: {e.name}, Type: {e.type}, Reps: {e.reps}, Sets: {e.sets},  Workout ID: {e.workout_id}")
       
def add_exercises():
    workout_id = input("Enter Workout ID: ").strip()
    workout = session.query(Workout).filter_by(id = workout_id).first()
    if not workout:
        print("Oops! Workout not found.")
        return
    name = input("Exercise name: ").strip()
    type = input("Exercise type(Cardio,Strength,Flexibility,etc.): ").strip()
    reps = input("Reps (or 0): ").strip()
    sets = input("Sets (or 0): ").strip()


    try:
        reps = int(reps)
        sets = int(sets)
    except:
        print("Invalid input for reps/sets.")
        return
    
    exercise = Exercise(name = name, type = type, reps = reps, workout = workout)
    session.add(exercise)
    session.commit()
    print("Exercise added Successfully.")
    

# update exercises
def update_exercise():
    ex_id = input("Enter Exercise ID to update: ").strip()
    ex = session.query(Exercise).filter_by(id = ex_id).first()
    if not ex:
        print("Oops! Exercise not found.")
        return
    name = input(f"New name (Leave blank to keep '{ex.name}'): ").strip()
    type_ = input(f"New type (Leave blank to keep '{ex.type}'): ").strip()
    reps = input(f"New reps (Leave blank to keep '{ex.reps}'): ").strip()
    sets = input(f"News sets (Leave blank to keep '{ex.sets}'): ").strip()


    if name:
        ex.name = name
    if type_:
        ex.type =type_
    if reps:
        ex.reps = int(reps)
    if sets:
        ex.sets = int(sets)

    session.commit()
    print("Exercise updated successfully.")

# del exercise
def del_exercise():
    ex_id = input("Enter Exercise ID to delete: ").strip()
    ex = session.query(Exercise).filter_by(id=ex_id).first()

    if not ex:
        print("Oops! Exercise not found.")
        print("************************")
        return
    
    confirm = input(f"Delete exercise '{ex.name}'? (y/n): ").strip().lower()

    if confirm =='y':
        session.delete(ex)
        session.commit()
        print("Exercise deleted Successfully.")


# exercises menu
def exercises_menu():
    while True:
        print("Exercises Menu:")
        print("1. List all exercises")
        print("2. Add exercise")
        print("3. Update exercise")
        print("4. Delete exercise")
        print("Back to main menu")


        choice = input("Choose an option: ").strip()
        if choice == '1':
            list_exercise()
        elif choice == '2':
            add_exercises()
        elif choice == '3':
            update_exercise()
        elif choice == '4':
            del_exercise()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# workouts menu
def workouts_menu():
    while True:
        print("Workouts Menu:")
        print("1. List all workouts")
        print("2. Add workout")
        print("3. Update workout")
        print("4. Delete workout")
        print("5. Back to main menu")


        choice =  input("Choose an option: ").strip()
        if choice == '1':
            list_workouts()
        elif choice == '2':
            add_workout()
        elif choice == '3':
            update_workout()
        elif choice == '4':
            del_workout()
        elif choice == '5':
            break
        else:
            print("Invalid choice.Try again...")
        

# users menu
def users_menu():
    while True:
        print("Users Menu:")
        print("1. List all users")
        print("2. Add user")
        print("3. Update user")
        print("4. Delete a user")
        print("5. Return to main menu")
        

        choice = input("Choose an option: ").strip()
        if choice == '1':
            list_users()
        elif choice == '2':
            add_user()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")


# main menu
def main_menu():
    while True:
        print("MAIN MENU:")
        print("1. USERS")
        print("2. WORKOUTS")
        print("3. EXERCISES")
        print("4. EXIT")

           

        choice = input("Choose an option: ").strip()
        if choice == '1':
            users_menu()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            print("Thank you for visiting.")
            break
        else:
            print("Invalid choice try again.")


if __name__ == '__main__':
    main_menu()


    

    
