# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:50:23 2021

@author: Shalin
"""

class Tensor():
    def __init__(self, data, shape):
        self.data = data
        self.shape = shape
        
    def reshape(self):  ## 'reshape' is an example. feel free to name it whatever you want.
        ## boundary conditions
        if not self.shape:
            print([])
            return
        ## calculate number of elements in output
        no_of_elements = 1
        for i in self.shape:
            no_of_elements *= i
            
        ## adjust the length of data
        len_data = len(self.data)
        if no_of_elements >= len_data:
            self.data.extend([0]*(no_of_elements-len_data))
        else:
            self.data = self.data[:no_of_elements]
        
        count = 0
        for i in self.shape[::-1]:
            if count==len(self.shape) - 1:
                break
            self.data = [self.data[j:j + i] for j in range(0, len(self.data), i)]
            count += 1
            # print(self.data)
        print(self.data)

data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
shape0 = [2, 3, 2]
tensor0 = Tensor(data0, shape0)
tensor0.reshape()
# output: [[[0, 1], [2, 3], [4, 5]], [[0.1, 0.2], [-3, 0], [0, 0]]]

data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
shape1 = [5, 2]
tensor1 = Tensor(data1, shape1)
tensor1.reshape()
# output: [[0, 1], [2, 3], [4, 5], [0.1, 0.2], [-3, -2]]
