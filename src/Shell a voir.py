Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\cercles2.py 
>>> draw_circle(a)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    draw_circle(a)
NameError: name 'a' is not defined
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\cercles2.py 
>>> draw_circle(cercleA)
>>> r(cercle,3)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    r(cercle,3)
NameError: name 'cercle' is not defined
>>> r(cercleA,3)
7.179676972449085
>>> r1(cercleA,3)
46.410161513775456
>>> draw_ncercles(cercleA,3)
>>> test = cercles_tangents(cercleA,3)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    test = cercles_tangents(cercleA,3)
NameError: name 'cercles_tangents' is not defined
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\cercles2.py 
>>> cercles_tangents(cercleA,3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cercles_tangents(cercleA,3)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\cercles2.py", line 255, in cercles_tangents
    x_cercle=get_x_axis(cercle)
NameError: name 'get_x_axis' is not defined
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\cercles2.py 
>>> cercles_tangents(cercleA,3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    cercles_tangents(cercleA,3)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\cercles2.py", line 255, in cercles_tangents
    x_cercle=pointplan.get_x_axis(cercle)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\pointplan.py", line 21, in get_x_axis
    return coord[0]
KeyError: 0
>>> draw_circle(cercleA)
>>> r(cercle,3)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    r(cercle,3)
NameError: name 'cercle' is not defined
>>> r(cercleA,3)
7.179676972449085
>>> r1(cercleA,3)
46.410161513775456
>>> cercleB = create(223.20508075688775,296.41016151377545,46.410161513775456)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    cercleB = create(223.20508075688775,296.41016151377545,46.410161513775456)
TypeError: create() takes 2 positional arguments but 3 were given
>>> cercleB = create(pointplan.create(223.20508075688775,296.41016151377545),46.410161513775456)
>>> cercleC = create(pointplan.create(223.2050807568877, 203.58983848622455),46.410161513775456)
>>> draw_circle(cercleB)
>>> draw_circle(cercleC)
>>> import triplets2
>>> triplets2.rayons_cercle(cercleA,cercleC)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    triplets2.rayons_cercle(cercleA,cercleC)
TypeError: rayons_cercle() missing 1 required positional argument: 'cercleC'
>>> triplets2.rayons_cercle(cercleA,cercleB,cercleC)
(8.854709733422611, -148.2309783324849)
>>> center(cercleA,cercleB,cercleC)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    center(cercleA,cercleB,cercleC)
NameError: name 'center' is not defined
>>> triplets2.center(cercleA,cercleB,cercleC)
((229.5643196996119+249.3830983688748j), (-14.947368927272054-14.317071403784764j), (229.5643196996119+249.3830983688748j), (-14.947368927272054-14.317071403784764j))
>>> prout = pointplan.create(229.5643196996119,249.3830983688748)
>>> draw_circle(prout,8.854709733422611)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    draw_circle(prout,8.854709733422611)
TypeError: draw_circle() takes 1 positional argument but 2 were given
>>> draw_circle(create(prout,8.854709733422611))
>>> def rayons_cercle(cercleA,cercleB,cercleC):
    k1=1/(cercle2.get_radius(cercleA))
    k2=1/(cercle2.get_radius(cercleB))
    k3=-1/(cercle2.get_radius(cercleC))
    truc = (math.sqrt(k1*k2+k1*k3+k2*k3))
    k4petit=(k1+k2+k3)+2*truc
    k4grand=(k1+k2+k3)-2*truc
    return (1/k4petit,1/k4grand)

>>> triplets2.rayons_cercle(cercleA,cercleB,cercleC)
(8.854709733422611, -148.2309783324849)
>>> rayons_cercle(cercleA,cercleB,cercleC)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    rayons_cercle(cercleA,cercleB,cercleC)
  File "<pyshell#27>", line 2, in rayons_cercle
    k1=1/(cercle2.get_radius(cercleA))
NameError: name 'cercle2' is not defined
>>> def rayons_cercle(cercleA,cercleB,cercleC):
    k1=1/(get_radius(cercleA))
    k2=1/(get_radius(cercleB))
    k3=-1/(get_radius(cercleC))
    truc = (math.sqrt(k1*k2+k1*k3+k2*k3))
    k4petit=(k1+k2+k3)+2*truc
    k4grand=(k1+k2+k3)-2*truc
    return (1/k4petit,1/k4grand)

>>> rayons_cercle(cercleA,cercleB,cercleC)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    rayons_cercle(cercleA,cercleB,cercleC)
  File "<pyshell#31>", line 5, in rayons_cercle
    truc = (math.sqrt(k1*k2+k1*k3+k2*k3))
ValueError: math domain error
>>> import math
>>> def rayons_cercle(cercleA,cercleB,cercleC):
    k1=1/(get_radius(cercleA))
    k2=1/(get_radius(cercleB))
    k3=-1/(get_radius(cercleC))
    truc = (math.sqrt(k1*k2+k1*k3+k2*k3))
    k4petit=(k1+k2+k3)+2*truc
    k4grand=(k1+k2+k3)-2*truc
    return (1/k4petit,1/k4grand)

>>> rayons_cercle(cercleA,cercleB,cercleC)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    rayons_cercle(cercleA,cercleB,cercleC)
  File "<pyshell#35>", line 5, in rayons_cercle
    truc = (math.sqrt(k1*k2+k1*k3+k2*k3))
ValueError: math domain error
>>> complex(get_radius(cercleA))
(100+0j)
>>> def rayons_cercle(cercleA,cercleB,cercleC):
    k1=1/(complex(get_radius(cercleA)))
    k2=1/(complex(get_radius(cercleB)))
    k3=-1/(complex(get_radius(cercleC)))
    truc = (cmath.sqrt(k1*k2+k1*k3+k2*k3))
    k4petit=(k1+k2+k3)+2*truc
    k4grand=(k1+k2+k3)-2*truc
    return (1/k4petit,1/k4grand)

>>> import cmath
>>> rayons_cercle(cercleA,cercleB,cercleC)
((5.109617221084916-22.01938995436713j), (5.109617221084916+22.01938995436713j))
>>> fufu = rayons_cercle(cercleA,cercleB,cercleC)
>>> abs(fufu)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    abs(fufu)
TypeError: bad operand type for abs(): 'tuple'
>>> abs(fufu[0])
22.60446243794556
>>> draw_circle(pointplan.create(175,250),abs(fufu[0]))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    draw_circle(pointplan.create(175,250),abs(fufu[0]))
TypeError: draw_circle() takes 1 positional argument but 2 were given
>>> draw_circle(create(pointplan.create(175,250),abs(fufu[0])))
>>> 
draw_circle(create(pointplan.create(175,250),abs(fufu[1])))
>>> 
>>> draw_circle(create(pointplan.create(315,250),abs(fufu[1])))
>>> pipi = point.plant(create(100,100))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    pipi = point.plant(create(100,100))
NameError: name 'point' is not defined
>>> pipi = pointplan.(create(100,100))
SyntaxError: invalid syntax
>>> pipi = pointplan.create(100,100)
>>> cercleH = create(pipi,140)
>>> draw_circle(cercleH)
>>> popo = pointplan.(create(175.02577388071438,99.99999999999999))
SyntaxError: invalid syntax
>>> popo = pointplancreate(175.02577388071438,99.99999999999999))
SyntaxError: invalid syntax
>>> popo = pointplan.create(175.02577388071438,99.99999999999999)
>>> cercleJ=create(popo,64.97422611928565)
>>> draw_circle(cercleJ)
>>> pupu = pointplan.create(62.48711305964278,35.02577388071437)
>>> cercleK=create(pupu,64.97422611928565)
>>> draw_circle(cercleK)
>>> rayons_cercle(cercleH,cercleJ,cercleK)
((7.153464109518885-30.827145936113986j), (7.153464109518885+30.827145936113986j))
>>> fafa = rayons_cercle(cercleH,cercleJ,cercleK)
>>> draw_circle(pointplan.create(165,20),abs(fafa[0]))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    draw_circle(pointplan.create(165,20),abs(fafa[0]))
TypeError: draw_circle() takes 1 positional argument but 2 were given
>>> draw_circle(create(pointplan.create(165,20),abs(fafa[0])))
>>> 
