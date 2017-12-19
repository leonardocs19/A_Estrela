from heapq import heappush, heappop

listaAbertos = []
listaFechados = set()

class Estado:

	def __init__(self,tabuleiro,g):
		self.tabuleiro = tabuleiro
		self.g = g
		self.h = h3(self.tabuleiro)
		self.f = self.g + self.h

	def __lt__(self,O2):
		return self.f < O2.f
def h1(vetor):

	solIdeal = [1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7]
	contPecas = 0

	for i in range (16):
		if(solIdeal[i] != vetor[i]):
			contPecas = contPecas + 1

	return contPecas


def h2(tabuleiro):

	tabuleiroCaracol = [None] * 16

	contadorPecas = 0

	tabuleiroCaracol[0] = tabuleiro[0]
	tabuleiroCaracol[1] = tabuleiro[1]
	tabuleiroCaracol[2] = tabuleiro[2]
	tabuleiroCaracol[3] = tabuleiro[3]
	tabuleiroCaracol[4] = tabuleiro[7]
	tabuleiroCaracol[5] = tabuleiro[11]
	tabuleiroCaracol[6] = tabuleiro[15]
	tabuleiroCaracol[7] = tabuleiro[14]
	tabuleiroCaracol[8] = tabuleiro[13]
	tabuleiroCaracol[9] = tabuleiro[12]
	tabuleiroCaracol[10] = tabuleiro[8]
	tabuleiroCaracol[11] = tabuleiro[4]
	tabuleiroCaracol[12] = tabuleiro[5]
	tabuleiroCaracol[13] = tabuleiro[6]
	tabuleiroCaracol[14] = tabuleiro[10]
	tabuleiroCaracol[15] = tabuleiro[9]

	for i in range (1,16):
		if((tabuleiroCaracol[i] != tabuleiroCaracol[i-1]+1) and (tabuleiroCaracol[i-1]!=0)):
			contadorPecas = contadorPecas + 1
			
	return contadorPecas

def h3(vetor):

	esperado = [9,0,1,2,3,7,11,15,14,13,12,8,4,5,6,10] 

	resultado = 0

	for posZero, x in enumerate(vetor):
		zeroX = posZero // 4
		zeroY = posZero % 4

		posEsperado = esperado[x]
		posEsperadoX = posEsperado // 4
		posEsperadoY = posEsperado % 4

		resultado += abs(posEsperadoX - zeroX) + abs(posEsperadoY - zeroY)

	return resultado

def h4(vetor):

	p1 = 0.2
	p2 = 0.4
	p3 = 0.4

	return (p1*h1(vetor) + p2*h2(vetor) + p3*h3(vetor))

def h5(tabuleiro):

	return max(h1(tabuleiro), h2(tabuleiro), h3(tabuleiro))



def sucessor(vetor,g):
	posZero = vetor.index(0)

	vetoraux = vetor[:]
	ge = g + 1

	if(posZero > 3):
		aux = vetor[posZero]
		vetor[posZero] = vetor[posZero - 4]
		vetor[posZero - 4] = aux
		if not tuple(vetor) in listaFechados:
			heappush(listaAbertos, Estado(vetor,ge))

	if(posZero < 12):
		vetor = vetoraux[:]
		aux = vetor[posZero]
		vetor[posZero] = vetor[posZero + 4]
		vetor[posZero + 4] = aux

		if not tuple(vetor) in listaFechados:
			heappush(listaAbertos, Estado(vetor,ge))

	if not posZero in [0,4,8,12]:
		vetor = vetoraux[:]
		aux = vetor[posZero]
		vetor[posZero] = vetor[posZero - 1]
		vetor[posZero - 1] = aux

		if not tuple(vetor) in listaFechados:
			heappush(listaAbertos, Estado(vetor,ge))
	
	if not posZero in [3,7,11,15]:
		vetor = vetoraux[:]
		aux = vetor[posZero]
		vetor[posZero] = vetor[posZero + 1]
		vetor[posZero + 1] = aux

		if not tuple(vetor) in listaFechados:
			heappush(listaAbertos, Estado(vetor,ge))


def main ():

	tabuleiro = [int(x) for x in input().split()]

	heappush(listaAbertos, Estado(tabuleiro,0))

	while listaAbertos:
		tmp = heappop(listaAbertos)

		if(tmp.h == 0):
			print(tmp.f)
			break

		listaFechados.add(tuple(tmp.tabuleiro))

		sucessor(tmp.tabuleiro, tmp.g)

if __name__ == '__main__':
	main()
