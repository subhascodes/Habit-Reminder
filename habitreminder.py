import schedule
import time
# Collect habits
habits = {}
habit = input("Enter a habit (or 'done' to finish): ")
while habit != "done":
    rtime = input(f"When should I remind you about '{habit}'? (e.g., 08:00): ")
    habits[habit] = rtime
    habit = input("Enter another habit (or 'done' to finish): ")

# Reminder function
def remind(habit):
    print(f"Reminder: {habit}")
    completed = input("Did you complete this habit? (y/n): ").lower()
    with open("habit_log.txt", "a") as log:
        log.write(f"{time.ctime()}: {habit} - {'Completed' if completed == 'y' else 'Missed'}\n")

# Schedule reminders
for habit, reminder_time in habits.items():
    schedule.every().day.at(reminder_time).do(remind, habit=habit)

# Run the scheduler
print("Starting habit reminders... (Press Ctrl+C to stop)")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped habit reminders.")