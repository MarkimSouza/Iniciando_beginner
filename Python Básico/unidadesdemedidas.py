m = float (input('Digite uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100 
mm = m * 1000
print ('conversões de {:.0f}m para as seguintes unidades de medidas:'.format(m))
print ('Km = {:.3f}km'.format (km))
print ('Hm = {:.2f}hm'.format(hm))
print ('Dam = {:.1f}dam'.format(dam))
print ('Dm = {:.0f}dm'.format(dm))
print('Cm = {:.0f}cm'.format(cm))
print ('mm = {:.0f}mm'.format(mm))

