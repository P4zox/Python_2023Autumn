class Car:
    def __init__(self, color):
        self.color=color
        self.next=None



def traverse(head):
    ptr=head
    while ptr != None:
        print("The color of the car is {}".format(ptr.color))
        ptr=ptr.next
    print("traverse finish")

red = Car("red")
blue = Car("blue")
black= Car("black")
pink=Car("pink")
red.next= None
blue.next= red #blue point to red
head= blue # 1 node = blue
head.next.next=black
black.next=None
pink.next=black
red.next=pink
red.next=black
top=head
head=head.next
red.next = None
traverse(head)