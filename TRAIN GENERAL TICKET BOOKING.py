import mysql.connector as sqlcon
import random def createdb(): global mydb global mycur mydb=sqlcon.connect( host="localhost",
user="root",
password="NeeRaja$1915",
database="NeeRaja"
)
if mydb.is_connected(): print("\t\t\t\t welcome to general booking.")
mycur=mydb.cursor()
gen1=("create table if not exists trainers (Sno int(100) primary key,Aadhar_number int(100), PASSANGER_NAME varchar(100), AGE
int(40),Mobile_number int(100),from1 varchar(100),to1 varchar(100),Train_number varchar(100),distance varchar(100),Train_name varchar(100),Train_timings
varchar(100),Ticket_price varchar(100),Seats_available varchar(100))") mycur.execute(gen1)
7
createdb() def Display_GeneralSeats():
print("================================================= ===================================================== =================================================") print("/Sno DESTINATION_PLACE ARRIVAL_PLACE
DISTANCE TRAIN_NUMBER TRAIN_NAME
TRAIN_TIMMINGS TICKET_PRICE SEATS_AVAILABLE /")
print("================================================= =====================================================
=================================================") print("1. TIRUPATHI VIJAYAVADA 450Km 12625 KERELA_EXPRESS 4:50AM-11:00AM 700 120
")
print("2. VISAKAPATNAM KADAPA 500Km 17488 TIRUMALA_EXPRESS 2:00PM-7:00AM 800
200 ")
print("3. GUNTUR SECUNDERABAD 750Km
12733 NARAYANADRI_EXPRESS 12:30AM-5:30AM 900
380 ")
print("4. BANGLORE NEW DELHI 2000Km 12627 KARNATAKA_EXPRESS 7:30PM-9:00AM 2000 530
")
print("5. ONGOLE NELLORE 600Km 17210 SESHADRI_EXPRESS 12:50PM-2:20AM 1300 890
")
print("================================================= =====================================================
=================================================") def Passanger_Details(): gen2="select * from trainers" mycur.execute(gen2)
r2=mycur.fetchall()
8
print("================================================= =====================================================
===================================================== =====================================================
")
print("/Sno Aadhar_number PASSANGER_NAME AGE Mobile_number DESTINATION_PLACE ARRIVAL_PLACE
DISTANCE TRAIN_NUMBER TRAIN_NAME
TRAIN_TIMMINGS TICKET_PRICE SEATS_AVAILABLE
/")
print("================================================= ===================================================== ===================================================== =====================================================
")
for i in range(len(r2)): print("| ",end="") print(str(r2[i][0]).ljust(22," "),end="|") print(str(r2[i][1]).ljust(17," "),end="|") print(str(r2[i][2]).ljust(17," "),end="|") print(str(r2[i][3]).ljust(17," "),end="|") print(str(r2[i][4]).ljust(15," "),end="") print(str(r2[i][5]).ljust(17," "),end="|") print(str(r2[i][6]).ljust(18," "),end="|") print(str(r2[i][7]).ljust(14," "),end="|")
print(str(r2[i][8]).ljust(15," "),end="|") print(str(r2[i][9]).ljust(16," "),end=" ") print(str(r2[i][10]).ljust(16," "),end=" ") print(str(r2[i][11]).ljust(16," "),end=" ") print(str(r2[i][12]).ljust(16," "),end=" ") print()
print("================================================= =====================================================
9
=====================================================
=============================================")
TP1,TP2,TP3,TP4,TP5 = 700,800,900,2000,1300
def Book_General_Seats(): global Seats
global TICKET_PRICE
global name
Sno = int(input("Enter the id: "))
Aadhar_number =int(input("Enter your aadhar number:"))
PASSANGER_NAME= str(input("Enter the name of the passenger: "))
AGE=int(input("Enter your age:"))
Mobile_number= input("Enter your mobile number:")
DESTINATION_PLACE =input("Enter the Destination Place: ") ARRIVAL_PLACE =input("Enter the Arrival Place: ")
DISTANCE =input("Enter the distance:")
TRAIN_NUMBER =int(input("Enter the Train Number: ")) print("
KERELA_EXPRESS,TIRUMALA_EXPRESS,NARAYANADRI_EXPR
ESS,KARNATAKA_EXPRESS,SESHADRI_EXPRESS")
TRAIN_NAME=input("Enter the Train Name: ") if TRAIN_NAME == "KERELA_EXPRESS": TICKET_PRICE = TP1
print(TP1," Rs per ticket")
elif TRAIN_NAME == "TIRUMALA_EXPRESS": TICKET_PRICE = TP2
print(TP2," Rs per ticket")
elif TRAIN_NAME == "NARAYANADRI_EXPRESS": print(TP3," Rs per ticket") TICKET_PRICE = TP3 elif TRAIN_NAME == "KARNATAKA_EXPRESS":
print(TP4," Rs per ticket") TICKET_PRICE = TP4 elif TRAIN_NAME == "SESHADRI_EXPRESS":
10
print(TP5," Rs per ticket") TICKET_PRICE = TP5 else:
print("please select the train in given list.")
TRAIN_TIMMINGS =str(input("Enter the Train Timings: ")) #TICKET_PRICE =int(input("Enter the Ticket Price: "))
SEATS_AVAILABLE =int(input("Enter the no.of Seats: "))
gen3 = "insert into Trainers values
('"+str(Sno)+"','"+str(Aadhar_number)+"','"+str(PASSANGER_NAME)+"'
,'"+str(AGE)+"','"+str(Mobile_number)+"','"+str(DESTINATION_PLACE )+"','"+str(ARRIVAL_PLACE)+"','"+str(DISTANCE)+"','"+str(TRAIN_N UMBER)+"','"+str(TRAIN_NAME)+"','"+str(TRAIN_TIMMINGS)+"','"+ str(TICKET_PRICE)+"','"+str(SEATS_AVAILABLE)+"')" mycur.execute(gen3)
print("Record has been added successfully")
def General_bill(): gen4 = "select * from Trainers" mycur.execute(gen4) r3 = mycur.fetchall() print("Your bill") person_1 = input("Enter the name of the passenger: ") for i in range(len(r3)):
a = r3[i][2] if person_1 == a: Seats = int(r3[i][12]) cost = int(r3[i][11])
print("Total number of seats you booked: ",r3[i][12]) print("your seat numbers are: ")
for i in range(Seats):
print(random.randrange(1,1000),end = ",") print(" ")
total_amount = cost * Seats print("Total Amount = ",total_amount) while True:
print("\n\n----------------------------------------------------DETAILS------------
----------------------------------------------------------------------------") print("(1)ACSeats (2)GENERALSeats (3)EXIT")
11
option=int(input("please enter your option:")) if(option==2): while True:
print("(1)Display_GeneralSeats (2)Book_General_Seats
(3)Passanger_Details (4)General_bill (5)Exit ") option2=int(input("Please enter your option:")) if(option2==1):
Display_GeneralSeats () elif(option2==2):
Book_General_Seats () elif(option2==3): Passanger_Details () elif(option2==4): General_bill () elif(option2==5):
break
if(option==3): mydb.commit() break