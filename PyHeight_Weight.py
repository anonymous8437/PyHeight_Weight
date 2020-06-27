weight = int(input("Your Weight <Kg>: "))
height = int(input("Your Height <Cm>: "))
height = height-100
height = height-2
print('Maximum balanced weight: ',height)
weight = weight-height
print(f"Your Extra/Shortage Weight is: {weight}")
