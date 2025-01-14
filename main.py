import time, os, platform
try:
    from prettytable import PrettyTable
except:
    os.system("pip install prettytable")


# Color codes for terminal output
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'

def re(text):
    """Simulates a typing effect for the provided text."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)

# Initialize colorama on Windows
if 'Windows' in platform.uname():
    try:
        from colorama import init
        init()
    except ImportError:
        os.system("pip install colorama")
else:
    pass

# Banner for BlackPearl
banner = f"""
{k}                                                                 
                              -     -                             
                            .+       +.                           
                           :#         #:                          
                          =%           %-                         
           {lrd}BLACKPEARL{k}     -*%.   {g}TOOL{k}   .%+    {be}TELEGRAM      {k}       
                        #@:             -@#                      
                     :  #@:             :@*  :                   
                    -=  *@:             -@*  =-                  
                   -%   *@-             =@+   %-                 
                  -@=  .*@+             +@+.  =@-                
                 =@%   .+@%-    :.:    -@@+.   #@:               
                =@@#:     =%%-+@@@@@+-%%=     .#@@=              
                 .+%@%+:.   -#@@@@@@@#-   .:=#@%=                
                    -##%%%%%#*@@@@@@@*#%%%%%##-                  
                  .*#######%@@@@@@@@@@@%#######*.                
               .=#@%*+=--#@@@@@@@@@@@@@@@#--=+*%@#=.             
            .=#@%+:     *@@@@@+.   .+@@@@@*     :+%@#=.         
          :*@@=.    .=#@@@@@@@       @@@@@@@#=.    .=@@*.       
            =@+    .%@@*%@@@@@*     *@@@@@%*@@%.    +@=         
             :@=    +@# :@@@@@#     #@@@@%. #@+    =@:          
              .#-   :@@  .%@@#       #@@#.  @@:   -#.           
                +:   %@:   =%         %=   :@%   -+             
                 -.  +@+                   +@+  .-              
                  .  :@#                   #@:  .               
                      %@.    {cn}@BlackPearlTool{k}    .@%                    
                      :+@:               =@+:                   
                        =@:             :@-                     
                         -%.           .%:                      
                          .#           #.                       
                            +         +                         
                             -       -                     
"""

# Display banner and information table
re(banner)
re("Warning! Use this tool responsibly. Any misuse is the user's responsibility.")
print(f"{lrd}")

t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Info{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}Reporter Channel{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}Reporter Account{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}Reporter Group [Updating]{lrd}'])
print(t)

number = input(f"{gn}Enter Number : {cn}")
if number == "1":
    os.system("python report/reporter.py")
elif number == "2":
    os.system("python report/report.py")
elif number == "3":
    print("This section is being updated and will be added soon.\n\nChannel: @BlackPearlTool")
