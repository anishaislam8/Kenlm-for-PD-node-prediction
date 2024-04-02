import sqlite3

connection = sqlite3.connect("/media/crouton/aislam4/database.db")
cursor = connection.cursor()

def get_hashes_of_a_project(project_name):
    cursor.execute("SELECT Distinct Hash FROM Revisions WHERE Project_Name = (?)", (project_name,))
    data = cursor.fetchall()
    data = set([x[0] for x in data])
    #print(len(data)
    return data


train_hashes = set()
test_hashes = set()

with open("train_projects.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        hashes = get_hashes_of_a_project(line)
        train_hashes.update(hashes)

with open("test_projects.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        hashes = get_hashes_of_a_project(line)
        test_hashes.update(hashes)

file_name = open('train_hashes.txt','a')
for item in train_hashes:
    file_name.write(item+"\n")

file_name = open('test_hashes.txt','a')
for item in test_hashes:
    file_name.write(item+"\n")