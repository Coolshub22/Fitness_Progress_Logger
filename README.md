# 🏋️‍♂️ Fitness Progress Logger

> A CLI-based Python application for tracking user workouts, exercises, and progress over time — built with SQLAlchemy ORM and SQLite.

## 📌 Overview

**Fitness Progress Logger** is a terminal-based fitness tracking system that allows users to log their workouts and exercises, record performance details like reps, sets, intensity, and track their fitness journey through a clean and simple interface. It’s designed for individual users and can be easily extended or customized for broader use.

---

## 🎯 Features

- 👤 **User Management**  
  Create and manage fitness profiles for multiple users.

- 📝 **Workout Logging**  
  Record detailed workouts with name, intensity, and notes.

- 🏋️ **Exercise Tracking**  
  Add exercises to workouts with type (e.g., cardio, strength), reps, and sets.

- 📊 **CRUD Functionality**  
  Full Create, Read, Update, and Delete operations for users, workouts, and exercises.

- 📆 **Datetime Support**  
  Workouts include precise timestamps for accurate tracking.

- ⚙️ **Clean CLI Navigation**  
  Easy-to-use menus and prompts for each action in the app.

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **SQLAlchemy** – ORM for database modeling
- **SQLite** – Lightweight embedded database
- **Alembic** – Database migrations
- **Pipenv** – Dependency and environment management

---


---

## 🧑‍💻 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/coolshub22/fitness-progress-logger.git

cd fitness-progress-logger
```

### 2. Install dependencies with Pipenv

```
pipenv install
```

### 3. Run migrations using Alembic

```
pipenv shell
alembic upgrade head
```

### 4. Seed the database with sample data (optional)

```
python seed.py
```

### 5. Start the CLI app

```
python cli.py
```

## 🧪 Example Usage

```Main Menu:
1. Users
2. Workouts
3. Exercises
4. Exit

Choose an option: 2
```

## 📈 Scalability & Code Design
The app is modular and follows clean code principles. You can easily:

- Add new features (e.g., body measurements, goals)

- Extend models and relationships

- Refactor the CLI into a GUI or web interface

## 🤝 Contributing
Contributions are welcome!
Feel free to fork the repo, submit pull requests, or open issues.

# 👤 Author
[Arnold Kulavi] 

GitHub: https://github.com/Coolshub22

## 📝 License
This project is licensed under the MIT License.










