import numpy as np


    
class map():
    def __init__(self):
        self.Map = [[1,1,1,1,1,1],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1],]
        
        self.F = np.empty(np.shape(self.Map), dtype = float)
        self.F.fill(np.inf)
        self.openF = np.empty(np.shape(self.Map), dtype = float)
        self.openF.fill(np.inf)
        self.open = self.Map.copy()
        self.H = np.zeros_like(self.open,dtype = float)
        
        self.G = np.empty(np.shape(self.Map), dtype = float)
        self.G.fill(np.inf)
        
        self.parrents = np.empty((np.shape(self.open)[0],np.shape(self.open)[1],2), dtype = int)
        self.parrents.fill(0)
        
        self.start = np.array((0,0))
        self.end = np.array((3,5))
        
        self.update(self.start,self.start)
        
        self.shape = np.shape(self.F)
        self.path = []
        
        
    def update(self,pos2,pos1):
        H = self.H[pos2[0]][pos2[1]] + np.linalg.norm(np.array(pos2)-np.array(pos1)) #self.parrents[pos1[0]][pos1[1]]
        G = np.linalg.norm(self.end-pos1)
        
        # F = self.H[pos1[0]][pos1[1]] + np.linalg.norm(self.end-pos1)
        F = H + G
        if F < self.F[pos1[0]][pos1[1]]:
            
            self.G[pos1[0]][pos1[1]] = G
            self.H[pos1[0]][pos1[1]] = H
            self.F[pos1[0]][pos1[1]] = F
            self.parrents[pos1[0],pos1[1]] = pos2
            if self.open[pos1[0]][pos1[1]] == 1:
                self.openF[pos1[0]][pos1[1]] = F
    
    def make_path(self):
        min_pos = (np.unravel_index(np.argmin(map.G),map.shape))
        # min_pos = map.end
        self.path.append(min_pos)
        current = self.parrents[min_pos[0]][min_pos[1]]
        while any(current != self.start):
            self.path.append(current)
            current = self.parrents[current[0]][current[1]]
        self.path.append(self.start)
        self.path = list(reversed(self.path))
        
        path_on_map = np.zeros_like(self.Map)
        for step in self.path:
            path_on_map[step[0]][step[1]] = 1
        return path_on_map
    

def get_neibors(pos,map):
    neibours = []
    indexes = ([(-1,-1),(0,-1),(1,-1),(1,0),(-1,0),(-1,1),(0,1),(1,1)])
    for index in indexes:
        neibour = (pos[0]+index[0],pos[1]+index[1])
        if neibour[0] >= 0 and neibour[1] >= 0 and neibour[0] < map.shape[0] and neibour[1] < map.shape[1] and map.open[neibour[0]][neibour[1]] == 1: 
            neibours.append(neibour)
    return neibours
    





map = map()


# Цикл в котором будет выбираться точка с наименьшим F в данный момент и которая не проверялась ранее,
# Для соседей точки вычисляется H,F 
# Если из нее до любого из ее соседей добраться быстрее (меньше F), то для соседа обновляется H, F, parrent

while map.F[map.end[0]][map.end[1]] == np.inf:
    min_pos = (np.unravel_index(np.argmin(map.openF),map.shape))
    neibours = get_neibors(min_pos,map)
    for neibour in neibours:
        map.update(min_pos, neibour)
        
    map.open[min_pos[0]][min_pos[1]] = 0
    map.openF[min_pos[0]][min_pos[1]] = np.inf
    
    if np.min(map.openF) == np.inf:
        break

# 

path_on_map = map.make_path()


print(map.path)
print(path_on_map)

