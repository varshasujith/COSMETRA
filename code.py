import pickle as pic
import os
f = open("cosmetra.dat" , "rb")
r = [[100, "SKINCARE" , "FENTY BEAUTY FOUNDATION" , 175],[101, "SKINCARE" , "MAC CONCEALER" , 115], [102 , "SKINCARE" , "SEPHORA BRONZER" ,  71],[103 , "SKINCARE", "LAKME BLUSH", 46],[104 ,"SKINCARE" , "SEPHORA HIGHLIGHTER" , 85],[105, "EYECARE" , "HUDABEAUTY EYELINER" , 125],[106, "EYECARE", "E.L.F MASCARA" , 20],[ 107, "EYECARE", "JAMES CHARLES X MORPHE PALLETE", 239],[108, "LIPCARE , KYLIE COSMETICS LIPLINER" , 185],[109, "LIPCARE", "NYX LIPSTICK", 27]]
for i in range:
    pic.dump(i,f)
f.close()
1)VIEW 

def viewitem(itemno):
    f = open("cosmetra.dat" . "ab" )
    try:
        found = 0
        while True:
            l = pic.load(f)
            if l[0] == n:
               found = 1
               print("Item typ: ",l[1])
               print("Description: ",l[2])
               print("Amount: ",l[3])
except:
     pass
if found == 0:
       print("Record Not Found")
f.close()

2) ADD
    
def additem(itemno):
    f = open("cosmetra.dat" . "ab" )
    it.no = int(input("Item Number = "))
    it.typ = input("Item Type:"))
    desc = input("Description:")
    amnt = int(input("Price="))
    l = [it.no, it.typ , desc , amnt ]
    pic.dump(l,r)
    f.close()
    print("New Item succesfully added")
    print(" Your Item Number = it.no")
3)MODIFY

def modifyitem(itemno):
    f1 = open("cosmetra.dat" . "rb"
    f2 = open("temp.dat". "ab")
    try:
       found = 0
       while True:
           l = pic.load(f1)
           it.no = l[0]
           it.typ =l[1]
           desc =l[2]
           amnt =l[3]
           if it.no == itemno:
              found = 1
              it.typ = input("Item Type: ")
              desc   = input("Description: ")
              amnt   = int(input("Price:")
           l1=[ it.no , it.typ, desc, amnt]
           pic.dump(l1,l2)
    except:
       pass
    if found == 1:
       f1.close()
       f2.close()
       os.remove("cosmetra.dat")
       os.rename("temp.dat" ,"cosmetra.dat")
       print(" Item information successfully updated")
    else:
        print("Record not found")
4) DELETE

def deleteitem(itemno):
    f1 = open("cosmetra.dat", "rb")
    f2 =open("temp.dat", "ab")
    try:
       found = 0
       while True:
           l = pic.load(f1)
           it.no = l[0]
           it.typ = l[1]
           desc   = l[2]
           amnt  = l[3]
           if it.no != itemno
                found = 1
                l1 = [it.no, it.typ, desc , amnt] 
                pic.dump(l1,l2)

    except:
        pass
    if found == 1:
        f1.close()
        f2.close()
        os.remove("cosmetra.dat")
        os.rename("temp.dat" ,"cosmetra.dat")
        print(" Item Deleted")
    else:
        print ("Record not found")
5)TRANSACTION


def transaction(itemno):
    f1 = open("cosmetra.dat", "rb")
    f2 =open("temp.dat", "ab")
    try:
       found = 0
       while True:
           l = pic.load(f1)
           it.no = l[0]
           it.typ = l[1]
           desc   = l[2]
           amnt  = l[3]
           if it.no != itemno
                found = 1
                l1 = [it.no, it.typ, desc , amnt] 
                pic.dump(l1,l2)
   except:
        pass
    if found == 1:
        f1.close()
        f2.close()
        os.remove("cosmetra.dat")
        os.rename("temp.dat" ,"cosmetra.dat")
        print(" Item Deleted")
    else:

        print ("Record not found")
6)RETAIL

def retail(itemno):
          f1 = open("cosmetra.dat", "rb")
          f2 =open("temp.dat", "ab")
          try:
             found = 0
             while True:
                 l = pic.load(f1)
                 it.no = l[0]
                 it.typ = l[1]
                 desc   = l[2]
                 amnt  = l[3]
                 if it.no == itemno:
                    add = int(input("Retail amnt:"))
                    found = 1
                l1 = [it.no, it.typ, desc , amnt+add] 
                pic.dump(l1,l2)
                else:
                    l1 =[it.no, it.typ , desc , amnt]
                    pic.dump(l1.f2)
          except:
            pass
          if found == 1:
             f1.close()
             f2.close()
             os.remove("cosmetra.dat") 
             os.rename("temp.dat","cosmetra.dat")
             print("Order successfull")
             print("Thank You for visiting COSMETRA,Please come again")
          else:
              print("Record not found")
7)WHOLESALE

def wholesale(itemno):
          f1 = open("cosmetra.dat", "rb")
          f2 = open("temp.dat", "ab")
          try:
             found = 0
             while True:
                 l = pic.load(f1)
                 it.no = l[0]
                 it.typ = l[1]
                 desc   = l[2]
                 amnt  = l[3]
                 if it.no == itemno:
                    add = int(input("Wholesale amnt:"))
                    found = 1
                l1 = [it.no, it.typ, desc , amnt+add] 
                pic.dump(l1,l2)
                else:
                    l1 =[it.no, it.typ , desc , amnt-taken]
                    pic.dump(l1.f2)
          except:
            pass
          if found == 1:
             f1.close()
             f2.close()
             os.remove("cosmetra.dat") 
             os.rename("temp.dat","cosmetra.dat")
             print("Order successfull")
          else:
              print("Record not found")
