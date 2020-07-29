import numpy as np

class Brain:
    
    def __init__(self,hiddenlayersizes,numinputs, numoutputs):
        self.weights = []
        self.biases = []
        self.inputshape = numinputs
        self.outputshape = numoutputs
        r = numinputs
        for i in range(len(hiddenlayersizes)+1):
            if(i<len(hiddenlayersizes)):
                c = hiddenlayersizes[i]
            else:
                c = numoutputs
            weightmatrix = np.ones((r,c))
            biasvector = np.zeros((c))
            self.weights.append(weightmatrix)
            self.biases.append(biasvector)
            r = c
        print(self.weights[0])
        print(self.biases[0])

    def evaluate(self,input):
        output = np.copy(input)

        if(input.shape[0]!=self.inputshape):
            return np.zeros(input.shape)
        
        for i in range(len(self.weights)):
            output = np.matmul(self.weights[i],output)
            output = np.add(output,self.biases[i])
        
        return output

    def actionindex(self,outputvec):
        return np.argmax(outputvec)[0]

    def mutate(self,weightfactor,biasfactor):
        
        for i in range(len(self.weights)):
            w =  self.weights[i]
            self.weights[i] = np.add(w,np.random.rand(w.shape[0],w.shape[1])*weightfactor)
            b = self.biases[i]
            self.biases[i] = np.add(b,np.random.rand(b.shape[0])*biasfactor) 


            
        
brain = Brain([10,10,10],14,6)
