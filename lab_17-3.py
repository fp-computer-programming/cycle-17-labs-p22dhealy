#author DMH 12/4/22

class tv_remote:

    # setting default values 
    def __init__(self, channel=0, volume_level=0, on=False):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    

    
    def __str__(self):
        if self.on == True:
            return "You are watching channel {0} at {1}% volume.".format(self.channel, self.volume_level)
        else:
            return "The TV is off."


# calling the functions
my_remote = tv_remote()
my_remote.on = True
print(my_remote)