from newmodelvoice import sayinshit
from datetime import date

todays = date.today()
datetoday=str(todays)
def main():
    print("""Ask A Question ? : 
          1 Hello
          2 What is the date ?
          3 What's your name ?
          """)
    n=int(input("Your Choice ?:"))
    if(n==1):
        print(sayinshit("Hey how you doing !!") or "Hey how you doing !!")
    elif(n==2):
        print(todays or sayinshit(datetoday))
    else:
        print(sayinshit("I am an A I developed by Robin") or "I am an AI developed by Robin")
main()        
while True:
    a=input(sayinshit("Do you want to continue:") or ("Do you want to continue(Y/y/N/n) :"))
    if a.lower()=="y":
        main()
    else:
        print(sayinshit("Thank you for using my program") or ("Thank you for using my program !!"))
        break