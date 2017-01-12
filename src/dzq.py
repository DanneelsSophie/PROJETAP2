Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> compare3_grand(1,2,3)
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> compare3_grand(1,2,3)
3
>>> compare3_grand(4,2,3)
4
>>> compare3_grand(4,2,4)
4
>>> compare3_grand(4,8,4)
8
>>> compare3_grand(1,8,4)
8
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> big_radius(cercleA,cercleB,cercleC)
{'radius': 200, 'center': (300, 200)}
>>> big_radius(cercleB,cercleA,cercleC)
{'radius': 200, 'center': (300, 200)}
>>> big_radius(cercleC,cercleB,cercleA)
{'radius': 200, 'center': (300, 200)}
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleA,cercleB,cercleC)
({'radius': 100, 'center': (150, 150)}, {'radius': 150, 'center': (220, 300)}, {'radius': 200, 'center': (300, 200)})
>>> draw_mini(cercleC,cercleB,cercleA)
({'radius': 200, 'center': (300, 200)}, {'radius': 150, 'center': (220, 300)}, {'radius': 200, 'center': (300, 200)})
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleC,cercleB,cercleA)
({'center': (150, 150), 'radius': 100}, {'center': (300, 200), 'radius': 200}, {'center': (220, 300), 'radius': 150})
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleC,cercleB,cercleA)
({'center': (150, 150), 'radius': 100}, {'center': (220, 300), 'radius': 150}, {'center': (300, 200), 'radius': 200})
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> cercleB=cercle.create(B,120)
>>> cercle1=cercle.create(pointplan.create(187.84609690826528, 355.69219381653056),55.69219381653055)
>>> cercle2=cercle.create(pointplan.create(187.84609690826525, 244.30780618346947),55.69219381653055)
>>> draw_mini(cercleB,cercle1,cercle2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle2)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 127, in draw_mini
    cercle_petit=cercle.create(center_small_entoure(cercleA,cercleB,cercleC),rayons_cercle_entoure(cercleA,cercleB,cercleC)[0])
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 114, in center_small_entoure
    k4=rayons_cercle_entoure(cercleA,cercleB,cercleC)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 89, in rayons_cercle_entoure
    return compare(1/k4petit,1/k4grand)
NameError: name 'compare' is not defined
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> cercleB=cercle.create(B,120)
>>> cercle1=cercle.create(pointplan.create(187.84609690826528, 355.69219381653056),55.69219381653055)
>>> cercle2=cercle.create(pointplan.create(187.84609690826525, 244.30780618346947),55.69219381653055)
>>> draw_mini(cercleB,cercle1,cercle2)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle2)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 127, in draw_mini
    cercle_petit=cercle.create(center_small_entoure(cercleA,cercleB,cercleC),rayons_cercle_entoure(cercleA,cercleB,cercleC)[0])
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 117, in center_small_entoure
    return pointplan.complex_to_coord(z4_1)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\module_pointPlan.py", line 33, in complex_to_coord
    return create(z.real,z.img)
AttributeError: 'complex' object has no attribute 'img'
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> cercleB=cercle.create(B,120)
>>> cercle1=cercle.create(pointplan.create(187.84609690826528, 355.69219381653056),55.69219381653055)
>>> draw_mini(cercleB,cercle1,cercle2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle2)
NameError: name 'cercle2' is not defined
>>> cercle2=cercle.create(pointplan.create(187.84609690826525, 244.30780618346947),55.69219381653055)
>>> draw_mini(cercleB,cercle1,cercle2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle2)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 127, in draw_mini
    cercle_petit=cercle.create(center_small_entoure(cercleA,cercleB,cercleC),rayons_cercle_entoure(cercleA,cercleB,cercleC)[0])
TypeError: 'float' object is not subscriptable
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> cercleB=cercle.create(B,120)
>>> cercle1=cercle.create(pointplan.create(187.84609690826528, 355.69219381653056),55.69219381653055)
>>> cercle2=cercle.create(pointplan.create(187.84609690826525, 244.30780618346947),55.69219381653055)
>>> draw_mini(cercleB,cercle1,cercle2)
>>> draw_circle(cercleB)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    draw_circle(cercleB)
NameError: name 'draw_circle' is not defined
>>> cercle.draw_circle(cercleB)
>>> cercle.draw_circle(cercle1)
>>> cercle.draw_circle(cercle2)
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> cercleB=cercle.create(B,120)
>>> cercle1=cercle.create(pointplan.create(187.84609690826528, 355.69219381653056),55.69219381653055)
>>> cercle2=cercle.create(pointplan.create(187.84609690826525, 244.30780618346947),55.69219381653055)
>>> cercle.draw_circle(cercleB)
>>> cercle.draw_circle(cercle1)
>>> cercle.draw_circle(cercle2)
>>> draw_mini(cercleB,cercle1,cercle2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle2)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 129, in draw_mini
    cercle.draw_circle(cercle_petit)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\module_cercle.py", line 98, in draw_circle
    x=module_pointPlan.get_x_axis(get_center(cercle))
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\module_pointPlan.py", line 22, in get_x_axis
    return coord[0]
TypeError: 'float' object is not subscriptable
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> cercleB=cercle.create(B,120)
>>> cercle1=cercle.create(pointplan.create(187.84609690826528, 355.69219381653056),55.69219381653055)
>>> cercle2=cercle.create(pointplan.create(187.84609690826525, 244.30780618346947),55.69219381653055)
>>> cercle.draw_circle(cercleB)
>>> cercle.draw_circle(cercle1)
>>> cercle.draw_circle(cercle2)
>>> draw_mini(cercleB,cercle1,cercle2)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle2)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 128, in draw_mini
    cercle_petit=cercle.create(center_small_entoure(cercleA,cercleB,cercleC)[1],rayons_cercle_entoure(cercleA,cercleB,cercleC))
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 118, in center_small_entoure
    return pointplan.complex_to_coord(z4_1,z4_2)
TypeError: complex_to_coord() takes 1 positional argument but 2 were given
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> cercleB=cercle.create(B,120)
>>> cercle1=cercle.create(pointplan.create(187.84609690826528, 355.69219381653056),55.69219381653055)
>>> cercle2=cercle.create(pointplan.create(187.84609690826525, 244.30780618346947),55.69219381653055)
>>> cercle.draw_circle(cercleB)
>>> cercle.draw_circle(cercle1)
>>> cercle.draw_circle(cercle2)
>>> draw_mini(cercleB,cercle1,cercle2)
>>>     cercle_petit=cercle.create(center_small_entoure(cercleA,cercleB,cercleC)[0],rayons_cercle_entoure(cercleA,cercleB,cercleC))
    
SyntaxError: unexpected indent
>>> cercle_petit=cercle.create(center_small_entoure(cercleA,cercleB,cercleC)[0],rayons_cercle_entoure(cercleA,cercleB,cercleC))
>>> cercle.draw_circle(cercle_petit)
>>> cercle_petit=cercle.create(center_small_entoure(cercle1,cercle2,cercleB)[0],rayons_cercle_entoure(cercle1,cercle2,cercleB))
>>> cercle.draw_circle(cercle_petit)
>>> cercle3 = cercle.create(pointplan.create(284.30780618346944, 300.0),55.69219381653055)
>>> cercle.draw_circle(cercle3)
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle2,cercle3)
>>> cercle_petit=cercle.create(center_small_entoure(cercle1,cercle3,cercleB)[1],rayons_cercle_entoure(cercle1,cercle3,cercleB))
>>> cercle.draw_circle(cercle_petit)
>>> cercle_petit=cercle.create(center_small_entoure(cercle1,cercle3,cercleB)[0],rayons_cercle_entoure(cercle1,cercle3,cercleB))
>>> cercle.draw_circle(cercle_petit)
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle2,cercle3)
>>> draw_mini(cercleB,cercle1,cercle2)
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle3)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 133, in draw_mini
    if point_is_in_circle(cercleC,center_small_entoure[0]):
TypeError: 'function' object is not subscriptable
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle3)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 133, in draw_mini
    if (point_is_in_circle(cercleC,center_small_entoure[0])):
TypeError: 'function' object is not subscriptable
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle3)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 133, in draw_mini
    if (point_is_in_circle(cercleC,center_c[0])):
NameError: name 'center_c' is not defined
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
((266.5594457356122, 380.6433255863265), (90.66820628996592, 117.92073901918363))
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    draw_mini(cercleB,cercle1,cercle3)
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py", line 134, in draw_mini
    if (point_is_in_circle(cercleC,center_c[0])):
NameError: name 'center_c' is not defined
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle2,cercle3)
>>> draw_mini(cercleB,cercle1,cercle2)
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle2,cercle3)
>>> draw_mini(cercleB,cercle1,cercle2)
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle2,cercle3)
>>> draw_mini(cercleB,cercle1,cercle2)
>>> x_cercle=pointplan.get_x_axis(get_center(cercle))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    x_cercle=pointplan.get_x_axis(get_center(cercle))
NameError: name 'get_center' is not defined
>>> x_cercle=pointplan.get_x_axis(pointplan.get_center(cercle))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    x_cercle=pointplan.get_x_axis(pointplan.get_center(cercle))
AttributeError: module 'module_pointPlan' has no attribute 'get_center'
>>> x_cercle=pointplan.get_x_axis(cercle.get_center(cercle))
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    x_cercle=pointplan.get_x_axis(cercle.get_center(cercle))
  File "E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\module_cercle.py", line 58, in get_center
    return cercle['center']
TypeError: 'module' object is not subscriptable
>>> test = cercle.get_center(cercleB)
>>> test
(220, 300)
>>> r_petit=(cercle.r(cercleB,3))
>>> pointplan.get_x_axis(test)
220
>>> petit_cercle=create(pointplan.create(220,300),r_petit)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    petit_cercle=create(pointplan.create(220,300),r_petit)
NameError: name 'create' is not defined
>>> petit_cercle=cercle.create(pointplan.create(220,300),r_petit)
>>> draw_mini(petit_cercle,cercle1,cercle2)
>>> draw_mini(petit_cercle,cercle3,cercle2)
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle1,cercle3)
>>> draw_mini(cercleB,cercle2,cercle3)
>>> draw_mini(cercleB,cercle2,cercle1)
>>> petit_cercle=cercle.create(pointplan.create(220,300),r_petit)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    petit_cercle=cercle.create(pointplan.create(220,300),r_petit)
NameError: name 'r_petit' is not defined
>>> test = cercle.get_center(cercleB)
>>> r_petit=(cercle.r(cercleB,3))
>>> petit_cercle=create(pointplan.create(220,300),r_petit)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    petit_cercle=create(pointplan.create(220,300),r_petit)
NameError: name 'create' is not defined
>>> petit_cercle=cercle.create(pointplan.create(220,300),r_petit)
>>> draw_mini(petit_cercle,cercle1,cercle2)
>>> draw_mini(petit_cercle,cercle3,cercle2)
>>> draw_mini(petit_cercle,cercle3,cercle1)
>>> 
 RESTART: E:\Documents\LICENCE2 INFO\S3\AP2\PROJETAP2-master\src\triplets2.py 
>>> draw_mini(cercleB,cercle1,cercle3)
{'center': (266.5594457356122, 380.6433255863265), 'radius': 26.8811085287755}
>>> draw_mini(draw_mini(cercleB,cercle1,cercle3),cercle1,cercle3)
{'center': (249.8838678780124, 351.760377491393), 'radius': 6.470047186424131}
>>> draw_mini(draw_mini(cercleB,cercle1,cercle3),draw_mini(draw_mini(cercleB,cercle1,cercle3),cercle1,cercle3),cercle3)
{'center': (258.8280339283095, 352.3072102947646), 'radius': 2.4908195378459363}
>>> draw_mini(petit_cercle,cercle3,cercle2)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    draw_mini(petit_cercle,cercle3,cercle2)
NameError: name 'petit_cercle' is not defined
>>> draw_mini(cercleB,cercle1,cercle3)
{'center': (266.5594457356122, 380.6433255863265), 'radius': 26.8811085287755}
>>> draw_mini(cercleB,cercle2,cercle3)
{'center': (266.5594457356122, 219.35667441367352), 'radius': 26.8811085287755}
>>> draw_mini(draw_mini(cercleB,cercle2,cercle3),cercle2,cercle3)
{'center': (249.8838678780124, 248.23962250860694), 'radius': 6.470047186424131}
>>> draw_mini(cercleB,draw_mini(cercleB,cercle2,cercle3),cercle3)
{'center': (303.9051447357983, 233.94183013689857), 'radius': 13.211633972620275}
>>> draw_mini(cercleB,cercle2,draw_mini(cercleB,cercle2,cercle3))
{'center': (235.2554808610542, 194.30692821903781), 'radius': 13.211633972620275}
>>> draw_mini(cercleB,cercle1,cercle3)
{'center': (266.5594457356122, 380.6433255863265), 'radius': 26.8811085287755}
>>> draw_mini(cercleB,draw_mini(cercleB,cercle1,cercle3),cercle3)
{'center': (303.9051447357983, 366.05816986310134), 'radius': 13.211633972620275}
>>> draw_mini(cercleB,cercle1,draw_mini(cercleB,cercle1,cercle3))
{'center': (235.2554808610542, 405.69307178096216), 'radius': 13.211633972620275}
>>> cercle.draw_circle(cercle1,3)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    cercle.draw_circle(cercle1,3)
TypeError: draw_circle() takes 1 positional argument but 2 were given
>>> cercle.draw_ncercles(cercle1,3)
>>> cercle.draw_ncercles(cercle2,5)
>>> cercle.draw_ncercles(cercle3,10)
>>> draw_mini(cercleB,cercle1,cercle2)
{'center': (126.88110852877556, 300.00000000000006), 'radius': 26.8811085287755}
>>> draw_mini(draw_mini(cercleB,cercle1,cercle2),cercle1,cercle2)
{'center': (160.23226424397512, 300.00000000000006), 'radius': 6.470047186424131}
>>> draw_mini(cercleB,draw_mini(cercleB,cercle1,cercle2),cercle2)
{'center': (120.83937440314743, 260.36509808213924), 'radius': 13.211633972620275}
>>> draw_mini(cercleB,cercle1,draw_mini(cercleB,cercle1,cercle2))
{'center': (120.8393744031474, 339.6349019178608), 'radius': 13.211633972620275}
>>> cercle.draw_ncercles(draw_mini(cercleB,cercle1,cercle2))
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    cercle.draw_ncercles(draw_mini(cercleB,cercle1,cercle2))
TypeError: draw_ncercles() missing 1 required positional argument: 'n'
>>> cercle.draw_ncercles(draw_mini(cercleB,cercle1,cercle2),5)
>>> 
