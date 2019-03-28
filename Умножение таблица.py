# -*- coding: cp1251 -*-
hom = float(raw_input('Bведите число для, которого нужна таблица умножения: '))
hom1 = float(raw_input('До какого множителя вы хотите дойти: '))
print "Вот ваша таблица"
i = 1
for i in range(int(hom1 + 1)):
    print hom, '*', '\t', i, ' = ', '\t', hom * i
    i = i + 1
    
    
    
