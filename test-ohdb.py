from onehabit import OneHabitDatabase
from onehabit.data.dataclasses.goals import Goal, GoalMetadata, GoalSet
from onehabit.data.dataclasses.users import User

if __name__ == "__main__":
    ohdb = OneHabitDatabase()
    user = User.from_existing("matthew")
    gs = GoalSet(user_id=user.id)
    pass