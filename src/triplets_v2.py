#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cercles` module

:author: Sauvage Célestine ,Danneels Sophie , Soltysiak Samuel

:date: November-December, 2015

Module for cercle.

"""
import module_cercle as cercle
import module_pointPlan as pointplan
import math
import cmath
A=pointplan.create(150,150)
B=pointplan.create(220,300)
C=pointplan.create(300,200)
cercleA = cercle.create(A,100)
cercleB = cercle.create(B,120)
cercleC = cercle.create(C,150)

##########################################
#       data structure of cercle         #
##########################################



def create(cercleA,cercleB,cercleC):
    """
    create a data structure with three circles

    :param cercleA: it is a circle
    :type cercleA: a circle
    :param cercleB: it is a circle
    :type cercleB: a circle
    :param cercleC: it is a circle
    :type cercleC: a circle
    :return: [cercleA,cercleB,cercleC]
    :rtype: a list
    :UC: none
    :Example:

    >>> cercleA =cercle.create(pointplan.create(150,100),100)
    >>> cercleB =cercle.create(pointplan.create(200,250),50)
    >>> cercleC =cercle.create(pointplan.create(280,250),30)
    >>> create(cercleA,cercleB,cercleC)
    [{'center': (150, 100), 'radius': 100}, {'center': (200, 250), 'radius': 50}, {'center': (280, 250), 'radius': 30}]
    """
    return [cercleA,cercleB,cercleC]

def get_cercle(triplet,n): #récupère le cercle en position n
    return triplet[n]

def modif_triplet(triplet,cercle,n): #modifie le cercle à la place n dans le triplet dans le tuplet
    if n==0:
        return create(cercle,get_cercle(triplet,1),get_cercle(triplet,2))
    elif n==1:
        return create(get_cercle(triplet,0),cercle,get_cercle(triplet,2))
    else:
        return create(get_cercle(triplet,0),get_cercle(triplet,1),cercle)

def echange_place(triplet,place1,place2): #échange la place de 2 cercles dans le tuple
    if place1>place2:
        place1,place2=place2,place1
    if place1==0:
        if place2==1:
           return create(get_cercle(triplet,place2),get_cercle(triplet,place1),get_cercle(triplet,2))
        else:
           return create(get_cercle(triplet,place2),get_cercle(triplet,2),get_cercle(triplet,place1))
    elif place1==1:
       return create(get_cercle(triplet,0),get_cercle(triplet,place2),get_cercle(triplet,place1))

##########################################
#       tangent                          #
##########################################


def tangent(triplet):
    """
    drawn three circles with 3 center A,B,C of circles

    :param A: it is a center of an circle one
    :type A: coordinated (poitplan.create)
    :param B: it is a center of an circle two
    :type B: coordinated (poitplan.create)
    :param C: it is a center of an circle three
    :type C: coordinated (poitplan.create)
    :return: drawn on tkinter three circles tangent
    :rtype: None
    :UC: none
    
    """
    AB=pointplan.len_deux_coord(A,B)
    AC=pointplan.len_deux_coord(A,C)
    BC=pointplan.len_deux_coord(B,C)
    longeur=-AB+AC+BC
    cercleC=cercle.create(C,longeur/2)
    cercle.draw_circle(cercleC)
    longeur1=AB+AC-BC
    cercleA=cercle.create(A,longeur1/2)
    cercle.draw_circle(cercleA)
    longeur3=AB-AC+BC
    cercleB=cercle.create(B,longeur3/2)
    cercle.draw_circle(cercleB)

##########################################
#      function formula mathematical    #
##########################################


def compare(a,b):
    """
    compare two name a and b and return smallest int part abs
    :type a: int
    :type b: int
    :return: smallest int part abs
    :rtype: int
    :Examples:
    >>> compare(-5,10)
    5
    >>> compare(-25,10)
    10
    """
    if abs(a) > abs(b):
        return abs(b)
    elif abs(a)==abs(b):
        return abs(a)
    else :
        return abs(a)

def big_radius(triplet):
    """
    return  a circle have a bigger radius

    :param cercleA: it is a circle
    :type cercleA: a circle
    :param cercleB: it is a circle
    :type cercleB: a circle
    :param cercleC: it is a circle
    :type cercleC: a circle
    :return: a circle have a bigger radius
    :rtype: a circle
    :UC: none
    :Examples:
    >>>cercleA = cercle.create(A,100)
    >>>cercleB = cercle.create(B,120)
    >>>cercleC = cercle.create(C,150)
    >>> big_radius(cercleA,cercleB,cercleC)
    {'center': (300, 200), 'radius': 150}
    """
    a = cercle.get_radius(get_cercle(triplet,0))
    b = cercle.get_radius(get_cercle(triplet,1))
    c = cercle.get_radius(get_cercle(triplet,2))
    if abs(a) > abs(b):
        if abs(a) > abs(c):
            return get_cercle(triplet,0)
        else:
            return get_cercle(triplet,2)
    elif abs(b) > abs(c):
        return get_cercle(triplet,1)
    else :
        return get_cercle(triplet,2)

def point_is_in_circle(cercleA,coord):#rename the function dot 
    """
    return  True or False if dot is in circle

    :param cercleA: it is a circle
    :type cerlceA: a circle
    :param coord: coordinated (with module pointplan)
    :type coord: coord
    :return: True of False if dot is in circle True if not False
    :rtype: bool
    :UC: none
    :Examples:
    >>>cercleA = cercle.create(A,100)
    >>>A=pointplan.create(150,150)
    >>>B=pointplan.create(220,300)
    >>> point_is_in_circle(cercleA,A)
    True
    >>> point_is_in_circle(cercleA,B)
    False
    """
    rayon = cercle.get_radius(cercleA)
    centreCercle = cercle.get_center(cercleA)
    longueur = pointplan.len_deux_coord(centreCercle,coord)
    return longueur < rayon

def is_tangent(cercleA,cercleB): #marchepas
    rayon1 = cercle.get_radius(cercleA)
    rayon2 = cercle.get_radius(cercleB)
    centre1 = cercle.get_center(cercleA)
    centre2 = cercle.get_center(cercleB)
    longueur = pointplan.len_deux_coord(centre1,centre2)
    print (longueur)
    print(rayon1+rayon2)
    return longueur == rayon1+rayon2
    
def rayons_cercle(triplet):#rename with radius_circle
    """
    return  a radius of small circle when two circles it are inscribed and tangent together.

    :param cercleA: it is a circle
    :type cercleA: a circle
    :param cercleB: it is a circle
    :type cercleB: a circle
    :param cercleC: it is a circle
    :type cercleC: a circle
    :return: a radius of small circle when two circles it are inscribed
    :rtype: int
    :UC: none
    :Examples:
    """
    #Faire l'exemple
    r1 = cercle.get_radius(get_cercle(triplet,0))
    r2 = cercle.get_radius(get_cercle(triplet,1))
    r3 = cercle.get_radius(get_cercle(triplet,2))
    k1=1/(r1)
    k2=1/(r2)
    k3=1/(r3)
    truc = (math.sqrt(k1*k2+k1*k3+k2*k3))
    k4petit=(k1+k2+k3)+2*truc
    k4grand=(k1+k2+k3)-2*truc
    return compare(1/k4petit,1/k4grand)

def rayons_cercle_entoure(triplet):
    """
    return  a radius of small circle when two circles it aren't inscribed and tangent together .

    :param cercleA: it is a circle
    :type cercleA: a circle
    :param cercleB: it is a circle
    :type cercleB: a circle
    :param cercleC: it is a circle
    :type cercleC: a circle
    :return: a radius of small circle when two circles it aren't inscribed
    :rtype: int
    :UC: none
    :Examples:
    """
    #exemple
    k1=1/(complex(cercle.get_radius(get_cercle(triplet,0))))
    k2=1/(complex(cercle.get_radius(get_cercle(triplet,1))))
    k3=-1/(complex(cercle.get_radius(get_cercle(triplet,2))))
    truc = (cmath.sqrt(k1*k2+k1*k3+k2*k3))
    k4petit=(k1+k2+k3)+2*truc
    k4grand=(k1+k2+k3)-2*truc
    return compare(1/k4petit,1/k4grand)

def center_small_inscrit(triplet):
    """
    return  a center of small circle when two circles it are inscribed and tangent together .

    :param cercleA: it is a circle
    :type cercleA: a circle
    :param cercleB: it is a circle
    :type cercleB: a circle
    :param cercleC: it is a circle
    :type cercleC: a circle
    :return: a center (with coord) of small circle when two circles it are inscribed
    :rtype: int
    :UC: none
    :Examples:
    """
    a = get_cercle(triplet,0)
    b = get_cercle(triplet,1)
    c = get_cercle(triplet,2)
    k1=1/(cercle.get_radius(a))
    k2=1/(cercle.get_radius(b))
    k3=1/(cercle.get_radius(c))
    z1=pointplan.coord_to_complex(cercle.get_center(a))
    z2=pointplan.coord_to_complex(cercle.get_center(b))
    z3=pointplan.coord_to_complex(cercle.get_center(c))
    base=(k1*z1)+(k2*z2)+(z3*k3)
    k4=rayons_cercle(triplet)
    baseinterieur=(k1*k2*z1*z2)+(k2*k3*z2*z3)+(k1*k3*z1*z3)
    z4_1=k4*(base+2*cmath.sqrt(baseinterieur))
    return pointplan.complex_to_coord(z4_1)



def center_small_entoure(triplet):
    """
    return  a center of small circle when two circles it aren't inscribed and tangent together .

    :param cercleA: it is a circle
    :type cercleA: a circle
    :param cercleB: it is a circle
    :type cercleB: a circle
    :param cercleC: it is a circle
    :type cercleC: a circle
    :return: a center(with coord) of small circle when two circles it aren't inscribed
    :rtype: int
    :UC: none
    :Examples:
    """
    a = get_cercle(triplet,0)
    b = get_cercle(triplet,1)
    c = get_cercle(triplet,2)
    k1=1/(cercle.get_radius(a))
    k2=1/(cercle.get_radius(b))
    k3=-(1/(cercle.get_radius(c)))
    z1=pointplan.coord_to_complex(cercle.get_center(a))
    z2=pointplan.coord_to_complex(cercle.get_center(b))
    z3=pointplan.coord_to_complex(cercle.get_center(c))
    base=(k1*z1)+(k2*z2)+(z3*k3)
    k4=rayons_cercle_entoure(triplet)
    baseinterieur=(k1*k2*z1*z2)+(k2*k3*z2*z3)+(k1*k3*z1*z3)
    z4_1=k4*(base+2*cmath.sqrt(baseinterieur))
    z4_2=k4*(base-2*cmath.sqrt(baseinterieur))
    return (pointplan.complex_to_coord(z4_1),pointplan.complex_to_coord(z4_2))


##########################################
#       drawn small circle tangent      #
##########################################


def draw_mini(triplet):
    """
    drawn a circle which is tangent cercleA,cercleB and cercleC on Tkinter (canvas)
    
    :param cercleA: it is a circle
    :type cercleA: a circle
    :param cercleB: it is a circle
    :type cercleB: a circle
    :param cercleC: it is a circle
    :type cercleC: a circle
    :return: a drawn on tkinter a circle which it tangent cercleA,cercleB and cercleC
    :rtype: None
    :UC: none
    :Examples:
    """
    plus_gros=big_radius(triplet)
    if plus_gros == get_cercle(triplet,0) :
        triplet = echange_place(triplet,0,2)
    if plus_gros == get_cercle(triplet,1) :
        triplet = echange_place(triplet,1,2)
    a = get_cercle(triplet,0)
    b = get_cercle(triplet,1)
    c = get_cercle(triplet,2)
    print(triplet)
    if point_is_in_circle(c,cercle.get_center(a)) and point_is_in_circle(c,cercle.get_center(b)) :
        center_c = center_small_entoure(triplet)                 
        if (point_is_in_circle(c,center_c[0])) and (not(point_is_in_circle(a,center_c[0]))) and (not(point_is_in_circle(b,center_c[0]))):
            centre_c = center_c[0]
        else :
            centre_c = center_c[1]
        cercle_petit=cercle.create(centre_c,rayons_cercle_entoure(triplet))
        cercle.draw_circle(cercle_petit)
        return cercle_petit
    else :
        cercle_petit=cercle.create(center_small_inscrit(triplet),rayons_cercle(triplet))
        cercle.draw_circle(cercle_petit)
        return cercle_petit

def create_baderne(cercle_grand,nombre):
    baderne=cercle.draw_ncercles(cercle_grand,nombre)
    petit=cercle.get_radius(baderne[0])
    grand=cercle.get_radius(baderne[0])
    l=[]
    for i in baderne:
        if cercle.get_radius(i)<=petit:
            petit=cercle.get_radius(i)
            small=i
    l=[small]+[cercle_grand]
    for i in baderne:
        if i!=l[0]:
            l=l+[i]
    return l

    
        
""" def recursion2(baderne,n):
    if n==0:
        pass
    else:
        cercle1=draw_mini(baderne[1],baderne[2],baderne[3])
        recursion(create_baderne(cercle1,3),n-1)
        cercle2=draw_mini(baderne[0],baderne[2],baderne[3])
        recursion(create_baderne(cercle2,3),n-1)
        cercle3=draw_mini(baderne[0],baderne[4],baderne[3])
        recursion(create_baderne(cercle3,3),n-1)
        cercle4=draw_mini(baderne[1],baderne[4],baderne[3])
        recursion(create_baderne(cercle4,3),n-1)
        cercle5=draw_mini(baderne[0],baderne[4],baderne[2])
        recursion(create_baderne(cercle5,3),n-1)
        cercle6=draw_mini(baderne[1],baderne[4],baderne[2])
        recursion(create_baderne(cercle6,3),n-1)
"""

def recursion(cercle,n_cercles,n_fois):
    def aux (cercle,l,n_cercles,n_fois):
        if n_fois==0:
            pass
        if len(a)== 1:
            aux(cercle_cree,l,n_cercles,(n_fois-1))
        else:
            cercle_cree = draw_mini(l[(len(l)-1)],l[0],l[1])
            return aux(cercle_cree,l[1:],n_cercles,n_fois)
    aux(cercle,l_1,n_cercles,n_fois)
       
        
"""def recur1(cercleA,nb_cercle,n_fois):
    liste_cercle = cercle.draw_ncercles(cercleA,nb_cercle)
    def aux(cercle,liste,i,j,k,n_fois):
        if k == 0:
            pass
        if k == len(liste):
            
        if i == len(liste) :
            return aux(liste[k+1],liste,0,1,k+1,nb_cercle,n_fois)
    else:
        draw_mini(cercle,liste[i],liste[j])
        return aux(cercle,liste,i+1,j+1,k,nb_cercle,n_fois)

def recurdef recur1(cercleA,nb_cercle,n_fois):
    liste_cercle = cercle.draw_ncercles(cercleA,nb_cercle)
    len_liste = len(liste_cercle)
    def aux(cercle,l,i,j,k,n_fois):
        if n_fois == 0 :
            return aux(cercle,l,
        else :"""
            
