import numpy as np
import os

class Brain:
    
    def __init__(self,hiddenlayersizes=[10,10],numinputs=14, numoutputs=6, load = False):
        if(load):
            if(self.load()):
                return
        self.weights = []
        self.biases = []
        self.inputshape = numinputs
        self.outputshape = numoutputs
        self.currepoch = 0
        r = numinputs
        for i in range(len(hiddenlayersizes)+1):
            if(i<len(hiddenlayersizes)):
                c = hiddenlayersizes[i]
            else:
                c = numoutputs
            weightmatrix = np.ones((c,r))
            biasvector = np.zeros((c))
            self.weights.append(weightmatrix)
            self.biases.append(biasvector)
            r = c

    def evaluate(self,input):
        output = np.copy(input)

        if(input.shape[0]!=self.inputshape):
            return np.zeros(input.shape)
        
        for i in range(len(self.weights)):
            output = np.matmul(self.weights[i],output)
            output = np.add(output,self.biases[i])
        
        return output

    def actionindex(self,outputvec,legals = [True]*6):
        outputvec = [outputvec[i] if legals[i] else -100000000 for i in range(len(outputvec))]
        return np.argmax(outputvec)

    def mutate(self,weightfactor = 1,biasfactor = 1):
        
        for i in range(len(self.weights)):
            w =  self.weights[i]
            self.weights[i] = np.add(w,(np.random.rand(w.shape[0],w.shape[1])-0.5)*2*weightfactor)
            b = self.biases[i]
            self.biases[i] = np.add(b,(np.random.rand(b.shape[0])-0.5)*2*biasfactor) 
        self.currepoch += 1

    def setlayers(self, newbrain):
        self.weights = np.copy(newbrain.weights)
        self.biases = np.copy(newbrain.biases)
        self.inputshape = newbrain.inputshape
        self.outputshape = newbrain.outputshape
        self.currepoch = newbrain.currepoch

    def printweights(self):
        print("Weights:")
        for i in range(len(self.weights)):
            print("Layer " + str(i) + " weights:")
            print(self.weights[i])

    def printbiases(self):
        print("Biases:")
        for i in range(len(self.biases)):
            print("Layer " + str(i) + " biases:")
            print(self.biases[i])

    def save(self):
        for i in range(len(self.weights)):
            np.save("weights/weights" + str(i),self.weights[i])
            np.save("biases/biases" + str(i),self.biases[i])
        f = open("currepoch.txt","w")
        f.write(str(self.currepoch))
        f.close()
        

    def load(self):
        self.weights = []
        self.biases = []
        if(len(os.listdir("weights"))<1 or len(os.listdir("biases"))<1):
            return False
        for f in os.listdir("weights"):
            self.weights.append(np.load("weights/"+f))
        for f in os.listdir("biases"):
            self.biases.append(np.load("biases/"+f))
        self.inputshape = self.weights[0].shape[1]
        self.outputshape = self.biases[-1].shape[0]
        epoch = open("currepoch.txt","r")
        self.currepoch = int(epoch.read())
        epoch.close()
        return True


            

if __name__ == "__main__":      
    brain = Brain([10,10,10],14,6,True)
    brain.mutate()
    brain.save()
    #print(brain.actionindex(brain.evaluate(np.array([4,4,4,4,4,4,0,4,4,4,4,4,4,0]))))
