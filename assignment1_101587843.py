"""
Author: Ifrad Hossain
Assignment: #1
"""

# Step b: Create 4 variables with data types commented to the right
gym_member = "Alex Alliton" # str
preferred_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # bool

# Step c: Create a dictionary named workout_stats
# Dictionary data type: keys are strings (names), values are tuples of integers (minutes for yoga, running, weightlifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 30, 25),
    "Taylor": (20, 50, 30)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
# We convert keys to a list first to avoid modifying the dictionary during iteration
for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
# Data type: List of tuples (each inner tuple contains integers for the 3 activities)
workout_list = [value for key, value in workout_stats.items() if not key.endswith("_Total")]

# Step f: Slice the workout_list
# 1. Extract and print minutes for yoga and running for all friends (index 0 and 1)
yoga_running_all = [row[0:2] for row in workout_list]
print("Yoga and running minutes for all friends:", yoga_running_all)

# 2. Extract and print minutes for weightlifting for the last two friends (index 2)
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for the last two friends:", weightlifting_last_two)

# Step g: Check if any friend's total >= 120
for name, value in workout_stats.items():
    if name.endswith("_Total"):
        friend_name = name.replace("_Total", "")
        if value >= 120:
            print(f"Great job staying active, {friend_name}!")

# Step h: User input to look up a friend's workout stats
friend_query = input("\nEnter a friend's name: ")

if friend_query in workout_stats and not friend_query.endswith("_Total"):
    activities = workout_stats[friend_query]
    total = workout_stats[f"{friend_query}_Total"]
    print(f"{friend_query}'s workout minutes: {activities}")
    print(f"{friend_query}'s total workout minutes: {total}")
else:
    print(f"Friend {friend_query} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {name: value for name, value in workout_stats.items() if name.endswith("_Total")}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"\nFriend with highest total minutes: {highest_friend.replace('_Total', '')} ({totals[highest_friend]} minutes)")
print(f"Friend with lowest total minutes: {lowest_friend.replace('_Total', '')} ({totals[lowest_friend]} minutes)")
