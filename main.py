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
while True :
    showmenu()        
    ch=input("Enter your choice :")
    if ch=="1":
        addcontact()
    elif ch=="2"  :
        vac()  