class worker:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.next=None

head = worker("ami",25)
head.next = None

def traverse(head):
    ptr=head
    while ptr != None:
        print("The employee name is {} and the age is {}.".format(head.name,head.age))
        ptr=ptr.next
    print("traverse finish")

traverse(head)



