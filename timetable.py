import pandas as pd
import random

# Define employees with WFH preferences, working days, and competencies
employees = [
    {"Name": "Alice", "WFH": "Flexible", "WorkingDays": ["Monday", "Wednesday", "Friday"], "Competency": ["Planning"]},
    {"Name": "Bob", "WFH": ["Monday", "Tuesday"], "WorkingDays": ["Monday", "Tuesday"], "Competency": ["Checking"]},
    {"Name": "Maz", "WFH": ["Wednesday", "Thursday"], "WorkingDays": ["Wednesday", "Thursday", "Friday"], "Competency": ["Planning", "Checking"]},
    # Add more employees here with WFH preferences, working days, and competencies
]

# Define workdays
workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Initialize a dictionary to store the final data
rota_data = {day: [] for day in ["Name", "Competency", "WorkingDays"] + workdays}

# Loop through each employee and assign WFH/Office for each workday based on preferences and working days
for employee in employees:
    rota_data["Name"].append(employee["Name"])
    rota_data["Competency"].append(", ".join(employee["Competency"]))  # Add their competencies
    rota_data["WorkingDays"].append(", ".join(employee["WorkingDays"]))  # Add their working days

    # Determine WFH days for flexible employees (e.g., Alice)
    if employee["WFH"] == "Flexible":
        # Choose two random WFH days from the employee's working days
        WFH_days = random.sample(employee["WorkingDays"], 2)
    else:
        WFH_days = employee["WFH"]

    # Assign WFH or Office for each workday
    for day in workdays:
        if day not in employee["WorkingDays"]:
            rota_data[day].append("Not Working")
        elif day in WFH_days:
            rota_data[day].append("WFH")
        else:
            rota_data[day].append("Office")

# Convert the rota data to a DataFrame
df = pd.DataFrame(rota_data)

# Save the rota to a CSV file
df.to_csv("work_from_home_rota_with_flexible.csv", index=False)

print("Work-from-home rota with flexible WFH saved as 'work_from_home_rota_with_flexible.csv'")
