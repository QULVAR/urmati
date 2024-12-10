from .urmatiSR import urmatiSR
from .urmatiKR import urmatiKR

#SR
#u = '+1*uxx +2*uxy +2*uyy +4*uyz +5*uzz +1*ux +1*uy'
#u = '+2*uxx +2*uxy +1*uyy +2*uxz +2*uz -3*u'
#matrixInp = '1 -3/2 0?0 1/2 2**0.5?0 0 1'
#matrixInp = '1 1 0?1 0 1?0 0 1'

def urmati(u, matrixInp, mode):
	if mode == 'SR':
		return urmatiSR(u, matrixInp)
	elif mode == 'KR':
		return urmatiKR(u)
	else:
		return 'No such number'