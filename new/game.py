import random
from newmodelvoice import sayinshit
numbers=[1,2,3]
random_ch=random.choice(numbers)
computer={
    1:"Stone",
    2:"Paper",
    3:"Scissor"
}
you={
    1:"Stone",
    2:"Paper",
    3:"Scissor"
}
print("1:Stone, 2:Paper, 3:Scissor")
def mainpart():
    sayinshit("Enter your choice : ")
    n=int(input(("Enter your choice (1,2 & 3): "))) 
    if(n==1 or n==2 or n==3):
        print(sayinshit(f"You selected {you[n]} & computer selected {computer[random_ch]}") or f"You selected {you[n]} & computer selected {computer[random_ch]}")
        if(n==random_ch): 
            print(sayinshit("It's a draw") or ("It's a draw"))
        elif(n==2 and random_ch==1): 
            print(sayinshit("You win! ") or ("You win! "))
        elif(random_ch==2 and n==1): 
            print(sayinshit("You lose!") or ("You lose!"))
        elif(n==3 and random_ch==2): 
            print(sayinshit("You win! ") or ("You win! "))
        elif(random_ch==2 and n==3): 
            print(sayinshit("You lose!") or ("You lose!"))
        elif(n==1 and random_ch==3): 
            print(sayinshit("You win! ") or ("You win! "))
        elif(n==3 and random_ch==1): 
            print(sayinshit("You lose!") or ("You lose!"))
        else:
            print(sayinshit("Invalid input !!") or ("Invalid input !!"))
    else:
        print(sayinshit("Error")or ("Error"))
mainpart()
while True:
    a=input(sayinshit("Do you want to continue:") or ("Do you want to continue(Y/y/N/n) :"))
    if a.lower()=="y":
        mainpart()
    else:
        print(sayinshit("Thank you for using my program") or ("Thank you for using my program !!"))
        break