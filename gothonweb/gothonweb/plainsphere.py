class Room(object):

    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.paths={}

    def go(self,direction):
        return self.paths.get(direction,None)

    def add_paths(self,paths):
        self.paths.update(paths)


central_corridor=Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship
destroyed your entire crew. You are the last surviving
member and your last mission is to get the neutron destr
bomb from the Weapons Armory, put it in the bridge, and
blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons
Armory when a Gothon jumps out, red scaly skin, dark gri
teeth, and evil clown costume flowing around his hate
filled body. He's blocking the door to the Armory and
about to pull a weapon to blast you.
""")

laser_weapon_armory=Room(" Laser Weapon Armory","""
You do a dive roll into the Weapon Armory, crouch and s
the room for more Gothons that might be hiding. It's de
quiet, too quiet. You stand up and run to the far side
the room and find the neutron bomb in its container.
There's a keypad lock on the box and you need the code
get the bomb out. If you get the code wrong 10 times th
the lock closes forever and you can't get the bomb. The
code is 3 digits.
""")

the_bridge=Room("The Bridge","""
You burst onto the Bridge with the netron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship. Each of them has an even ugli
clown costume than the last. They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
 """)

escape_pod=Room("Escape Pod","""
You rush through the ship desperately trying to make it
the escape pod before the whole ship explodes. It seems
like hardly any Gothons are on the ship, so your run is
clear of interference. You get to the chamber with the
escape pods, and now need to pick one to take. Some of
them could be damaged but you don't have time to look.
There's 5 pods, which one do you take?
""")

the_end_winner=Room("The End","""
    You jump into pod 2 and hit the eject button.114 The pod easily slides out into space heading to the
    planet below. As it flies to the planet, you look
    back and see your ship implode then explode like a
    bright star, taking out the Gothon ship at the same
    time. You won!
""")

the_end_loser=Room("The End","""
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body i
jam jelly.
""")

escape_pod.add_paths({
    '2':the_end_winner,
    '*':the_end_loser
})

# the_end_loser.add_paths{
#     '*':generic_death
# }
generic_death=Room("death","You died.")

the_bridge.add_paths({
    'throw the bomb':generic_death,
    'slowly place the bomb':escape_pod
})

laser_weapon_armory.add_paths({
    '132':the_bridge,
    '*':generic_death
})

central_corridor.add_paths({
    'shoot!':generic_death,
    'dodge!':generic_death,
    'tell a joke':laser_weapon_armory
})

START='central_corridor'

def load_room(name):
    """
    There is a potential security problem here,
    who gets to set name?can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    same possible security problem.Can you trust room?
    what's a better solution than this globals lookup?
    """
    for key,value in globals().items():
        if value == room:
            return key
