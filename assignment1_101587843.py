"""
Author: Ifrad Hossain
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5    # float
highest_reps = 25             # int
membership_active = True      # bool

# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 30, 25),
    "Taylor": (20, 50, 30)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[f"{friend}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
workout_list = [v for k, v in workout_stats.items() if not k.endswith("_Total")]

# Step f: Slice the workout_list
print("Yoga and running:", [friend[0:2] for friend in workout_list])
print("Weightlifting (last two):", [friend[2] for friend in workout_list[-2:]])

# Step g: Check if any friend's total >= 120
for name, value in workout_stats.items():
    if name.endswith("_Total"):
        if value >= 120:
            print(f"Great job staying active, {name.replace('_Total', '')}!")

# Step h: User input to look up a friend
friend_query = input("Enter a friend's name: ")
if friend_query in workout_stats and not friend_query.endswith("_Total"):
    print(f"Stats: {workout_stats[friend_query]}, Total: {workout_stats[friend_query + '_Total']}")
else:
    print(f"Friend {friend_query} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {name: value for name, value in workout_stats.items() if name.endswith("_Total")}
print(f"Highest: {max(totals, key=totals.get).replace('_Total', '')}")
print(f"Lowest: {min(totals, key=totals.get).replace('_Total', '')}")
