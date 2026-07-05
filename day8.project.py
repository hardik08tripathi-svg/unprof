import requests
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

API_URL = "https://jsonplaceholder.typicode.com/posts"

# ----------------------------
# Fetch Data
# ----------------------------
try:
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    print("Data fetched successfully!")

except requests.exceptions.RequestException as e:
    print("API Error:", e)
    exit()

# ----------------------------
# Convert to DataFrame
# ----------------------------
df = pd.DataFrame(data)

# ----------------------------
# Clean Data
# ----------------------------
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Create title length column
df["Title Length"] = df["title"].apply(len)

# ----------------------------
# Analysis
# ----------------------------
posts_per_user = df.groupby("userId").size()

average_title = df["Title Length"].mean()

print("\n========== SUMMARY ==========")
print("Total Posts:", len(df))
print("Unique Users:", df["userId"].nunique())
print("Average Title Length:", round(average_title, 2))

# ----------------------------
# Save Processed Data
# ----------------------------
df.to_csv("processed_posts.csv", index=False)
df.to_json("processed_posts.json", orient="records", indent=4)

print("\nProcessed data saved.")

# ----------------------------
# Bar Chart
# ----------------------------
plt.figure(figsize=(8,5))
posts_per_user.plot(kind="bar")

plt.title("Posts Per User")
plt.xlabel("User ID")
plt.ylabel("Number of Posts")

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# ----------------------------
# Line Chart
# ----------------------------
plt.figure(figsize=(8,5))

plt.plot(posts_per_user.index,
         posts_per_user.values,
         marker="o")

plt.title("Posts Trend by User")
plt.xlabel("User ID")
plt.ylabel("Posts")

plt.grid(True)

plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# ----------------------------
# Pie Chart
# ----------------------------
plt.figure(figsize=(7,7))

posts_per_user.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Posts Distribution")

plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

# ----------------------------
# Generate PDF Report
# ----------------------------
styles = getSampleStyleSheet()

pdf = SimpleDocTemplate("Data_Analysis_Report.pdf")

content = []

content.append(Paragraph("<b>Data Analysis Report</b>", styles["Title"]))
content.append(Paragraph("<br/>", styles["Normal"]))

content.append(Paragraph(f"Total Posts: {len(df)}", styles["BodyText"]))
content.append(Paragraph(f"Unique Users: {df['userId'].nunique()}", styles["BodyText"]))
content.append(Paragraph(f"Average Title Length: {round(average_title,2)}", styles["BodyText"]))

content.append(Paragraph("<br/>Charts Generated:", styles["Heading2"]))
content.append(Paragraph("- Bar Chart", styles["BodyText"]))
content.append(Paragraph("- Line Chart", styles["BodyText"]))
content.append(Paragraph("- Pie Chart", styles["BodyText"]))

pdf.build(content)

print("\nPDF Report Generated Successfully!")
print("CSV Saved: processed_posts.csv")
print("JSON Saved: processed_posts.json")
print("PDF Saved: Data_Analysis_Report.pdf")
