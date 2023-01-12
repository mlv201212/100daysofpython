print('''
*******************************************************************************
                       _,.-------.,_
                            ,;~'             '~;,
                          ,;                     ;,
                         ;                         ;
                        ,'                         ',
                       ,;                           ;,
                       ; ;      .           .      ; ;
                       | ;   ______       ______   ; |
                       |  `/~"     ~" . "~     "~\'  |
                       |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                        |   |        }:{        |   |
                        |   l       / | \       !   |
                        .~  (__,.--" .^. "--.,__)  ~.
                        |     ---;' / | \ `;---     |
                         \__.       \/^\/       .__/
                          V| \                 / |V
       __                  | |T~\___!___!___/~T| |                  _____
    .-~  ~"-.              | |`IIII_I_I_I_IIII'| |               .-~     "-.
   /         \             |  \,III I I I III,/  |              /           Y
  Y          ;              \   `~~~~~~~~~~'    /               i           |
  `.   _     `._              \   .       .   /               __)         .'
    )=~         `-.._           \.    ^    ./           _..-'~         ~"<_
 .-~                 ~`-.._       ^~~~^~~~^       _..-'~                   ~.
/                          ~`-.._           _..-'~                           Y
{        .~"-._                  ~`-.._ .-'~                  _..-~;         ;
 `._   _,'     ~`-.._                  ~`-.._           _..-'~     `._    _.-
    ~~"              ~`-.._                  ~`-.._ .-'~              ~~"~
  .----.            _..-'  ~`-.._                  ~`-.._          .-~~~~-.
 /      `.    _..-'~             ~`-.._                  ~`-.._   (        ".
Y        `=--~                  _..-'  ~`-.._                  ~`-'         |
|                         _..-'~             ~`-.._                         ;
`._                 _..-'~                         ~`-.._            -._ _.'
   "-.="      _..-'~                                     ~`-.._        ~`.
    /        `.                                                ;          Y
   Y           Y                                              Y           |
   |           ;                                              `.          /
   `.       _.'                                                 "-.____.-'
     ~-----"
*******************************************************************************
''')
print("You have been kidnapped and wake up chained to a bed in a house youve never been in before.")
print("You unchain yourself and see a hallway to your left and right. Your mission is to escape without being killed.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
hallway = input("Will you enter the left or right hallway?\n")


if hallway == "left":
  print("Oh no that way was booby trapped and you died by spikes.") 
  quit("Game Over")
  
else:
  print("After entering the right hallway you find a room with the person who kidnapped you sleeping.")

decide = input("Do you enter the room or keep walking\n")

if decide == "enter" or decide == "enter the room":
  print("You woke him up and he killed you with a knife")
  quit("Game Over")
  
else:
    print("As you kept walking you reach the end of the hallway. There are three doors")

door = input("Which door will you go through? 1 2 or 3\n")

if door == "1":
  input("The door was unlocked and you escaped the house!")
  quit("You Lived and escaped!!!!!")
elif door == "2":
  print("The door was locked and as you tried to open it you woke up the killer. You are dead now.")
  quit("Game Over")
elif door == "3":
  print("You have opened the door but an alarm sounds, the killer finds you and you are dead.")
  quit("Game Over")