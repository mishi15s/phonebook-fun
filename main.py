phonebook={}
def showmenu():
    print("=================================================================================================")
    print("📱📖 PhoneBook Application")
    print("1.Add new contact")
    print("2.View all contacts" )
    print("3.Search contact ")
    print("4.Update contact")
    print("5.Delete contact")
    print("6.Exit")
    print("================================================================================================")
def addcontact():
    name=input("Enter the name:").strip().lower()
    if name in phonebook:
        print("Contact already exists")
    phone=input("Enter a phone number:").strip()  
    phonebook[name]=phone
    print("Contact added successfully✔️")
def vac():
    if not phonebook:
        print("Phonebook is empty.Add a contact to get started")
        return
    print("All contacts📃")  
    print("---------------------------------")   
    for name,number in phonebook.items():
        print(f"Name:{name}-Phonenumber:{phonebook[name]}")
def search():
    name=input("Enter the name to be searched:")
    if name not in phonebook:
        print("Contact does not exist ❌")
    else :
        print("Contact found")
        print(f"Name:{name}-Phonenumber:{phonebook[name]}")
def uc():
    name=input("Emter the name to be updated:").strip().lower()
    if name not in phonebook:
        print("Contact does not exist ❌")
    else :
        nn=input("Enter the new number:")
        phonebook[name]=nn
        print("Contact updated successfully✔️")
def dc():
    name=input("Emter the name to be deleted:").strip().lower()
    if name not in phonebook:
        print("Contact does not exist ❌")
    else :
        del phonebook[name]
        print("Contact deleted ❌")
           
while True :
    showmenu()        
    ch=input("Enter your choice :")
    if ch=="1":
        addcontact()
    elif ch=="2"  :
        vac()  
    elif ch=="3"  :
        search()  
    elif ch=="4"  :
        uc()  
    elif ch=="5"  :
        dc() 
    elif ch=="6"   :
        break     
    else  :
        print("❌❌Invalid input❌❌")
