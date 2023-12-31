class Car:
    def __init__(self, color):
        self.color=color
        self.next=None

def traverse(head):
    ptr=head
    while True:
        print("The color of the car is {}".format(ptr.color))
        if ptr.next == head:
            break
        ptr=ptr.next
    print("traverse finish")



head = Car("red")
bl=Car("blue")
new = Car("black")
head.next= bl
bl.next=head
new.next=head
ptr=head
while ptr.next != head:
    ptr = ptr.next
ptr.next= new
head = new
traverse(head)