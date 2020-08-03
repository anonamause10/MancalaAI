import numpy as np
#from matplotlib import pyplot as plt

class DataManager:

    def __init__(self, load = False):
        if(load):
            if(self.load()):
                return
        self.winrate = []
        self.avgscore = []
        self.top4score = []
        for i in range(4):
            self.top4score.append([])
        self.fitness = []

    def winrateaddpoint(self,val):
        self.winrate.append(val)

    def avgscoreaddpoint(self,val):
        self.avgscore.append(val)

    def top4scoreaddpoints(self,vals):
        i = 0
        for rate in self.top4score:
            rate.append(vals[i])
            i+=1

    def fitnessaddpoint(self,val):
        self.fitness.append(val)

    def display(self):
        print("does nothing yet lol")

    def load(self):
        try:
            self.winrate = np.load("gamedata/winrate.npy").tolist()
            self.avgscore = np.load("gamedata/avgscore.npy").tolist()
            self.top4score = np.load("gamedata/top4score.npy").tolist()
            self.fitness = np.load("gamedata/fitness.npy").tolist()
            return True
        except FileNotFoundError:
            print("no data files, creating new ones")
            return False

    def save(self):
        np.save("gamedata/winrate",self.winrate)
        np.save("gamedata/avgscore",self.avgscore)
        np.save("gamedata/top4score",self.top4score)
        np.save("gamedata/fitness",self.fitness)


        