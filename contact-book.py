#Contact Book Py 
import os
import tkinter
from tkinter import messagebox

contact_book = {"john": "12345678", "rick": "23456789" , "alice": "87654321"}

def add_contact():
    name = input("Enter your name: ")
    name = name.lower()
    number = input("Enter your 8 digit number: ")

    if not name.isalpha():#not a-z(Check for invalid first)
        print("Invalid name! Name must be a-z only")
        return # Exit here when invalid #Ref ai
        
    else:
        print(f"name '{name}' has been added!")
        
    if not number.isdigit() or len(number) !=8: #NOT 0-9, Not 8 digit only
        print("Invalid! Numbers must be from 0-9 and has 8 digits")
        return
        
    else:
        print(f"number {number} has been added!")

    if name.isalpha() and number.isdigit() and len(number) ==8: # Ref Ai
        contact_book[name] = number

def view_contact():
    if not contact_book:
        print("Contact not avaliable")
        return
    else: 
        print("Contact is avaliable")
    
    for name, number in contact_book.items():
        print(f"Name: '{name}'| Number: '{number}'")
    
def search_contact():
    search_name = input("Enter name to search: ")
    
    if search_name in contact_book: # Ref ai
        print(f"Name: '{search_name}' | Number: '{contact_book[search_name]}'")
    else:
        print("User doesn't exists")

def delete_contact():
    name = input("Enter a name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"You have deleted the contact {name}!")
    else:
        print("Contact not found!")

while True:  #Ref ai
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4: Delete Contact")
    print("5. Exit") 

    choice = input("Enter choice: ")

    if choice == "1": #Ref ai
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break