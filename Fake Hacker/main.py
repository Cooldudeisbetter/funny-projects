from plugin import*


print(Colorate.Horizontal(Colors.green_to_black, string))
time.sleep(5)

print(Colors.red, "Data is found Data is encryptced")
   
custom_set = 'ABCDEFGHIJKMNOPQRSTUVWSYZabcdefghijkmnlopqrstuvwxyz'


random_letters = ''.join(random.choice(custom_set) for _ in range(59))
random_lettersTwo = ''.join(random.choice(custom_set) for _ in range(20))
print(Colors.green, "data decoded")
print(Colors.green, random_letters + Colors.blue, "<---Discord Token")
print(Colors.blue, "Pc name found" + Colors.blue, random_lettersTwo)
print(Colors.yellow, "Antivirus found Virus")
time.sleep(1)
print(Colors.yellow, "disableing Antivirus")
time.sleep(3)
print(Colors.green, "Antivirus Disabled")
time.sleep(1)
print(Colors.green, "Mouse Blocked")
print(Colors.green, "Keyboard Blocked")
print(Colors.yellow, "1 Lag users pc 2 dont lag pc")
lagpc = input(selectedchoice)
if lagpc == '1':
    print(Colors.red, "this is a fake hacking tool that is made for fun are you sure that you want to lag pc this will open about 100 tabs in your browser!! ")
    print(Colors.yellow, "if anything happens to your computer i will not be responsible for your pc")
    print(Colors.yellow, "y/n")
    lagpc2 = input(selectedchoice)
    if lagpc2 == 'y':

     lines = [
                "Discord TOken -->", random_letters, "\n"
                "Pc name -->", random_lettersTwo, "\n"
            ]
    
    # Open file in write mode ('w')
    with open('Victim', 'w') as file:
        # Write multiple lines to the file
        file.writelines(lines)

    while True:
              webbrowser.open_new("https://d9utvt3h.forms.app/untitled-form-1")
              print("To stop lag you need to close the program!")


time.sleep(5)

if lagpc == '2':
     print(Colors.yellow, "ok writing data to new file when file is created copy the cresidentials and remove the data")
     time.sleep(4)
             
     linestwo = [
                "Discord TOken -->", random_letters, "\n"
                "Pc name -->", random_lettersTwo, "\n"
            ]

       # Open file in write mode ('w')
     with open('Victim', 'w') as file:
        # Write multiple lines to the file
        file.writelines(linestwo)



