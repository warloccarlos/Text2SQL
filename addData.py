import sqlite3

connection = sqlite3.connect('DisposableEmail.db')
cursor = connection.cursor()

my_file = open("DisposableEmail.txt", "r")
# reading the file
data = my_file.readlines()
  
dataList = data
# printing the data
#print(dataList[2])

for dl in dataList:
    dl = dl.split('\n')
    print(dl[0])        #This is optional for visual confirmation
    cursor.execute('insert into disposableEmail(emailDomain) values(?)', [(dl[0])])
    connection.commit()
    
connection.close()
my_file.close()
