def singleTon(cls):
    L=[]
    def Inner():
        if (len(L)==0):
            L.append(cls())
        return L[0]
    return Inner
@singleTon
class chandramukhi2:
    def __init__(self):
        self.tickets=390
    def booking(self):
        ntickets=int(input("enter the no.of tickets:"))
        if self.tickets>=ntickets:
            self.tickets-=ntickets
            print("Tickets booked successfully....")
            print("-"*115)
        else:
            print("Tickets not available")
            print("-"*115)
@singleTon
class skanda:
    def __init__(self):
        self.tickets=390
    def booking(self):
        ntickets=int(input("enter the no.of tickets:"))
        if self.tickets>=ntickets:
            self.tickets-=ntickets
            print("Tickets booked successfully....")
            print("-"*115)
        else:
            print("Tickets not available")
            print("-"*115)
singleTon
class jawan:
    def __init__(self):
        self.tickets=390
    def booking(self):
        ntickets=int(input("enter the no.of tickets:"))
        if self.tickets>=ntickets:
            self.tickets-=ntickets
            print("Tickets booked successfully....")
            print("-"*115)
        else:
            print("Tickets not available")
            print("-"*115)

def book_my_show():
    print("1.chandramukhi2\n2.skanda\n3.jawan")
    option=int(input("select option:"))
    if option==1:
        print("movie name is :chandharamukhi2")
        c1=chandramukhi2()
        c1.booking()
    elif option==2:
        print("movie name is :skanda")
        s1=skanda()
        s1.booking()
    elif option==3:
        print("movie name is :jawan")
        j1=jawan()
        j1.booking()
    else:
        print("Invalid option")
while True:
    book_my_show()
