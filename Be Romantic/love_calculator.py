import random

your_name = input("Enter your name : ")

crush_name = input("Enter your partner name : ")

percentage = random.randint(1, 100)

print(f"{your_name} and {crush_name} yours love percentage :{percentage}")


if(percentage >= 80):
    print("Your partner is your best friend and you can�t take your eyes off each other."
          "Celebrate this awesomeness with a romantic dinner date.")
elif (percentage >=60):
    print("Both of you are really happy."
          "Dr.Love says taking a short vacation would give you both more reasons to rejoice!")
elif(percentage>=40):
    print("Let fate play cupid! Dr.Love feels your partner may be feeling a bit neglected for a while." 
           "Give him/her the attention that they seek, and enjoy this wonderful time togethe")
else:
    print("Beta Tumse na ho paega")
