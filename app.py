import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")
print(data)

# print(data.head())
# print(len(data))
# print(data.columns)

# print(data['Python'].mean())
# print(data['Python'].min())
# print(data['Python'].max())

# low_attendance = data[data["Attendance"]<75]
# print(low_attendance)


# HIGHEST PYTHON SCORER
top_python = data.loc[data["Python"].idxmax()]
print(top_python)

# CALCULATE AVERAGE MARKS
data["Average"]=data[["Python","ML","OS"]].mean(axis=1)
print(data[["Name","Average"]])

# STUDENTS WITH AVERAGE 80 OR ABOVE
high_performers = data[data["Average"]>=80]
print(high_performers[["Name","Average"]])


subjects = ["Python", "ML", "OS"]   #chart 1: subject averages

averages = [
    data["Python"].mean(),
    data["ML"].mean(),
    data["OS"].mean()
]
plt.bar(subjects,averages)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()

#chart 2: scatter plot
plt.scatter(data["Study_Hours"],data["Average"])

plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.show()


#chart 3:
plt.scatter(data["Attendance"],data["Average"])

plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance(%)")
plt.ylabel("Average Marks")
plt.show()







