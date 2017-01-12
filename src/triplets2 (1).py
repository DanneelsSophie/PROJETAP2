#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cercles` module

:author: Sauvage Célestine ,Danneels Sophie , Soltysiak Samuel

:date: November-December, 2015

Module for cercle.

"""
import sys

sys.setrecursionlimit(100000)

import module_cercle as cercle
import module_pointPlan as pointplan
import math
import cmath
from random import *
A=pointplan.create(150,150)
B=pointplan.create(250,250)
C=pointplan.create(300,200)
cercleA = cercle.create(A,100)
cercleB = cercle.create(B,210)
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

##########################################
#       tangent                          #
##########################################


def tangent(A,B,C):
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

def big_radius(cercleA,cercleB,cercleC):
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
    a = cercle.get_radius(cercleA)
    b = cercle.get_radius(cercleB)
    c = cercle.get_radius(cercleC)
    if abs(a) > abs(b):
        if abs(a) > abs(c):
            return cercleA
        else:
            return cercleC
    elif abs(b) > abs(c):
        return cercleB
    else :
        return cercleC

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
    
def rayons_cercle(cercleA,cercleB,cercleC):#rename with radius_circle
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
    r1=cercle.get_radius(cercleA)
    r2=cercle.get_radius(cercleB)
    r3=cercle.get_radius(cercleC)
    k1=1/(r1)
    k2=1/(r2)
    k3=1/(r3)
    truc = (math.sqrt(k1*k2+k1*k3+k2*k3))
    k4petit=(k1+k2+k3)+2*truc
    k4grand=(k1+k2+k3)-2*truc
    return compare(1/k4petit,1/k4grand)

def rayons_cercle_entoure(cercleA,cercleB,cercleC):
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
    k1=1/(complex(cercle.get_radius(cercleA)))
    k2=1/(complex(cercle.get_radius(cercleB)))
    k3=-1/(complex(cercle.get_radius(cercleC)))
    truc = (cmath.sqrt(k1*k2+k1*k3+k2*k3))
    k4petit=(k1+k2+k3)+2*truc
    k4grand=(k1+k2+k3)-2*truc
    return compare(1/k4petit,1/k4grand)

def center_small_inscrit(cercleA,cercleB,cercleC):
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
    k1=1/(cercle.get_radius(cercleA))
    k2=1/(cercle.get_radius(cercleB))
    k3=(1/(cercle.get_radius(cercleC)))
    z1=pointplan.coord_to_complex(cercle.get_center(cercleA))
    z2=pointplan.coord_to_complex(cercle.get_center(cercleB))
    z3=pointplan.coord_to_complex(cercle.get_center(cercleC))
    base=(k1*z1)+(k2*z2)+(z3*k3)
    k4=rayons_cercle(cercleA,cercleB,cercleC)
    baseinterieur=(k1*k2*z1*z2)+(k2*k3*z2*z3)+(k1*k3*z1*z3)
    z4_1=k4*(base+2*cmath.sqrt(baseinterieur))
    return pointplan.complex_to_coord(z4_1)



def center_small_entoure(cercleA,cercleB,cercleC):
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
    k1=1/(cercle.get_radius(cercleA))
    k2=1/(cercle.get_radius(cercleB))
    k3=-(1/(cercle.get_radius(cercleC)))
    z1=pointplan.coord_to_complex(cercle.get_center(cercleA))
    z2=pointplan.coord_to_complex(cercle.get_center(cercleB))
    z3=pointplan.coord_to_complex(cercle.get_center(cercleC))
    base=(k1*z1)+(k2*z2)+(z3*k3)
    k4=rayons_cercle_entoure(cercleA,cercleB,cercleC)
    baseinterieur=(k1*k2*z1*z2)+(k2*k3*z2*z3)+(k1*k3*z1*z3)
    z4_1=k4*(base+2*cmath.sqrt(baseinterieur))
    z4_2=k4*(base-2*cmath.sqrt(baseinterieur))
    return (pointplan.complex_to_coord(z4_1),pointplan.complex_to_coord(z4_2))


##########################################
#       drawn small circle tangent      #
##########################################


def get_mini(cercleA,cercleB,cercleC):
    """
    drawn a circle which is tangent cercleA,cercleB and cercleC on Tkinter (canvas)
    
    :param cercleA: it is a circle
    :type cercleA: a circle
    :param cercleB: it is a circle
    :type cercleB: a circle
    :param cercleC: it is a circle
    :type cercleC: a circle
    :return: the little circle and a drawn on tkinter a circle which it tangent cercleA,cercleB and cercleC
    :rtype: a circle
    :UC: none
    :Examples:
    """
    plus_gros=big_radius(cercleA,cercleB,cercleC)
    if plus_gros == cercleA :
        cercleA,cercleC = cercleC,cercleA
    if plus_gros == cercleB :
        cercleB,cercleC = cercleC,cercleB
    if point_is_in_circle(cercleC,cercle.get_center(cercleA)) and point_is_in_circle(cercleC,cercle.get_center(cercleB)) :
        center_c = center_small_entoure(cercleA,cercleB,cercleC)                 
        if (point_is_in_circle(cercleC,center_c[0])) and (not(point_is_in_circle(cercleA,center_c[0]))) and (not(point_is_in_circle(cercleB,center_c[0]))):
            centre_c = center_c[0]
        else :
            centre_c = center_c[1]
        cercle_petit=cercle.create(centre_c,rayons_cercle_entoure(cercleA,cercleB,cercleC))
        cercle.draw_circle(cercle_petit)
        return cercle_petit
    else :
        cercle_petit=cercle.create(center_small_inscrit(cercleA,cercleB,cercleC),rayons_cercle(cercleA,cercleB,cercleC))
        return cercle_petit

def create_liste_tangent(l): # param l : liste des cercles dessinés avec draw_ncercles
    """
    ça retourne une liste des 3cercles tangents quand tu les dessines avec draw_ncercles
    par exemple : a = cercle.draw_ncercles(cercleA,3)
    Tu auras [(cercleA,a[0],a[1]),(cercleA,a[1],a[2]),(cercleA,a[2],a[0]),(a[4]( c'est le petit du milieu),a[0],a[1]),(a[4],a[1],a[2]),(a[4],a[2],a[0])]"""
    """
    return a list of all 3 circles tangents created with the fonction draw_ncercles

    :param l: circles created with draw_ncercles
    :type l: list of circles
    :return: a list of circles that are tangents 2 to 2
    :rtype: a list
    :UC: circles need to be created with fonction draw_ncercles
    :Example:
    """
    
    l1 = [(l[0],l[len(l)-3],l[len(l)-2])] + [(l[0],l[len(l)-3],l[len(l)-1])]
    def aux(l,l_trpl):
        if len(l)==3: # Quand il ne reste plus que le dernier cercle, le grand cercle et le plus petit, tu as finis
            return l_trpl
        else :
            l_trpl += [(l[0],l[1],l[len(l)-1])] + [(l[0],l[1],l[len(l)-2])] # Tu ajoutes le triplet de Suddy ( les 3 cercles tangents 2 à 2 ) le premeir : avec le grand le deuxième : avec le petit
            return aux(l[1:],l_trpl) # Tu continues en enlevant le cercle du début
        
    return aux(l,l1)


def draw_all_circles(l,l2,l3): # l : listes des cercles tangents , l2 l3 listes vides au début
    """
    draw all cercles 

    :param l: list of circles that are tangents 2 à 2
    :type l: list of circles
    :return: a list of circles thath are tangents 2 à 2 with the mini cercle
    :rtype: a list
    :UC:
    :Example:
    """
    if len(l)==0:
        return (l2,l3) # l2 : listes des cercles tangents, l3 : listes des cercles crées
    else:
        a = l[0]
        while len(a)!=0 :
            mini = get_mini(a[0],a[1],a[2])
            if cercle.get_radius(mini) > 1 :
                cercle.draw_circle(mini)
                l3.append(mini)
                l2 += [[mini,a[0],a[1]] + [mini,a[1],a[2]] + [mini,a[0],a[2]]]
                a=a[3:]
            else :
                break
        return draw_all_circles(l[1:],l2,l3)

def baderne1(cercleA,n_cercles): # pour faire tout les cercles
    a = cercle.draw_ncercles(cercleA,n_cercles)
    c = draw_all_circles(create_liste_tangent(a),[],[])
    d = liste_cercle_vide(cercleA,n_cercles) + c[1]
    for i in range(10):
        c = draw_all_circles(c[0],[],[])
        d += c[1]
    return d


def draw_all_circles2(l,l2,n_cercles,n_profondeur):
	if n_profondeur==0:
		pass
	elif l==[]:
		return l2
	else:
		if cercle.get_radius(l[0])<3:
			return draw_all_circles2(l[1:],l2,n_cercles,n_profondeur)
		else:
			l2 += baderne1(l[0],n_cercles)
			return draw_all_circles2(l[1:],l2,n_cercles,n_profondeur)
		    

def baderne2(cercleA,n_cercles,n_profondeur):
    a = baderne1(cercleA,n_cercles)
    for i in range(n_profondeur-1):
        a = draw_all_circles2(a,[],n_cercles,n_profondeur-i)
    print('finish')

def baderne2_plus(cercleA,n_cercles,n_profondeur):
    a = baderne1(cercleA,n_cercles)
    for i in range(n_profondeur-1):
        a = draw_all_circles2(a,[],n_cercles+i,n_profondeur-i)
    print('finish')

def baderne1_random(cercleA): # pour faire tout les cercles
    int_r = randint(3,10)
    a = cercle.draw_ncercles(cercleA,int_r)
    c = draw_all_circles(create_liste_tangent(a),[],[])
    d = liste_cercle_vide(cercleA,int_r) + c[1]
    for i in range(10):
        c = draw_all_circles(c[0],[],[])
        d += c[1]
    return d
                             
def draw_all_circles2_random(l,l2,n_profondeur):
	if n_profondeur==0:
		pass
	elif l==[]:
		return l2
	else:
		if cercle.get_radius(l[0])<3:
			return draw_all_circles2(l[1:],l2,randint(3,10),n_profondeur)
		else:
			l2 += baderne1_random(l[0])
			return draw_all_circles2(l[1:],l2,randint(3,10),n_profondeur)

def baderne2_random(cercleA,n_profondeur):
    a = baderne1(cercleA,randint(3,10))
    for i in range(n_profondeur-1):
        a = draw_all_circles2_random(a,[],n_profondeur-i)
    print('finish')

            
def liste_cercle_vide(cercleA,n_cercles): # crée une liste des cercles à remplir
    a = cercle.draw_ncercles(cercleA,n_cercles)
    l = []
    for i in range (len(a)-1):
        l.append(a[i])
    return l

