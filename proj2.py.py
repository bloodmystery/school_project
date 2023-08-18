import mysql.connector as sqltor

db = sqltor.connect(host='localhost',user='root',password='vivek')

cursor=db.cursor()

cursor.execute('''create database if not exists football''')
cursor.execute('''use football''')
cursor.execute('''CREATE TABLE IF NOT EXISTS FOOTBALLLEAGUE
                (SNO int(3) primary key,
               TEAMNAME varchar(20),
               REGION varchar(20),
               MATCHESPLAYED int(4),
               WINS int(4),
               LOSE int(4),
               TIED int(4),
               NOOFGOALS int(4),
               TOTALPOINTS int(4))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS CHENNAIPLAYERS
                (SNO int(3) primary key,
               NAME varchar(20),
               DOB date,
               GOALS int(4),
               ASSIST int(4),
               DEFEND int(4))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS KERALAPLAYERS
                (SNO int(3) primary key,
               NAME varchar(20),
               DOB date,
               GOALS int(4),
               ASSIST int(4),
               DEFEND int(4))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS GUJARATPLAYERS
                (SNO int(3) primary key,
               NAME varchar(20),
               DOB date,
               GOALS int(4),
               ASSIST int(4),
               DEFEND int(4))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS MADURAIPLAYERS
                (SNO int(3) primary key,
               NAME varchar(20),
               DOB date,
               GOALS int(4),
               ASSIST int(4),
               DEFEND int(4))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS PLAYINGS
                (SNO int(3) primary key,
               TEAMPLAYED varchar(20),
               DATEOFMATCH date,
               TEAMWON varchar(20),
               NOOFGOALS int(3))''')

# 1st TABLE OF DATABASE FOOTBALL
def insert():
    a=int(input('ENTER SNO:'))
    b=input('ENTER TEAMNAME:')
    c=input('ENTER REGION: ')
    d=int(input('ENTER MATCHESPLAYED:'))
    e=int(input('ENTER WINS:'))
    f=int(input('ENTER LOSE:'))
    g=int(input('ENTER TIED:'))
    h=int(input('ENTER NOOFGOALS:'))
    i=int(input('ENTER TOTALPOINTS:'))
    cursor.execute('''INSERT INTO FOOTBALLLEAGUE VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(a,b,c,d,e,f,g,h,i))
    db.commit()


def winner():
    cursor.execute('''select * from FOOTBALLLEAGUE where TOTALPOINTS=(select max(TOTALPOINTS) from FOOTBALLLEAGUE);''')
    
    a=cursor.fetchall()
    print('THE WINNER IS: ')
    print('TEAM NAME\t\tWINS\tLOSE\tTIED\tNO OF GOALS\tTOTAL POINTS')
    for i in a:
        print(i[1],'\t\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t\t',i[8])
    
def search():
    while(1):
        print(''' FOR SEARCH
                 1.TEAM NAME
                 2.REGION
                 3.MATCHES PLAYED
                 4.WINS
                 5.LOSE
                 6.TIED
                 7.NO OF GOALS
                 8.TOTAL POINTS
                 9.EXIT''')
        ch = int(input("Enter the sno. to be searched : "))
        if(ch==1):
            cursor.execute("SELECT "+ "TEAMNAME" + " from FOOTBALLLEAGUE")        
            row =cursor.fetchall()
            print("TEAM NAME")
            for i in row:
                print(i[0])
        elif(ch==2):
            cursor.execute("SELECT "+ "REGION" + " from FOOTBALLLEAGUE")        
            row =cursor.fetchall()
            print("REGION")
            for i in row:
                print(i[0])
        elif(ch==3):
            cursor.execute("SELECT "+ "MATCHESPLAYED" + " from FOOTBALLLEAGUE")        
            row =cursor.fetchall()
            print("MATCHES PLAYED")
            for i in row:
                print(i[0])
        elif(ch==4):
            cursor.execute("SELECT "+ "WINS" + " from FOOTBALLLEAGUE")        
            row =cursor.fetchall()
            print("WINS")
            for i in row:
                print(i[0])
        elif(ch==5):
            cursor.execute("SELECT "+ "LOSE" + " from FOOTBALLLEAGUE")        
            row =cursor.fetchall()
            print("LOSE")
            for i in row:
                print(i[0])
        elif(ch==6):
            cursor.execute("SELECT "+ "TIED" + " from FOOTBALLLEAGUE")        
            row =cursor.fetchall()
            print("TIED")
            for i in row:
                print(i[0])
        elif(ch==7):
            cursor.execute("SELECT "+ "NOOFGOALS" + " from FOOTBALLLEAGUE")        
            row =cursor.fetchall()
            print("NO OF GOALS")
            for i in row:
                print(i[0])
        elif(ch==8):
            cursor.execute("SELECT "+ "TOTALPOINTS" + " from FOOTBALLLEAGUE")        
            row =cursor.fetchall()
            print("TOTAL POINTS")
            for i in row:
                print(i[0])
        elif(ch==9):
            break
        else:
            print("INVALID INPUT")
            
def points():
    cursor.execute('''SELECT * FROM FOOTBALLLEAGUE ORDER BY TOTALPOINTS DESC ;''')
    row = cursor.fetchall()
    print("TEAMNAME\t","REGION\t\t","MATCHESPLAYED\t","WINS\t","LOSE\t","TIED\t","NOOFGOALS\t","TOTALPOINTS")
    for c in row:
        print(c[1],"\t",c[2],"\t\t",c[3],"\t\t",c[4],"\t",c[5],"\t",c[6],"\t",c[7],"\t\t",c[8])

# 2ND TABLE OF DATABASE PLAYERS
def playersinsert1():
    a=int(input('ENTER SNO: '))
    b=input('ENTER THE PLAYER: ')
    c=input('ENTER THE DOB YYYY/MM/DD :')
    d=int(input('ENTER NO.OF GOALS: '))
    e=int(input('ENTER NO. OF ASSIST: '))
    f=int(input('ENTER NO.OF DEFEND: '))
    cursor.execute('''INSERT INTO CHENNAIPLAYERS VALUES
(%s,%s,%s,%s,%s,%s)''',(a,b,c,d,e,f))
    db.commit()

def playersinsert2():
    a=int(input('ENTER SNO: '))
    b=input('ENTER THE PLAYER: ')
    c=input('ENTER THE DOB YYYY/MM/DD :')
    d=int(input('ENTER NO.OF GOALS: '))
    e=int(input('ENTER NO. OF ASSIST: '))
    f=int(input('ENTER NO.OF DEFEND: '))
    cursor.execute('''INSERT INTO KERALAPLAYERS VALUES
(%s,%s,%s,%s,%s,%s)''',(a,b,c,d,e,f))
    db.commit()
    
def playersinsert3():
    a=int(input('ENTER SNO: '))
    b=input('ENTER THE PLAYER: ')
    c=input('ENTER THE DOB YYYY/MM/DD :')
    d=int(input('ENTER NO.OF GOALS: '))
    e=int(input('ENTER NO. OF ASSIST: '))
    f=int(input('ENTER NO.OF DEFEND: '))
    cursor.execute('''INSERT INTO GUJARATPLAYERS VALUES
(%s,%s,%s,%s,%s,%s)''',(a,b,c,d,e,f))
    db.commit()

def playersinsert4():
    a=int(input('ENTER SNO: '))
    b=input('ENTER THE PLAYER: ')
    c=input('ENTER THE DOB YYYY/MM/DD :')
    d=int(input('ENTER NO.OF GOALS: '))
    e=int(input('ENTER NO. OF ASSIST: '))
    f=int(input('ENTER NO.OF DEFEND: '))
    cursor.execute('''INSERT INTO MADURAIPLAYERS VALUES
(%s,%s,%s,%s,%s,%s)''',(a,b,c,d,e,f))
    db.commit()


# 3RD TABLE OF DATABASE MATCHES
def insertmatches():
    a=int(input('ENTER SNO:'))
    b=input('ENTER TEAM PLAYED:')
    c=input('ENTER THE DATE OF MATCH YYYY/MM/DD :')
    d=input('ENTER THE TEAM NAME WHO WON:')
    e=int(input('ENTER NO OF GOALS:'))
    cursor.execute('''INSERT INTO PLAYINGS VALUES
(%s,%s,%s,%s,%s)''',(a,b,c,d,e))
    db.commit()




while(1):
    print('''
              MENU OF TABLES
              1.FOOTBALL LEAGUE
              2.PLAYERS
              3.MATCHES
              4.EXIT''')
    a=int(input('ENTER YOUR CHOICE: '))
    if (a==1):
        while(1):
          print('''
                   MENU
                   1.INSERT TEAMS
                   2.SEARCH RECORDS
                   3.DISPLAY POINTS TABLE
                   4.WINNER OF MATCH
                   5.EXIT''')
          ch=int(input("ENTER CHOICE: "))
          if  (ch==1):
              insert()
              
          elif(ch==2):
              search()

          elif(ch==3):
              points()

          elif(ch==5):
              break
          elif(ch==4):
              winner()
          elif(ch==5):
              break
            
          else:
              print('INVALID INPUT')

    elif (a==2):
        while(1):
            print('''
                  MENU
                  1.INSERT FOR CHENNAI PLAYERS
                  2.SHOW CHENNAI PLAYERS INFO
                  3.INSERT FOR KERALA PLAYERS
                  4.SHOW KERALA PLAYERS INFO
                  5.INSERT FOR GUJARAT PLAYERS
                  6.SHOW GUJARAT PLAYERS INFO 
                  7.INSERT FOR MADURAI PLAYERS
                  8.SHOW MADURAI PLAYERS INFO
                  9.EXIT''')
            b=int(input('ENTER YOUR CHOICE'))
            if (b==1):
                  playersinsert1()
            elif(b==2):
                cursor.execute('''SELECT * FROM CHENNAIPLAYERS''')
                data=cursor.fetchall()
                for i in data:
                     print(i)
            elif(b==3):
                playersinsert2()
            elif(b==4):
                cursor.execute('''SELECT * FROM KERALAPLAYERS''')
                data=cursor.fetchall()
                for i in data:
                     print(i)
            elif(b==5):   
                 playersinsert3()
            elif(b==6):
                cursor.execute('''SELECT * FROM GUJARATPLAYERS''')
                data=cursor.fetchall()
                for i in data:
                    print(i)
            elif(b==7):
                playersinsert4()
            elif(b==8):
                cursor.execute('''SELECT * FROM MADURAIPLAYERS''')
                data=cursor.fetchall()
                for i in data:
                    print(i)
            elif(b==9):
                break
            else:
                  print("INVALID INPUT")
                  
    elif(a==3):
        while(1):
            print('''
                      MENU
                      1.INSERT MATCHES
                      2.SHOW FULL MATCHES
                      3.SHOW WHO WON MORE MATCHES
                      4.SHOW WHO WON LESS MATCHES
                      5.EXIT''')
            c=int(input('ENTER YOUR CHOICE'))
              
                     
            if (c==1):
                      insertmatches()
            elif (c==2):
                      cursor.execute('''select * from playings''')
                      data=cursor.fetchall()
                      for i in data:
                          print(i)
            elif (c==3):
                      cursor.execute('''drop table if exists result''')
                      db.commit()
                      cursor.execute('''create table as (select teamwon,count(*) won from playing group by teamwon''')
                      cursor.execute('''select teamwon from result where won=(select max(won) from result)''')
                      wonteam=cursor.fetchall()
                      print(wonteam[0][0])
            elif(c==4):
                      cursor.execute('''drop table if exists result''')
                      db.commit()
                      cursor.execute('''create table as (select teamwon,count(*) won from playing group by teamwon''')
                      cursor.execute('''select teamwon from result where won=(select min(won) from result)''')
                      wonteam=cursor.fetchall()
                      print(wonteam[0][0])
            elif (c==5):
                      break
            else:
                print('INVALID INPUT')
    elif (a==4):
        break
    else:
        print("INVALID INPUT")

db.close()

