class Car:
    def __init__(self, color):
        self.color=color
        self.next=None

head = Car("red")
head.next= None

def traverse(head):
    ptr=head
    while ptr != None:
        print("The color of the car is {}".format(ptr.color))
        ptr=ptr.next
    print("traverse finish")


newnode = Car("blue")
secnode= Car("black")
newnode.next= head #blue point to red
head= newnode # 1 node = blue
head.next.next=secnode
secnode.next=None
traverse(head)