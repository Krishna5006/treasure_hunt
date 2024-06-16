print(r'''
||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||
||\\$//        ~         '------========--------'                \\$//||
||<< /        /$\              // ____ \\                         \ >>||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
||<<|        \\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
''')

print("Welcome To The Treasure Island")
print("Your mission is to find the treasure containing Lacs of hundred-dollar notes")
start=input("Are you ready to start the journey? Y or N ")
if (start == "Y"):
  print("We reached at a cross road.")
  cross_road=input("Where you want to go? Type 'left' or 'right'")
  if (cross_road == "left"):
    print("You reached a lake.")
    shore=input("Will you wait for boat or swim to the castle in the middle of the lake ?")
    if (shore == "boat"):
      print("You reached the castle safetly.")
      enter_castle=input("If you want to return back safetly from the castle leave as soon as you arriver here. For entering type Y and N for exit")
      if (enter_castle == "Y"):
        print("There are three rooms in front of you named fire animal and tresure")
        door_choice=input("Choose a door you want to enter named as A B C respectively as the above case scenario")
        if (door_choice == "A"):
          print("You won the treasure")
        elif (door_choice == "B"):
          print("As soon as you entered the room a wild animal from the corner came and attacked you ./n GAME OVER")
        else:
          print("You fell into a trap and got eaten by small microbes")
      else:
        print("You came this far but got nothing . Well done you saved your life")
    else:
      print("Lake beast devoured you ./n GAME OVER")
  else:
    print("You tried your best but was never able to reach the treasure")
else:
  print("You never started so you never got the treasure")


  
