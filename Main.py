import datetime
import smtplib
count=1
def home():
        try:
                a=1
                while a:
                        print("  Library management system  ".center(70,'#'))
                        a=int(input('''select a choice
1.Admin Login
2.Student Login
3.Admin Signup
4.Student Signup
0.Exit\n'''))
                        if a is 1:
                                adminlogin()
                        elif a is 2:
                                stdlogin()
                        elif a is 3:
                                adminsign()
                        elif a is 4:
                                stdsign()
                        elif a is 0:
                                print('Thanks for using our management system\n')
                                break
                        else:
                                print("OOOPS seems you need an eye checkup, kindly renter option:)\n")
                                
        except ValueError:
                print('OOPS!!! seems you pressed nothing, kindle renter\n')
                home()
                




def adminsign():
        print('  admin signin  '.center(60,'*'))
        b='%s,%s\n'%(input('enter new admin username\n'),input('enter new admin password\n'))
        if b.split(',')[0] in open('c:/Users/dell/Desktop/LMS/admin.txt').read():
                print('User already exists')
                a=int(input("press 1 to go to home screen"))
                if a is 1:
                        home()
                else:
                        print("Kindly enter right choice\n")


        else:
                open('c:/Users/dell/Desktop/LMS/admin.txt','a').write(b)
        a=int(input("press 1 to go to home screen"))
        if a is 1:
                home()
        else:
                print("Kindly enter right choice\n")

def adminlogin():
    print('   admin log in   '.center(60,'*'))
    b='%s,%s\n'%(input('Enter the admin username\n'),input('Enter the admin password\n'))
    if b in open('c:/Users/dell/Desktop/LMS/admin.txt').read():
        print('logged in')
        c=(int)(input('To add books press 1 \nTo check fine press 2 \n'))
        if c is 1:
            addbook()
        elif c is 2:
                fine()
    else:
        print('You need a serious eye checkup:)')
        a=int(input("press 1 to go to home screen"))
        if a is 1:
                home()
        else:
                print("Kindly enter right choice\n")

        

def stdsign():
    print('   student signin   '.center(60,'*'))
    b='%s,%s,%s\n'%(input('enter student name\n'),input('enter the student usn\n'),input('Enter Password\n'))
    if b.split(',')[1] in open('c:/Users/dell/Desktop/LMS/std.txt').read():
        print('User already exists')
        a=int(input("press 1 to go to home screen"))
        if a is 1:
                home()
        else:
                print("Kindly enter right choice\n")
    else:
        open('c:/Users/dell/Desktop/LMS/std.txt','a').write(b)
        a=int(input("press 1 to go to home screen"))
        if a is 1:
                home()
        else:
                print("Kindly enter right choice\n")



def stdlogin():
    print('   student log in   '.center(60,'*'))
    b='%s,%s'%(input('Enter the usn\n'),input('Enter the password\n'))
    if b in open('c:/Users/dell/Desktop/LMS/std.txt').read():
        print('logged in')
        issue=str(input("To go to issue section type yes\n"))
        if issue == 'yes':
                viewbook()
        else:
                print('Kindly enter right choice\n')
                
    else:
        print('You need a serious eye checkup:)')
        a=int(input("press 1 to go to home screen"))
        if a is 1:
                home()
        else:
                print("Kindly enter right choice\n")


def addbook():
    global count
    b='%s %s %s %s'%(input('Enter the name of the book without space\n'),input('Enter the isbn no.\n'),input('Currently issued or not enter False currently\n'),input('Date if issued enter none currently\n'))
    b=b+' '+str(count)+'\n'
    open('c:/Users/dell/Desktop/LMS/books.txt','a').write(b)
    c=open('c:/Users/dell/Desktop/LMS/books.txt')
    a=c.readlines()
    
    if (((a[-1]).split())[1]) in open('c:/Users/dell/Desktop/LMS/books.txt').read():
        count=count+1
    open('c:/Users/dell/Desktop/LMS/books.txt','a').write(b)
    c.close()
    choice=(int)(input('Enter 1 to add another book\n2 to go back to main menu\n'))
    if choice is 1:
            addbook()
    else:
            home()
    
    
    
    

def viewbook():
        print('You are in issue section\n')
        i=input('Enter the isbn no. of the book You want\n')
        c=open('c:/Users/dell/Desktop/LMS/books.txt')
        a=c.readlines()
        try:
                for j in range(len(a)):
                        isb=((a[j]).split())[1]
                        if isb == i:
                                r=j
                if (int)(((a[r]).split())[4])>0:
                        issue=input("Your book is available \nTo issue Type yes\n")
                        if issue == 'yes':
                                print('Your book is issued kindly collect it from Library\n')
                                count=(int)(((a[r]).split())[4])-1
                                l=a[r].split()
                                l[4]=str(count)
                                s=' '.join(l)
                                s=s+'\n'
                                open('c:/Users/dell/Desktop/LMS/books.txt','a').write(s)
                                l1=s.split()
                                l1[3]=str(datetime.datetime.today()).split()[0]
                                st=' '.join(l1)
                                st=st+'\n'
                                l2=st.split()
                                l2[2]='True'
                                s2=' '.join(l2)
                                s2=s2+'\n'
                                open('c:/Users/dell/Desktop/LMS/books.txt','a').write(s2)
                else:
                        print('Sorry This book is currently unavailable\n')
        except UnboundLocalError:
                print('Sorry the book you queried is currently unavailable in library\n')
                        
        c.close()
        choice=(int)(input('Enter 1 to query another book\n2 to go back to main menu\n'))
        if choice is 1:
                viewbook()
        else:
                home()
    

def fine():
        i=int(input('Enter the isbn no. of the book student returned\n'))
        c=open('c:/Users/dell/Desktop/LMS/books.txt')
        a=c.readlines()
        for j in range(len(a)):
                isb=((a[j]).split())[1]
                if isb==str(i):
                        r=j
        s=input('Enter the return date in dd format\n')
        s1=int(s)
        l=int(((a[r].split())[3])[-2::1])
        if s1<l:
                m=int(((a[r].split())[3])[6])
                if m is 1 or 3 or 5 or 7 or 8 or 10 or 12:
                        l=31-l
                else:
                        l=30-l
                if (s1+l)>7:
                        f1=abs(s1-l)
                        f=(f1-7)*10
                        print("Sorry You have to pay a fine of ₹%d on late return" % (f))
                        content = ('Pay fine of Rs %d' % (f))
                        mail=smtplib.SMTP('smtp.gmail.com',587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login('abhisheksri2013@gmail.com','sarahwalker')
                        s=input('enter email of student\n')
                        mail.sendmail('abhisheksri2013@gmail.com',s,content)
                        mail.close()                        
        elif ((s1-l))>7:
                f1=abs(s1-l)
                f=(f1-7)*10
                print("Sorry You have to pay a fine of ₹%d on late return" % (f))#per day fine is rs10
        else:
                print('You have no fine. You are SAFE:)\n')
        c.close()
        choice=(int)(input('Enter 1 to query another fine\n2 to go back to main menu\n'))
        if choice is 1:
                fine()
        else:
                home()

wel=input('Enter yes to access Library management system\n')
if wel == 'yes':
        home()
else:
        print('Seems You entered wrong choice\n')
        
        
    
        
           
           
    
        
        
    
    
    
