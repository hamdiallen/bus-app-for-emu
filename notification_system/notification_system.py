from datetime import datetime, timedelta

user_patterns = {
    "student_1": {"route": "101A", "usual_time": "08:10"},
    "student_2": {"route": "102B", "usual_time": "08:20"},
}

def should_notify(user_id, current_time):
    user = user_patterns.get(user_id)
    if not user:
        return False

    usual_time = datetime.strptime(user["usual_time"], "%H:%M").time()
    current_time = datetime.strptime(current_time, "%H:%M").time()
    notify_time = (datetime.combine(datetime.today(), usual_time) - timedelta(minutes=2)).time()

    return current_time >= notify_time and current_time <= (datetime.combine(datetime.today(), usual_time) + timedelta(minutes=2)).time()

current_time = "08:08"
for user_id in user_patterns:
    if should_notify(user_id, current_time):
        print(f"Notification sent to {user_id}")
