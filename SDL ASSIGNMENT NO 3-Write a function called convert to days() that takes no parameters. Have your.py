def get_days(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    days = total_seconds / 86400  # 86400 seconds in a day
    return days

def convert_to_days():
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))
    
    days = get_days(hours, minutes, seconds)
    rounded_days = round(days, 4)
    
    print(f"The total number of days is approximately {rounded_days} days.")

# Call the function to test
convert_to_days()