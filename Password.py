
import math
import random
stoixeia1 = []
stoixeia2 = []
stoixeia3 = []
stoixeia4 = []
  

def CreatePassword(a,b,c,d,length,length1):
    #gia kathe stoixeio tou input tou xristi, kovei to string se mikos length.
    for index in range(0, len(a), length1):
        stoixeia1.append(a[index : index + length1])
   
    for index in range(0, len(b), length1):
        stoixeia2.append(b[index : index + length1])
   
    for index in range(0, len(c), length1):
        stoixeia3.append(c[index : index + length1])
    #edw logw tou floor pou xrisimopoihsame(se periptwsh eisagwgis monou arithmou mikous password) to mikos tha einai length-3*length.
    for index in range(0, len(d), length-(3*length1)):
        stoixeia4.append(d[index : index + length-(3*length1)])

    stoixeia = []
    #vazoume ta kommena stoixeia se enan neo pinaka, pou tha exei 4 elements mesa pou einai idi kommena. (fav num, fav color, pet name, last name)
    stoixeia.append(stoixeia1[0])
    stoixeia.append(stoixeia2[0])
    stoixeia.append(stoixeia3[0])
    stoixeia.append(stoixeia4[0])
    random.shuffle(stoixeia)
    #print(stoixeia)
    #kanoume ola ta elements join, wste na dimiourgithei ena string.
    password=''.join(stoixeia)
    #print(password) #print(password) before adding special characters

    #replace letters with special characters
    return password.replace('o','0').replace('i','!').replace('a','@').replace('s','$').capitalize()
   
    #letter O -> 0
    #lettel i -> !
    #letter a -> @
    #set first letter to capital
    #letter s -> $
    


def main():
    
    print("--CREATE YOUR PASSWORD--")
    a = input('Give your favorite number: ')
    b = input('Give your favorite color: ')
    c = input('Give the name of your pet:')
    d = input('Give your last name: ')
    length = int(input('Set the length of your password: '))
    length1=math.floor((length/4)) #efoson zita 4 stoixeia, diairei to mikos pou thelei o xristis gia to password
                                #to length1 pou prokuptei tha einai to mikos tou kathe stoixeiou pou tha xrisimopoihthei gia to password/
    
    listofpasswords =[] #lista pou tha apothikeuontai ola ta passwords pou dimiourgoume.
    while True:
        
        password = CreatePassword(a,b,c,d,length,length1) #kaloume ti sunartisi pou dimiourgei ta passwords, me parametrous ta stoixeia p dinei o xristis
        #until generate a password that is not in list of passwords
        while password in listofpasswords: #psaxnei prwta an yparxei to password pou dimiourghse, hdh sti lista
            print(password+" exists in list. Generating new password!!!")
            password = CreatePassword(a,b,c,d,length,length1)#dimiourgei kainourio
            
        print("New password is : "+password+"\n") 
        listofpasswords.append(password) #prosthetei to password sti lista me ta upoloipa.
        #elegxos an thelei na dimiourghsei epipleon passwords, an oxi tupwnei osa exei dimiourghsei k telos.
        answer = input('Do you want to create more passwords?')
        if answer=='yes':
           continue
        else:
            print(listofpasswords)
            exit()
    
#dhlwsh main sunarthshs.
if __name__== "__main__":
    main()


