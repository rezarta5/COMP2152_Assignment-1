"""
Author: Rezarta Marku
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"      
preferred_weight_kg = 20.5       
highest_reps = 25                
membership_active = True        

print(gym_member, preferred_weight_kg, highest_reps, membership_active)
# Step c: Create a dictionary named workout_stats
# Dictionary storing friends' workout minutes (yoga, running, weightlifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (20, 40, 30),
    "Taylor": (25, 35, 25)
}

print("Workout stats dictionary:")
print(workout_stats)

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, activities in list(workout_stats.items()):
    total = sum(activities)
    workout_stats[f"{friend}_Total"] = total

print("Workout stats with total minutes added:")
print(workout_stats)

# Step e: Create a 2D nested list called workout_list
workout_list = [list(activities) for friend, activities in workout_stats.items() if "_Total" not in friend]
print("2D nested list of workout minutes:")
print(workout_list)

# Step f: Slice the workout_list
# Yoga and running for all friends
yoga_running = [row[:2] for row in workout_list]
print("Yoga & running for all friends:", yoga_running)

# Weightlifting for last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting for last two friends:", weightlifting_last_two)

# Step g: Check if any friend's total >= 120
for key in workout_stats:
    if "_Total" in key and workout_stats[key] >= 120:
        name = key.replace("_Total", "")
        print(f"Great job staying active, {name}!")

# Step h: User input to look up a friend
friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats:
    activities = workout_stats[friend_name]
    total = workout_stats[f"{friend_name}_Total"]
    print(f"\n{friend_name}'s workout minutes:")
    print("Yoga:", activities[0])
    print("Running:", activities[1])
    print("Weightlifting:", activities[2])
    print("Total workout minutes:", total)
else:
    print(f"Friend {friend_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {key.replace("_Total",""): value for key, value in workout_stats.items() if "_Total" in key}
highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)
print("Friend with highest total workout minutes:", highest_friend)
print("Friend with lowest total workout minutes:", lowest_friend)
