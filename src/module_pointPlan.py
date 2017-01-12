#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cercles` module

:author: Sauvage Célestine ,Danneels Sophie , Soltysiak Samuel

:date: November-December, 2015

Module for point.


"""
import math
import cmath

##########################################
#       data structure of coord          #
##########################################
#create

def create(x,y):
    """
    create a data structure with coord

    :param x: it a coord x_axis
    :type x: int
    :param y:it a coord y_axis
    :type y: int
    :return: tuple of coord
    :rtype: tuple
    :UC: #Il ne faut pas que cela depasse 
    :Example:
    >>> create(20,36)
    (20, 36)
    >>> create(150,200)
    (150, 200)
    """
    return (x,y)

#picker
def get_x_axis(coord):
    """
    return x_axis of coord
    :param coord:coord
    :type coord: tuple
    :return: x_axis of coord
    :rtype: int
    :UC: none
    """
    return coord[0]

def get_y_axis(coord):
    """
    return y_axis of coord
    :param coord:coord
    :type coord: tuple
    :return: y_axis of coord
    :rtype: int
    :UC: none
    """
    return coord[1]

def coord_to_complex(coord):
    x=get_x_axis(coord)
    y=get_y_axis(coord)
    return complex(x,y)

def complex_to_coord(z):
    return create(z.real,z.imag)

def len_deux_coord(coord1,coord2):
    x1=get_x_axis(coord1)
    y1=get_y_axis(coord1)
    x2=get_x_axis(coord2)
    y2=get_y_axis(coord2)
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def sqrt_complex_petite(coord_complexe):
    a=(coord_complexe.real)
    b=(coord_complexe.imag)
    s3=math.sqrt(a**2+b**2)
    x2=(a+s3)/2
    x=-math.sqrt(x2)
    y=b/(2*x)
    return complex(x,y)


def sqrt_complex_grande(coord_complexe):
    a=(coord_complexe.real)
    b=(coord_complexe.imag)
    s3=math.sqrt(a**2+b**2)
    x2=(a+s3)/2
    x=-math.sqrt(x2)
    y=b/(2*x)
    return complex(x,y)
