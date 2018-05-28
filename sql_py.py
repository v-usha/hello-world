import pyodbc
import os
import zipfile

conn = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = '10.1.3.121\sql2017', database = 'jrlmain')
cursor = conn.cursor()

#cursor.execute("SELECT COUNT(*) as count FROM oe_hdr")
#row = cursor.fetchone()
#print(row)

'''
source_path = "//p21vault/Application_updates/18.1/18.1/18.1.3176/zip/SQL_18.1.3176.zip"

newpath = r'C:\sqlscript\18.1.3176' 
if not os.path.exists(newpath):
    os.makedirs(newpath)


zip_ref = zipfile.ZipFile(source_path, 'r')
zip_ref.extractall(newpath)
zip_ref.close()


newpath = r'C:\sqlscript\test' 
for filename in os.walk(newpath):
	for statement in file(filename).read().split(';'):
		cursor.execute(statement) 
'''

inputdir = r'C:\sqlscript\test' 
for script in os.listdir(inputdir):
    with open(inputdir+'\\' + script,'r') as inserts:
        sqlScript = inserts.read()
	#print(sqlScript)
        for statement in sqlScript.split(';'):
		#print(statement)
		cursor.execute(statement)
    print(script)


conn.commit()
#print(row)
conn.close()








