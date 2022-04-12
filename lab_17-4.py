#author DMH 12/4/22

# defining class
class tv_remote:

    # setting default values 
    def __init__(self, channel=0, volume_level=0, on=False):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    
    
    # adding conditions
    def __str__(self):
        if self.on == True:
            return "You are watching channel {0} at {1}% volume.".format(self.channel, self.volume_level)
        else:
            return "The TV is off."


    
    def turn_on(self):
        self.on = True
    

    def turn_off(self):
        self.on = False
    

    def volume_up(self, value):
        self.volume_level += value
    

    def volume_down(self, value):
        self.volume_level -= value
    

    def channel_up(self, value):
        self.channel += value
    

    def channel_down(self, value):
        self.channel -= value
    
my_remote = tv_remote()
my_remote.on = True
my_remote.turn_on()
my_remote.turn_off()
my_remote.volume_up(2)
my_remote.volume_down(1)
my_remote.channel_up(6)
my_remote.channel_down(2)
my_remote.turn_on()
print(my_remote)