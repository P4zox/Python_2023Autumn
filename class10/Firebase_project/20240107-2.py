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



red = Car("red")
blue=Car("blue")
black = Car("black")
pink = Car("pink")
black.next=red
red.next=blue
blue.next=black
red.next=pink
pink.next=blue
black=red
blue.next=red
red.next=blue
traverse(red)