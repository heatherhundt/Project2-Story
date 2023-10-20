#intro to story

print("        Tales of the Kingdom of UMBC   ")
print("            a work of fiction")

print("")
print(" You are a knight in the year 650 BC. You are trying to become the most famous knight of them all.")
print("")
print(" You decide to go on an adventure to the castle of UMBC to earn your glory. ")

#choose who to help multiple choice

print("  As you approach the castle grounds you encounter three different people asking for help. You can talk to: ")
print("")
print("     A. The local blacksmith, who needs a rare sword.")
print("     B. The towns teacher, who has a question.")
print("     C. The king, who needs a brave warrior.")
print("")


#ask for input
whoAssist = input(" Which one do you choose to assist? Please select A, B, or C:")
print("")
print(f"You chose: {whoAssist}")

#If user chose A then go to blacksmith
if(whoAssist == "a" or whoAssist == "A"):
    print(" Now, you will meet with the town blacksmith, looking for a legendary beskar sword.")
    print("Legend has it that the sword is frozen in the ice waiting to be found.")
    print("")
  #blacksmith search 
    print("Where do you go in search of the sword?")
  
    print("")
    print("     A. Look for the sword in the Desert.")
    print("     B. Look for the sword in the forest.")
    print("     C. Look for the sword in the Arctic.")
    sword = input(" Which one do you choose to search? Please select A, B, or C:")

  #blacksmith search and not find sword -END
    if(sword == "a" or sword == "A" or sword == "b" or sword == "B"):
        print("")
        #if user chose A or B then go to Desert or forest
        print("Oh no! You will spend the rest of your days, to no avail, in search of the legendary beskar sword. As you whisper your last parched words - I should have yielded the wise advice of the blacksmith and gone somewhere cold.")
        print("")
      
        print("       THE END")
      
      #if user chose C then go to Arctic
    elif(sword == "c" or sword == "C"):
        print("") 
        
        print("You chose wisely")
        print("")
        print("  After searching day and night across the icy land, you've finally found it.")
        print(" The legendary swod of Python! The blacksmith is overjoyed and rewards you with a suit of armor made from beskar. You're a hero!")
        print("")
      
        print("       THE END")
elif(whoAssist == "b" or whoAssist == "B"):
  #if user chose B then go to teacher
  print("")
  #teacher asks question
  print(" You selected the town teacher. You meet with her and she is asking you for help. I have to be honest with you, she says. ")
  print("")
  
  print("I am not really qualified to teach and am struggling with this equation. She then gestures to this math equation")
  
  teacherQuestion = input(" Can you find the answer: y = 9 + 3 + 10  : ")
  print("")
  #teacher question correct
  if(teacherQuestion == "22"):
    print("")
    print(" That makes perfect sense! exclaims the teacher. She then rewards you with an honorary degree. You are forever known as the smartest in all the land!")
    print("")
    print("       THE END")  
    #teacher question incorrect
  elif(teacherQuestion != "22"):
    print("You chose poorly")
    print("")
    print(" That doesn't look right. You shall be sent to live with the jesters for the rest of your days.")
    print("")
    print("       THE END")
    
#the king riddle from dragon
elif(whoAssist == "c" or whoAssist == "C"):
  print("")
  print("You chose the king.")
  print("")
  print(" You meet with the king of UMBC. He is in search of a brave and mighty warrior. The king states that he needs someone to conquer a nearby fire breathing dragon and save the kingdom fro its wrath. There is no time, travel east as the sun rises, and be ready for battle!")

  print("")
  #king riddle from dragon
  print(" Ready for battle you trave east. But in a twist of fate as you encounter the dragon he has other plans. He asks you to solve a riddle in exchange for the safety of the kingdom.")
  print("")
  print("What two numbers, when added together, equal ten?")

  print("")
  print("You ponder for a moment. Realizing there are multiple answers to this question. After thinking for a moment you answer with two numbers.")
  print("")
  firstNumber = input("What is the first number? ")
  firstNumber = int(firstNumber)
  secondNumber  = input("What is the second number? ")
  secondNumber = int(secondNumber)
  result = firstNumber + secondNumber
  
  print("")
  print("")
  
  #dragon riddle correct
  if(result == "10"):
      print(f"Ah yes, {firstNumber} and {secondNumber} add up to ten. Well done! As your answer is correct the dragon agrees to keep his promise and let the kingdom of UMBC remain safr from his wrath.")
      print("")
      print("         THE END")

  #dragon riddle incorrect
  elif(result != "10"):
       print("No, those numbers don't add up to 10. The fire breathing dragon will now burn down the kingdom of UMBC and you will forever be exiled to the arctic by the king!")
       print("")
       print("       THE END")

  
  
    
  




