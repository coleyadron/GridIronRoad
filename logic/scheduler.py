import json

def scheduler():
    try:
        with open("json/schedule.json", "r") as file:
            schedule = json.load(file)
            return schedule
    except FileNotFoundError:
        print("Error finding schedule file")
        return None
    except json.JSONDecodeError:
        print("Error decoding schedule file")
        return None
    except Exception as e:
        print("Error reading schedule file: ", e)
        return None
    
    