from config.setup import Session
from lib.models import User, Workout, Exercise

# session instance
session = Session()

def printMessage(message):
    print(
        f"-----------------------------------------------\n{message}\n------------------------------------------------"
    )


# user operations in the CLI

# to list all users
def list_users():
    users = session.query(User).all()
    if not users:
        print("Oops! No users found.")
        return
    for user in users:
        printMessage(f"ID: {user.id}, Username: {user.name}, Email: {user.email}")
       

# to add a user
def add_user():
    name = input("Username: ").strip()
    email = input("Email: ").strip()

    if session.query(User).filter_by(name = name).first():
        printMessage("Username already exists.")
        return
    
    new_user = User(name = name, email = email)
    session.add(new_user)
    session.commit()
    printMessage(f"User '{name}' added.")


# update a user
def update_user():
    user_id = input("Enter User ID to update: ").strip()
    user = session.query(User).filter_by(id = user_id).first()

    if not user:
        printMessage("Oops! User not found.")
        return
    new_username = input(f"New username (leave blank to keep '{user.name}'").strip()
    new_email = input(f"New email (leave blank to keeo '{user.email}'").strip()

    if new_username:
        user.name = new_username
    if new_email:
        user.email = new_email

    session.commit()
    printMessage(f"User ID {user_id} updated successfully.")


# delete a user
def delete_user():
    user_id = input("Enter User ID to delete: ").strip()
    user = session.query(User).filter_by(id = user_id).first()

    if not user:
        printMessage("Oops! User not found.")
        return
    
    confirm = input(f"Are you sure you want to delete user '{user.name}?").strip()

    if confirm == 'y':
        session.delete(user)
        session.commit()
        printMessage(f"User '{user.name}' deleted successfully.")
    else:
        printMessage("Deletion canceled.")

# workouts
# list workouts
def list_workouts():
    workouts = session.query(Workout).all()
    if not workouts:
        printMessage("Oops! No workouts found.")
        return
    for w in workouts:
        printMessage(f"ID: {w.id}, Name: {w.workout_name}, Intensity: {w.intensity}")
       

# add workout
def add_workout():
    user_id = input("Enter User ID: ").strip()
    user = session.query(User).filter_by(id = user_id).first()
    if not user:
        printMessage("Oops! User not found.")
        return
    name = input("Workout name: ").strip()
    intensity = input("Intensity (1-10): ").strip()
    notes = input("Notes (optional): ").strip()
    

    try:
        intensity_val = int(intensity)
    except:
        printMessage("Invalid input for intensity.")
        return
    

    workout = Workout(workout_name = name, intensity = intensity_val, notes = notes, user = user)
    session.add(workout)
    session.commit()
    printMessage("Workout added successfully.")
    

# update workout
def update_workout():
    workout_id = input("Enter workout ID to update: ").strip()
    workout = session.query(Workout).filter_by(id = workout_id).first()
    if not workout:
        printMessage("Oops! Workout not found.")
        return
    
    name = input(f"New name (Leave blank to keep '{workout.workout_name}'): ").strip()
    intensity = input(f"New intensity (Leave blank to keep '{workout.intensity}'): ").strip()
    notes = input(f"New notes (Leave blank to keep the notes): ").strip()

    if name:
        workout.workout_name = name
    if intensity:
        workout.intensity = int(intensity)
    if notes:
        workout.notes = notes
    
    session.commit()
    printMessage("Workout updated successfully.")


# delete workout
def del_workout():
    workout_id = input("Enter Workout ID to delete: ").strip()
    workout = session.query(Workout).filter_by(id = workout_id).first()
    if not workout:
        printMessage("Oops! Workout not found.")
        return
    confirm = input(f"Delete workout '{workout.workout_name}'? (y/n): ").strip().lower()
    if confirm == 'y':
        session.delete(workout)
        session.commit()
        printMessage("Workout deleted Successfully.")
       

# exercises
# list all exercises
def list_exercise():
    exercises = session.query(Exercise).all()
    if not exercises:
        printMessage("Oops! No exercises found.")
        return
    for e in exercises:
        printMessage(f"ID: {e.id}, Name: {e.name}, Type: {e.type}, Reps: {e.reps}, Sets: {e.sets},  Workout ID: {e.workout_id}")
       
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
        printMessage("Invalid input for reps/sets.")
        return
    
    exercise = Exercise(name = name, type = type, reps = reps, workout = workout)
    session.add(exercise)
    session.commit()
    printMessage("Exercise added Successfully.")
    

# update exercises
def update_exercise():
    ex_id = input("Enter Exercise ID to update: ").strip()
    ex = session.query(Exercise).filter_by(id = ex_id).first()
    if not ex:
        printMessage("Oops! Exercise not found.")
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
    printMessage("Exercise updated successfully.")

# del exercise
def del_exercise():
    ex_id = input("Enter Exercise ID to delete: ").strip()
    ex = session.query(Exercise).filter_by(id=ex_id).first()

    if not ex:
        printMessage("Oops! Exercise not found.")
        return
    
    confirm = input(f"Delete exercise '{ex.name}'? (y/n): ").strip().lower()

    if confirm =='y':
        session.delete(ex)
        session.commit()
        printMessage("Exercise deleted Successfully.")


# view workouts
def view_workouts_for_user():
    users = session.query(User).all()
    if not users:
        printMessage("No users found.")
        return
    
    for user in users:
        print(f"{user.id}. {user.name}")

    try:
        user_id = int(input("Enter the user ID to view their workouts: "))
        user = session.query(User).get(user_id)
        if not user:
            printMessage("User not found.")
            return

        workouts = user.workouts
        if workouts:
            printMessage(f"\nWorkouts for {user.name}:")
            for workout in workouts:
                printMessage(f"  ID: {workout.id} | Name: {workout.workout_name} | Intensity: {workout.intensity}")
        else:
            printMessage("This user has no workouts yet.")
    except ValueError:
        printMessage("Invalid input. Please enter a number.")


def view_exercises_by_type():
    printMessage("\nView Exercises by Type")
    exercise_type = input("Enter exercise type (e.g., cardio, strength): ").lower()
    
    exercises = session.query(Exercise).filter(
        Exercise.type.ilike(f"%{type}%")
    ).all()

    if exercises:
        print(f"\nExercises of type '{exercise_type}':")
        for ex in exercises:
            printMessage(
                f"  - {ex.name} | Type: {ex.type} | Reps: {ex.reps} | Sets: {ex.sets} | Workout ID: {ex.workout_id}"
            )
    else:
        printMessage("No exercises found for that type.")




# exercises menu
def exercises_menu():
    while True:
        print("Exercises Menu:")
        print("1. List all exercises")
        print("2. Add exercise")
        print("3. Update exercise")
        print("4. Delete exercise")
        print("5. Back to main menu")


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
            printMessage("Invalid choice. Try again.")

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
            printMessage("Invalid choice.Try again...")
        

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
            printMessage("Invalid choice, try again.")


# main menu
def main_menu():
    print("WELCOME TO PROGRESS FITNESS LOGGER\nLOG YOUR FITNESS JOURNEY HERE WITH US...\n--------------------------------------------------------------------------------------------------")
    while True:
        print("MAIN MENU:")
        print("1. USERS")
        print("2. WORKOUTS")
        print("3. EXERCISES")
        print("4. View all workouts for a user")
        print("5. View exercises by type")
        print("6. EXIT")
        print("---------------------------------------------------------------------------------------------")
           

        choice = input("Choose an option: ").strip()
        if choice == '1':
            users_menu()
        elif choice == '2':
            workouts_menu()
        elif choice == '3':
            exercises_menu()
        elif choice == "4":
            view_workouts_for_user()
        elif choice == "5":
            view_exercises_by_type()

        elif choice == '6':
            printMessage("Thank you for visiting Progress Fitness Logger.")
            break
        else:
            printMessage("Invalid choice try again.")


if __name__ == '__main__':
    main_menu()


    

    
