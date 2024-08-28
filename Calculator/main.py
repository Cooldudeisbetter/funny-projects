from plugin import*

div = """
██████  ██ ██    ██ ██ ███████  ██████  ███    ██ 
██   ██ ██ ██    ██ ██ ██      ██    ██ ████   ██ 
██   ██ ██ ██    ██ ██ ███████ ██    ██ ██ ██  ██ 
██   ██ ██  ██  ██  ██      ██ ██    ██ ██  ██ ██ 
██████  ██   ████   ██ ███████  ██████  ██   ████ 
                                                  
                                                  
"""

multi = """
███    ███ ██    ██ ██      ████████ ██ ██████  ██      ██  ██████  █████  ████████ ██  ██████  ███    ██ 
████  ████ ██    ██ ██         ██    ██ ██   ██ ██      ██ ██      ██   ██    ██    ██ ██    ██ ████   ██ 
██ ████ ██ ██    ██ ██         ██    ██ ██████  ██      ██ ██      ███████    ██    ██ ██    ██ ██ ██  ██ 
██  ██  ██ ██    ██ ██         ██    ██ ██      ██      ██ ██      ██   ██    ██    ██ ██    ██ ██  ██ ██ 
██      ██  ██████  ███████    ██    ██ ██      ███████ ██  ██████ ██   ██    ██    ██  ██████  ██   ████ 
                                                                                                          
                                                                                                          
"""

subtract = """
███████ ██    ██ ██████  ████████ ██████   █████   ██████ ████████ 
██      ██    ██ ██   ██    ██    ██   ██ ██   ██ ██         ██    
███████ ██    ██ ██████     ██    ██████  ███████ ██         ██    
     ██ ██    ██ ██   ██    ██    ██   ██ ██   ██ ██         ██    
███████  ██████  ██████     ██    ██   ██ ██   ██  ██████    ██    
                                                                   
                                                                   
"""

logo = """
 ██████  █████  ██       ██████ ██    ██ ██       █████  ████████  ██████  ██████  
██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
██      ███████ ██      ██      ██    ██ ██      ███████    ██    ██    ██ ██████  
██      ██   ██ ██      ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
 ██████ ██   ██ ███████  ██████  ██████  ███████ ██   ██    ██     ██████  ██   ██ 
                                                                                   
                                                                                   
"""

add = """
 █████  ██████  ██████  
██   ██ ██   ██ ██   ██ 
███████ ██   ██ ██   ██ 
██   ██ ██   ██ ██   ██ 
██   ██ ██████  ██████  
                        
                        
"""

print(colorama.Fore.RED, logo)
print("")
print(Colors.red, "1 Add  2 subtraction 3 multiplication 4 divison")
CHOOSE = input(selectedchoice)
if CHOOSE == '1':
    clear()
    print(colorama.Fore.RED, add)
    print(colorama.Fore.RED, "Give the numbers to add")
    CHOOSE2 = input(selectedchoice)
    num1 = CHOOSE2
    CHOOSE3 = input(selectedchoice)
    num2 = CHOOSE3
    newnum1 = int(num1)
    newnum2 = int(num2)

    res = newnum1 + newnum2

    print(colorama.Fore.GREEN, res)
    time.sleep(3)
    clear()
    os.system("py main.py")

if CHOOSE == '2':
    clear()
    time.sleep(0.5)
    print(colorama.Fore.RED, subtract)
    print("")
    print(Colors.yellow, "enter the two numbers")
    CHOOSE4 = input(selectedchoice)
    sub1 = CHOOSE4
    CHOOSE5 = input(selectedchoice)
    sub2 = CHOOSE5
    subnew1 = int(sub1)
    subnew2 = int(sub2)
    resub = subnew1 - subnew2
    print(Colors.green, resub)
    time.sleep(5)
    clear
    os.system("py main.py")

if CHOOSE == '3':
    time.sleep(0.5)
    clear()
    print(colorama.Fore.RED, multi)
    print("")
    print(Colors.yellow, "Enter first number")
    CHOOSE6 = input(selectedchoice)
    multinum1 = CHOOSE6
    CHOOSE7 = input(selectedchoice)
    multinum2 = CHOOSE7
    multicon1 = int(multinum1)
    multicon2 = int(multinum2)
    print(Colors.green, multicon1 * multicon2)
    time.sleep(7)
    clear()
    os.system("py main.py")

if CHOOSE == '4':
    time.sleep(0.5)
    clear()
    print(colorama.Fore.RED, div)
    print("")
    print(Colors.yellow, "Enter the first number")
    CHOOSE8 = input(selectedchoice)
    print(Colors.yellow, "Enter second number")
    CHOOSE9 = input(selectedchoice)
    divcon = int(CHOOSE8)
    divcon2 = int(CHOOSE9)
    divres = divcon // divcon2
    print(Colors.green, divres)
    time.sleep(10)
    clear()
    os.system("py main.py")


