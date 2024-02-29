h=int(input("enter the height of the persn for a ride in cm "))
a=int(input("enter the age of the persn for a ride "))
bill=0
if h>=120:
    if a<12:
        bill=5
        print("THE BILL IS 5$")
    elif a<18:
        bill=7
        print("THE BILL IS 7$")
    elif a>=18:
        bill=12
        print("THE BILL IS 12$")

    ph=input("want even photo of ur ride ?? y/n ")
    if ph=='y':
        bill+=3 
        print(f"SO TOTAL BILL OF UR RIDE IS {bill} $")
    else:
        print(f"SO TOTAL BILL OF UR RIDE IS {bill} $")

else:
    print("grow heigher and come next time!!!")