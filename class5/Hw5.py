class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.next=None



def traverse(head):
    ptr=head
    while ptr != None:
        print("The name of the worker is {}, and the age is {}".format(ptr.name, ptr.age))
        ptr=ptr.next
    print("traverse finish")

amy = Employee("Amy",25)
eddy = Employee("Eddy",43)
esme= Employee("Esme",32)
amy.next= eddy
amy.next.next=esme
esme.next=None
traverse(amy)