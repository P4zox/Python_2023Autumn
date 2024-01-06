class Employee:
    def __init__(self, name, pt):
        self.name=name
        self.purchaseTime=pt
        self.next=None



def traverse(head):
    ptr=head
    while ptr != None:
        print("The name of the worker is {}, and the purchase time is {}".format(ptr.name, ptr.purchaseTime))
        if ptr.next == head:
            break
        ptr=ptr.next
    print("traverse finish")

amy = Employee("Amy",8)
john = Employee("John",10)
leo= Employee("Leo",17)
brian = Employee("Brian",1)
brian.next= leo
leo.next=john
john.next=amy
amy.next= brian
traverse(brian)