__author__ = 'marechaux'

from execution import protobuf
from numpy import *


class Sigmoid:

    @staticmethod
    def function(x):
        return 1/(1+exp(-x))

    @staticmethod
    def differential_auxiliary(y):
        return y*(1-y)

    @staticmethod
    def to_protobuf_message():
        return protobuf.SIGMOID

class Softmax:

    @staticmethod
    def function(x_list):
        sum=0
        for x in x_list:
            x=exp(x)
            sum +=x
        return x_list/sum

    @staticmethod
    def to_protobuf_message():
        return protobuf.SOFTMAX

    #TODO : Add softmax derivative which produce a matrix

class Nothing:

    @staticmethod
    def function(x):
        return x

    @staticmethod
    def differential(y):
        return 1

    @staticmethod
    def to_protobuf_message():
        return protobuf.NOTHING

class LinearError:

    @staticmethod
    def function(y, expected):
        return absolute(y-expected)

    @staticmethod
    def unit_step(x):
        unit_step = lambda x: 0 if x < 0 else 1
        for i in range(len(x)):
            x[i] = unit_step(x[i])
        return x

    @staticmethod
    def differential(y, expected):
        return LinearError.unit_step(y) - expected  #This is not exact but proportional to differential


class QuadraticError:

    @staticmethod
    def function(y, expected):
        return (y-expected)**2

    @staticmethod
    def differential(y, expected):
        return (y-expected)  #This is not exact but proportional to differential
