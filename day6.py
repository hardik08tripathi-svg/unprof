import pandas as pd

# Read CSV file
try:
    df = pd.read_csv("student_marks.csv")
    print("CSV file loaded successfully.\n")

except FileNotFoundError:
    print("Error: student_marks.csv not found!")
    exit()

except Exception as e:
    print("Error:", e)
    exit()

# Display Original Data
print("Original Data:")
print(df)

# Convert subject columns to numeric
subjects = ["Math", "Science", "English", "Computer"]

for subject in subjects:
    df[subject] = pd.to_numeric(df[subject], errors="coerce")

# Replace missing/invalid values with subject average
for subject in subjects:
    average = df[subject].mean()
    df[subject].fillna(average, inplace=True)

print("\nCleaned Data:")
print(df)

# Calculate subject-wise average
print("\nSubject-wise Average Marks")

subject_average = {}

for subject in subjects:
    avg = round(df[subject].mean(), 2)
    subject_average[subject] = avg
    print(f"{subject}: {avg}")

# Student Total and Percentage
df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = round(df["Total"] / len(subjects), 2)

print("\nStudent Report")
print(df[["Name", "Total", "Percentage"]])

# Generate Summary Report
print("\n========== SUMMARY REPORT ==========")
print("Total Students:", len(df))

highest = df.loc[df["Percentage"].idxmax()]
lowest = df.loc[df["Percentage"].idxmin()]

print("Highest Scorer :", highest["Name"], "-", highest["Percentage"])
print("Lowest Scorer  :", lowest["Name"], "-", lowest["Percentage"])

print("\nSubject Averages")
for subject, avg in subject_average.items():
    print(subject, ":", avg)

print("====================================")S
