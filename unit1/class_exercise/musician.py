class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
            
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end="  ")
        print()

class Bassist(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])
        
    def tune(self):
        print("Be with you in a moment")
        print("Twoning", "sproing", "sprang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bum", "Ding", "Dam"])

    def count(self):
        print("One, Two, Three, Four!")
    
    def combust(self): 
        print("Kaboom! Oh My goodness! The drummer blew up!")


class Band(object):
    def __init__(self):
        self.members = {}
    
    def hire(self, role, musician):
        self.members[role] = musician
    
    def fire(self, role):
        if role in self.members:
            del self.members[role]
        
    def gig(self, length):
        Drummer.count(self)
        for role, musician in self.members.items():
            musician.solo(length)
            
            
            
if __name__ == '__main__':    
        
    derek = Bassist()
    nigel = Guitarist()
    david = Drummer()
    the_band = Band()
    the_band.hire('Drummer', david)
    print("We hired a drummer, David!")
    the_band.gig(6)
    the_band.hire('Guitarist', nigel)
    print("We hired a Guitar, Nigel!")
    the_band.hire('Bassist', derek)
    print("We hired a Bassist, Derek!")
    the_band.gig(3)
    the_band.fire('Bassist')
    print("We fired Derek, we need better bass")
    the_band.gig(1)
