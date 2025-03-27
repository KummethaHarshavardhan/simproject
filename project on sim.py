
import mysql.connector
import smtplib
import random
import requests
url=" http://demo1867978.mockable.io/sim_data"
response=requests.get(url)
print(response.status_code)
if response.status_code==200:
    get_data=response.json()
    print(get_data)
else:
    print("not avialable data")    

mydb=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='harsha6281240878',
    database='project sim'
)
print(mydb)

mycursor=mydb.cursor()   #pipe line of mysql to python
def login():
    sim_name=input("enter your sim name: ")
    sim_mail=input("enter sim mail: ")

    sql="select* from sim_data where sim_name=%s and  sim_mail=%s "
    val=(sim_name,sim_mail)
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    if result:
        print(f"hi sir! the {sim_name} sim is avilabe")
        var=input("do you want this sim : ")
        if var=="yes":
            full_name=input("enter your full name : ")
            package=int(input("enter you want package validity: "))
            adhar_id=int(input("enter adhar number: "))
            x=input("enter you emil_id : ")
            number = random.randint(1000000000, 9999999999)
            sender_email="harshavardhan6281240878@gmail.com"
            receiver_email=x
            password="okpf axmv octs zvrh"

            subject = "10-digit Number"
            body = f"The 10-digit number is: {number}"

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{body}")
            server.quit()
            
            print("Email sent successfully!")
        else:
            print("thank you sir!")  
 
    else:
        print("sorry! this sim not avialable ")
          
login() 


''' output:-

200
{'simname1': 'airtel', 'simname2': 'jio', 'simname3': 'bsnl', 'simname4': 'vi'}
<mysql.connector.connection_cext.CMySQLConnection object at 0x000002904775A640>
enter your sim name: airtel
enter sim mail: airtel@gmail.com
hi sir! the airtel sim is avilabe
do you want this sim : yes
enter your full name : harsha
enter you want package validity: 299
enter adhar number: 567849
enter you emil_id : harshavardhankummeth@gmail.com
Email sent successfully!
PS D:\kummetha harshavardhan\python> '''