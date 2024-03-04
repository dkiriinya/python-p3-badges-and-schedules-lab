def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    l = []
    for name in names:
        l.append(f'Hello, my name is {name}.') 
    return l

def assign_rooms(names):
    l = []
    room = 1
    if room <= 8:
        for name in names:
            l.append(f"Hello, {name}! You'll be assigned to room {room}!")
            room += 1
    return l

NAMES = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]
print (assign_rooms(NAMES))
            
            

def printer(names):
    badges = (batch_badge_creator(names))
    for badge in badges:
        print(badge)
   
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print (assignment)
    
printer(NAMES)
