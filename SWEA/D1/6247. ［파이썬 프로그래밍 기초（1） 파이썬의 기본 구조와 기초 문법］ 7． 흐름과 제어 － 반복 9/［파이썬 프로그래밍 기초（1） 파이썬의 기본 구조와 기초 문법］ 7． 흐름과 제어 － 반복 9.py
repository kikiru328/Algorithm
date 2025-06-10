stars = 7

while stars >= 1:
    space = (7 - stars) // 2
    print(' ' * space + '*' * stars)
    stars -= 2