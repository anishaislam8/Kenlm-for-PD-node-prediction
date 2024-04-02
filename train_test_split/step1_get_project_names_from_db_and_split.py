import sqlite3

connection = sqlite3.connect("/media/crouton/aislam4/database.db")
cursor = connection.cursor()

cursor.execute("SELECT Project_Name from Projects;")
data = cursor.fetchall()
data = [x[0] for x in data]
print(len(data))

file_name = open('Projects.txt','a')
for item in data:
    file_name.write(item+"\n")

from sklearn.model_selection import train_test_split

with open("Projects.txt", 'r') as file:
    data = file.readlines()

# Split the data into train and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

file_name = open('train_projects.txt','a')
for item in train_data:
    item = item.strip()
    file_name.write(item+"\n")


file_name = open('test_projects.txt','a')
for item in test_data:
    item = item.strip()
    file_name.write(item+"\n")
