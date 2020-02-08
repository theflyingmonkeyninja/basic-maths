# -*- coding: utf-8 -*-
"""
Created on Feb  8 13:29:49 2019

@author: dhananjay
 
this module is collection of functions to compute a reimann sum \sum_{i=a}^{b} f_i(x_i)


a = lowerlimit, b = upperlimit, y = function values defined by function on x each y value should corrospond to x value
 
"""

class reimannsum:
    def __init__(self,a,b,N):
        self.a = a;
        self.b = b;
        self.h = (b-a);
        self.N = N;
        
        
    def rect(self,y,x):
        delta = self.h/len(x);
        rsum = delta*sum(y);
        return rsum
    
    def trapz(self,y,x):
        delta=self.h/(2*(self.N-1));
        rsum = y[0]+y[-1];
        i = 1;
        while i < len(x)-1:
            rsum += 2 * y[i]
            i += 1
        rsum = rsum*delta;
        return rsum
    
    def simpsons(self, y,x):
        rsum = 0;
        i = 0
        while i<= len(x)-1:
            if i == 0 or i == len(x)-1:
                rsum+= y[i]
            elif i % 2 != 0:
                rsum+= 4 * y[i] 
            else:
                rsum+= 2 * y[i]
            i+= 1
            
        rsum = rsum * (self.h /((len(x)-1)*3)) 
        return rsum
                
                
#To include gauss integration                 
            
        
