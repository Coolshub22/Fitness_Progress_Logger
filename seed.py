from lib.models import User, Workout, Exercise
from config.setup import Session


# session instance
session = Session()

# remove any previous data
session.query(Exercise).delete()
session.query(Workout).delete()
session.query(User).delete()

# add users
user1 = User(name="David Burale", email="dburale@gmail.com")
user2 = User(name="Jane Atoti", email="janeatoti@gmail.com")
user3 = User(name="Michael Davids", email="micdavids@gmail.com")
user4 = User(name="Sarah Lee", email="sara@gmail.com.com")
user5 = User(name="Harper Travis", email="htravis@gmail.com")


# add workouts
w1 = Workout(workout_name="Push Day",intensity=8, notes="Great chest session")
w2 = Workout(workout_name="Leg Day",intensity=9, notes="Tiring but worth it")
w3 = Workout(workout_name="Cardio Blast",intensity=6, notes="Morning energy boost")
w4 = Workout(workout_name="Pull Day", intensity=7, notes="Need to improve form")
w5 = Workout(workout_name="Full Body HIIT", intensity=9, notes="Very sweaty")
w6 = Workout(workout_name="Upper Body Burn", intensity=8, notes="Felt the pump")
w7 = Workout(workout_name="Morning Run", intensity=5, notes="Light jog")
w8 = Workout(workout_name="Strength Circuit", intensity=8, notes="Circuit training")
w9 = Workout(workout_name="Core Focus", intensity=7, notes="Abs on fire")
w10 = Workout(workout_name="Evening Yoga", intensity=4, notes="Very relaxing")


# add exercises
# Push Day
e1 = Exercise(name="Bench Press", sets=4, reps=10, weight=70.0, type="Strength")
e2 = Exercise(name="Overhead Press", sets=3, reps=8, weight=45.0, type="Strength")

    # Leg Day
e3 =  Exercise(name="Squats", sets=4, reps=8, weight=100.0, type="Strength")
e4 =  Exercise(name="Leg Press", sets=3, reps=10, weight=180.0, type="Strength")

    # Cardio Blast
e5 =  Exercise(name="Treadmill", duration=30, type="Cardio")
e6 =  Exercise(name="Rowing Machine", duration=15, type="Cardio")

    # Pull Day
e7 =  Exercise(name="Deadlifts", sets=4, reps=6, weight=120.0, type="Strength")
e8 =  Exercise(name="Barbell Rows", sets=3, reps=10, weight=60.0, type="Strength")

    # Full Body HIIT
e9 =  Exercise(name="Burpees", sets=3, reps=15, type="HIIT")
e10 = Exercise(name="Mountain Climbers", sets=3, reps=20, type="HIIT")

    # Upper Body Burn
e11 = Exercise(name="Push Ups", sets=4, reps=20, type="Bodyweight")
e12 = Exercise(name="Tricep Dips", sets=3, reps=15, type="Bodyweight")

    # Morning Run
e13 = Exercise(name="Jogging", duration=25, type="Cardio")
e14 = Exercise(name="Stretching", duration=10, type="Flexibility")

    # Strength Circuit
e15 = Exercise(name="Kettlebell Swings", sets=3, reps=15, weight=20.0, type="Circuit")
e16 = Exercise(name="Jump Squats", sets=3, reps=20, type="HIIT")

    # Core Focus
e17 = Exercise(name="Plank", sets=3, reps=1, duration=60, type="Core")
e18 = Exercise(name="Bicycle Crunches", sets=3, reps=25, type="Core")
    # Evening Yoga
e19 = Exercise(name="Downward Dog", sets=2, reps=5, duration=5, type="Flexibility")
e20 = Exercise(name="Sun Salutation", sets=3, reps=4, duration=8, type="Flexibility")

# Associate Users with workouts
w1.user = user1
w2.user = user2
w3.user = user3
w4.user = user4
w5.user = user5
w6.user = user1
w7.user = user2
w8.user = user3
w9.user = user4
w10.user = user5


# Associate exercises with workouts
e1.workout = w1
e2.workout = w1

e3.workout = w2
e4.workout = w2

e5.workout = w3
e6.workout = w3

e7.workout = w4
e8.workout = w4

e9.workout = w5
e10.workout = w5

e11.workout = w6
e12.workout = w6

e13.workout = w7
e14.workout = w7

e15.workout = w8
e16.workout = w8

e17.workout = w9
e18.workout = w9

e19.workout = w10
e20.workout = w10



session.add_all([user1, user2, user3, user4, user5, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20])
session.commit()

print("✅ Seeded database available!")