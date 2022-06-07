import numpy as np


    
class map():
    def __init__(self):
        self.Map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

        self.open = self.Map
        self.F = np.empty(np.shape(self.open), dtype = float)
        self.F.fill(np.inf)
        self.H = np.zeros_like(self.open)
        self.parrents = np.empty((np.shape(self.open)[0],np.shape(self.open)[1],2), dtype = int)
        self.parrents.fill(0)
        
        self.start = np.array((0,0))
        self.end = np.array((13,3))
        
        self.update(self.start,self.start)
        
    def update(self,pos2,pos1):
        H = self.H[pos2[0]][pos2[1]] + np.linalg.norm(self.parrents[pos1[0]][pos1[1]]-pos1) 
        F = self.H[pos1[0]][pos1[1]] + np.linalg.norm(self.end-pos1)
        if F < self.F[pos1[0]][pos1[1]]:
            self.H[pos1[0]][pos1[1]] = H
            self.F[pos1[0]][pos1[1]] = F
            self.parrents[pos1[0],pos1[1]] = pos2
        
map = map()

# Цикл в котором будет выбираться точка с наименьшим F в данный момент и которая не проверялась ранее,
# Для соседей точки вычисляется H,F 
# Если из нее до любого из ее соседей добраться быстрее (меньше H), то для соседа обновляется H, F, parrent

# # min_g_distance = np.inf
# while min_g_distance != 0:

# 