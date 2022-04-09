# Youtube : sd._sttri

# Twitter : sadra_sattari

# instagram : sd._sttri

# random   colorama    time    os  

# windows => pip install random  

# linux   => sudo apt install colorama

from unittest import result
from colorama import init ,Fore
import  time 
import os 
import random

init()

def logo() :
    print(Fore.YELLOW + """
                   ...                                 ..                                                
          .Y#&&@@: ?PPPPGPY:                  :5#&&@& .GGGGGGGG7.GGGGGGGG7 YP555J!:   !#BBG         
         .&@@@@&#: B@@@BG@@@7                :&@@@@&B :@@@@@@@@P^@@@@@@@@P &@@@##@@B  J@@@@.        
         ^@@@@Y    G@@@J^@@@&                ?@@@@7   .G#@@@@BG?.G#@@@@BG7 &@@@::@@@: J@@@&         
         .&@@@&G^  G@@@J^@@@@.               :@@@@&P.   :@@@@:    :@@@@.   &@@@B&@@#  J@@@&         
          :B@@@@@! G@@@?~@@@&.                ^#@@@@@:  :@@@@:    :@@@@.   &@@@@@@@^  ?@@@&         
         .  ^&@@@G G@@@?Y@@@B :##&J          .  !@@@@J  :@@@@.    :@@@&.   #@@@Y&@@#. 7@@@&         
         ~@&&@@@@^ G@@@&@@@&: :@@@# .??????^ J@&&@@@&.  :@@@@.    :@@@&    #@@@~:@@@J ~@@@&         
         .B&&&#P:  !GPPGPY!   .&&&B !@@@@@@# :#&&&#Y.   .PGGP     .GGG5    7GP5. ~G^  :#GGY         
                                    ~@&&&&@B                                                        

    """)

def tool() :
    U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    L = "abcdefghijklmnopqrstuvwxyz"
    N = "1234567890"
    C = "!@#$%^&*(){}[]"
    x = U + L + N + C
    len = int(input(" please Enter your pass lenght: "))
    result = "".join(random.sample(x , len  ))
    print(Fore.BLUE + " your password is : " + Fore.GREEN + str(result))
    f = open("result-pass.txt" , "a")
    f.write(result + "\r\n")

logo()

time.sleep(3)

tool()
os.system("pause")
