import shutil
import mysql.connector as rajjo
import getpass
def reset_data(cur):
    try:
        shutil.rmtree("Data")
    except:
        pass
    try:
        s="DROP DATABASE class_management"
        cur.execute(s)
    except:
        pass
print("You are about to reset all the data of this project!")
u=input("Username : ")
p=getpass.getpass("Password : ")
try:
    mydb=rajjo.connect(host="localhost",user=u,password=p)
    cur1=mydb.cursor()
    reset_data(cur1)
except:
    pass

