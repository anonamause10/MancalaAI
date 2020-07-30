import numpy as np
#from matplotlib import pyplot as plt

class DataManager:

    def __init__(self, load = False):
        if(load):
            if(self.load()):
                return
        self.winrate = []
        self.avgscore = []
        self.top4winrate = []
        for i in range(4):
            self.top4winrate.append([])
        self.mutation = []

    def winrateaddpoint(self,val):
        self.winrate.append(val)

    def avgscoreaddpoint(self,val):
        self.avgscore.append(val)

    def top4winrateaddpoints(self,vals):
        i = 0
        for rate in self.top4winrate:
            rate.append(vals[i])
            i+=1

    def mutationaddpoint(self,val):
        self.mutation.append(val)

    def display(self):
        print("does nothing yet lol")

    def load(self):
        try:
            self.winrate = np.load("gamedata/winrate.npy").tolist()
            self.avgscore = np.load("gamedata/avgscore.npy").tolist()
            self.top4winrate = np.load("gamedata/top4winrate.npy").tolist()
            self.mutation = np.load("gamedata/mutation.npy").tolist()
            return True
        except FileNotFoundError:
            print("no data files, creating new ones")
            return False

    def save(self):
        np.save("gamedata/winrate",self.winrate)
        np.save("gamedata/avgscore",self.avgscore)
        np.save("gamedata/top4winrate",self.top4winrate)
        np.save("gamedata/mutation",self.mutation)

data = DataManager(True)
data.save()
        