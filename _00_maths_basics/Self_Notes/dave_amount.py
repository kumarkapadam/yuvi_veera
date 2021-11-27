"""
dave , laura  , owen , vick  , amr

dave  180 - 3  ===   laura  owen  vick
owen  50- 1    ===   dave
amr   150 -2  ===   vick owen
laura 360- 2  ===    amr vick

"""

list1 = ['laura', 'owen', 'vick']
for dave in list1:
    print(dave, 180 / 3)
for owen in ['dave']:
    print(owen, 50)
for amr in ['vick', 'owen']:
    print(amr, 150 / 2)
for laura in ['amr', 'vick']:
    print('laura', 360 / 2)

"""
dave = [180]
owen = [50]
amr = [150]
laura = [360]
vic = [0]

dave.append(dave[-1] - 180)
laura.append(laura[-1] + 180 / 3)
owen.append(owen[-1] + 180 / 3)
vic.append(vic[-1] + 180 / 3)

owen.append(owen[-1] - 50)
dave.append(dave[-1] + 50)

amr.append(amr[-1] - 150)
vic.append(vic[-1] + 150 / 2)
owen.append(owen[-1] + 150 / 2)

laura.append(laura[-1] - 360)
amr.append(amr[-1] + 360 / 2)
vic.append(vic[-1] + 360 / 2)

print(
    f"Dave {dave[-1]}, Laura {int(laura[-1])}, Owen {int(owen[-1])}, Vic {int(vic[-1])}, Amr {int(amr[-1])}")"""
