import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Read Sales Data from CSV File
# ----------------------------

months = []
sales = []

try:
    with open("sales_data.csv", "r") as file:
        next(file)  # Skip header

        for line in file:
            month, amount = line.strip().split(",")
            months.append(month)
            sales.append(float(amount))

except FileNotFoundError:
    print("Error: sales_data.csv not found!")
    exit()

except Exception as e:
    print("Error:", e)
    exit()

# Convert sales list into NumPy array
sales = np.array(sales)

# ----------------------------
# Sales Analysis
# ----------------------------

print("========== SALES ANALYSIS ==========")

print("Total Sales      :", np.sum(sales))
print("Average Sales    :", np.mean(sales))
print("Highest Sales    :", np.max(sales))
print("Lowest Sales     :", np.min(sales))
print("Standard Deviation:", round(np.std(sales), 2))

highest_month = months[np.argmax(sales)]
lowest_month = months[np.argmin(sales)]

print("Best Month       :", highest_month)
print("Lowest Month     :", lowest_month)

# ----------------------------
# Dashboard
# ----------------------------

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(months, sales)
plt.title("Monthly Sales (Bar Chart)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(axis='y')
plt.show()

# Line Chart
plt.figure(figsize=(8,5))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
plt.pie(
    sales,
    labels=months,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales Distribution")
plt.show()
