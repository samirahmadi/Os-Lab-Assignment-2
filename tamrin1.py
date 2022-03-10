from random import choice
words_bank=["book","apple","sadjad","mashhad","blue","tree","linux","iran","python","comuter"]
word=choice(words_bank)
user_true_chars=[]
wrong=[]
joon=5

while joon>0:
    line=""
    for i in word:
        if i in user_true_chars:
            line=line+i
        else:
            line=line+"_"
    if line==word:
     break  
    print(line,"\nplease enter a character:\n")
    user_char=input()
    if len(user_char)==1:
        if user_char in user_true_chars:
         print("please enter a character",user_char)
        elif user_char in word:
         print("✅")
         user_true_chars.append(user_char)
        else:
         print("❌")
         joon=joon-1
    else:
        print("\nmesle adam vared kon:/")    
    print()
if  joon:
    print(word)
    print("\nباریکلا")
else:
    print("Game over")










