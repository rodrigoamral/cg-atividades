import numpy as np

class leitorObj:
    def __init__(self, obj_file):
        self.obj_file = obj_file
        self.vertices = None

    def load_model(self):
        vertices = []
        with open(self.obj_file, 'r') as file:
            for line in file:
                tokens = line.strip().split()
                if len(tokens) > 0:
                    if tokens[0] == 'v':
                        vertex = list(map(float, tokens[1:]))
                        vertices.append(vertex)

        self.vertices = np.array(vertices)

    def get_vertices(self):
        if self.vertices is None:
            self.load_model()
        return self.vertices
    
    def get_faces(self):
        if self.vertices is None:
            self.load_model()
        return self.faces