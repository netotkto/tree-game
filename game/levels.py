from modules import Grow_Up


def first_level(pop_axes, bags, drops, woods, axes, flowers):

    if len(bags) < 1:
        if 30 - pop_axes == 0:
            bags.append(Grow_Up(420, 350, 70, 80))
            pop_axes = 0

    if pop_axes > 30:
        pop_axes = 0

    for drop in drops:
        if drop.x <= 320:
            if 440 > drop.y > -1001:
                drop.y += drop.speed
            else:
                drops.pop(drops.index(drop))

        elif drop.x > 350:

            if 350 > drop.y > -1001:
                drop.y += drop.speed
            else:
                drops.pop(drops.index(drop))

    for wood in woods:
        if wood.x <= 320:
            if 450 > wood.y > -61:
                wood.y += wood.speed
            else:
                woods.pop(woods.index(wood))

        elif wood.x > 320:
            if 380 > wood.y > -61:
                wood.y += wood.speed
            else:
                woods.pop(woods.index(wood))

    for flower in flowers:
        if flower.x <= 320:
            if 450 > flower.y > -61:
                flower.y += flower.speed
            else:
                flowers.pop(flowers.index(flower))

        elif flower.x > 320:
            if 380 > flower.y > -61:
                flower.y += flower.speed
            else:
                flowers.pop(flowers.index(flower))

    for axe in axes:
        if axe.x <= 320:
            if 420 > axe.y > -151:
                axe.y += axe.speed
            else:
                axes.pop(axes.index(axe))
                pop_axes += 1

        elif axe.x > 320:
            if 340 > axe.y > -151:
                axe.y += axe.speed
            else:
                axes.pop(axes.index(axe))
                pop_axes += 1


def second_level(pop_axes, bags, drops, woods, axes, flowers):
    
    if len(bags) > 0:
        if bags[0].x == 420 and bags[0].y == 350:
            bags.clear()

    if 1 > len(bags):
        if 30 - pop_axes == 0:
            bags.append(Grow_Up(20, 350, 70, 80))
            pop_axes = 0

    if pop_axes > 30:
        pop_axes = 0

    for drop in drops:
        if drop.x >= 150:
            if 440 > drop.y > -1001:
                drop.y += drop.speed
            else:
                drops.pop(drops.index(drop))

        elif drop.x < 150:

            if 350 > drop.y > -1001:
                drop.y += drop.speed
            else:
                drops.pop(drops.index(drop))

    for wood in woods:
        if wood.x >= 150:
            if 450 > wood.y > -61:
                wood.y += wood.speed
            else:
                woods.pop(woods.index(wood))

        elif wood.x < 150:
            if 380 > wood.y > -61:
                wood.y += wood.speed
            else:
                woods.pop(woods.index(wood))

    for flower in flowers:
        if flower.x >= 150:
            if 450 > flower.y > -61:
                flower.y += flower.speed
            else:
                flowers.pop(flowers.index(flower))

        elif flower.x < 150:
            if 380 > flower.y > -61:
                flower.y += flower.speed
            else:
                flowers.pop(flowers.index(flower))

    for axe in axes:
        if axe.x >= 150:
            if 420 > axe.y > -151:
                axe.y += axe.speed
            else:
                axes.pop(axes.index(axe))
                pop_axes += 1

        elif axe.x < 150:
            if 340 > axe.y > -151:
                axe.y += axe.speed
            else:
                axes.pop(axes.index(axe))
                pop_axes += 1


def third_level(pop_axes, bags, drops, woods, axes, flowers):
    
    if len(bags) > 0:
        if bags[0].x == 20 and bags[0].y == 350:
            bags.clear()

    if len(bags) < 1:
        if 30 - pop_axes == 0:
            bags.append(Grow_Up(425, 420, 70, 80))
            pop_axes = 0

    if pop_axes > 30:
        pop_axes = 0

    for drop in drops:
        if 440 > drop.y > -1001:
            drop.y += drop.speed
        else:
            drops.pop(drops.index(drop))

    for wood in woods:
        if 450 > wood.y > -61:
            wood.y += wood.speed
        else:
            woods.pop(woods.index(wood))

    for flower in flowers:
        if 450 > flower.y > -61:
            flower.y += flower.speed
        else:
            flowers.pop(flowers.index(flower))

    for axe in axes:
        if 420 > axe.y > -151:
            axe.y += axe.speed
        else:
            axes.pop(axes.index(axe))
            pop_axes += 1
            
            
def fourth_level(pop_axes, bags, drops, woods, axes, flowers):
    
    if len(bags) > 0:
        if bags[0].x == 425 and bags[0].y == 420:
            bags.clear()

    if len(bags) < 1:
        if 30 - pop_axes == 0:
            bags.append(Grow_Up(420, 350, 70, 80))
            pop_axes = 0

    if pop_axes > 30:
        pop_axes = 0

    for drop in drops:
        if drop.x <= 320:
            if 440 > drop.y > -1001:
                drop.y += drop.speed
            else:
                drops.pop(drops.index(drop))

        elif drop.x > 350:

            if 350 > drop.y > -1001:
                drop.y += drop.speed
            else:
                drops.pop(drops.index(drop))

    for wood in woods:
        if wood.x <= 320:
            if 450 > wood.y > -61:
                wood.y += wood.speed
            else:
                woods.pop(woods.index(wood))

        elif wood.x > 320:
            if 380 > wood.y > -61:
                wood.y += wood.speed
            else:
                woods.pop(woods.index(wood))

    for flower in flowers:
        if flower.x <= 320:
            if 450 > flower.y > -61:
                flower.y += flower.speed
            else:
                flowers.pop(flowers.index(flower))

        elif flower.x > 320:
            if 380 > flower.y > -61:
                flower.y += flower.speed
            else:
                flowers.pop(flowers.index(flower))

    for axe in axes:
        if axe.x <= 320:
            if 420 > axe.y > -151:
                axe.y += axe.speed
            else:
                axes.pop(axes.index(axe))
                pop_axes += 1

        elif axe.x > 320:
            if 340 > axe.y > -151:
                axe.y += axe.speed
            else:
                axes.pop(axes.index(axe))
                pop_axes += 1
                
                
def fifth_level(pop_axes, bags, drops, woods, axes, flowers):
    
    if len(bags) > 0:
        if bags[0].x == 420 and bags[0].y == 350:
            bags.clear()

    if len(bags) < 1:
        if 30 - pop_axes == 0:
            bags.append(Grow_Up(20, 350, 70, 80))
            pop_axes = 0

    if pop_axes > 30:
        pop_axes = 0

    for drop in drops:
        if drop.x >= 150:
            if 440 > drop.y > -1001:
                drop.y += drop.speed
            else:
                drops.pop(drops.index(drop))

        elif drop.x < 150:

            if 350 > drop.y > -1001:
                drop.y += drop.speed
            else:
                drops.pop(drops.index(drop))

    for wood in woods:
        if wood.x >= 150:
            if 450 > wood.y > -61:
                wood.y += wood.speed
            else:
                woods.pop(woods.index(wood))

        elif wood.x < 150:
            if 380 > wood.y > -61:
                wood.y += wood.speed
            else:
                woods.pop(woods.index(wood))

    for flower in flowers:
        if flower.x >= 150:
            if 450 > flower.y > -61:
                flower.y += flower.speed
            else:
                flowers.pop(flowers.index(flower))

        elif flower.x < 150:
            if 380 > flower.y > -61:
                flower.y += flower.speed
            else:
                flowers.pop(flowers.index(flower))

    for axe in axes:
        if axe.x >= 150:
            if 420 > axe.y > -151:
                axe.y += axe.speed
            else:
                axes.pop(axes.index(axe))
                pop_axes += 1

        elif axe.x < 150:
            if 340 > axe.y > -151:
                axe.y += axe.speed
            else:
                axes.pop(axes.index(axe))
                pop_axes += 1


