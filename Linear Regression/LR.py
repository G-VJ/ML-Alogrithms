# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 2021

@author: gauravvijayvergiya
"""

import numpy as np



class LR():
    
    def __init__(self, fit_intercept=True):
        self.fit_intercept = True
        

    
    def predict(self, X):
        #print(self.W, self.b)
        y_pred = X.dot(self.m) + self.c
        return y_pred
      
    
    def fit(self, X, Y):
        
        self.X = X
        self.Y = Y
        
        x_mean = np.mean(X)
        y_mean = np.mean(Y)
        
        x_len = len(X)
        
        # calculation numerator and denominator for m and b
        numr = 0 
        den = 0
        
        for i in range(x_len):
            numr += (X[i] - x_mean) * (Y[i] - y_mean)
            den += (X[i]- x_mean) ** 2
        
        # calculate m and b
        self.m = numr/den
        self.c = y_mean - (self.m * x_mean )
        
        return self
        
        
        
        
        
        
        