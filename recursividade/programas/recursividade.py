#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
recursividade.py

Exemplos de funções e programas recursivos.

Created by Ernesto Costa on 2008-11-15.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

def deriva(f,x):
	pass
	
# potência

def pot_op(x,n):
	if n==0:
		return 1
	else:
		factor=pot_op(x,n/2)
		if (n%2 == 0):
			return factor * factor
		else:
			return factor * factor * x	

# problema 5.5
def sobe_e_desce(n):
	if n == 1:
		return [1]
	else:
		return [n] + sobe_e_desce(n-1) + [n]

# problema 5.6

def somat(n):
	if n == 1:
		return 1
	else:
		return n + somat(n-1)

def varios_somat(m):
	for i in range(1,m+1):
		print(somat(i))


# problema 5.7

def remove_dup(cad):
	if len(cad) == 1:
		return cad
	elif cad[0]== cad[1]:
		return cad[0] + remove_dup(cad[2:])
	else:
		return cad[0] + remove_dup(cad[1:])

# entremear duas listas. Os tamanhos podem ser diferentes
# - versão simples
def inter(l1,l2):
	if l1 == []:
		return l2
	elif l2 == []:
		return l1
	else:
		return [l1[0],l2[0]] + inter(l1[1:],l2[1:])
		
# versão completa		
def inter_all(l1,l2,aux=[]):
	if l1 == []:
		return [aux + l2]
	if l2 == []:
		return [aux + l1]
	return inter_all(l1[1:], l2, aux+[l1[0]]) + inter_all(l1, l2[1:], aux + [l2[0]])


def inter_all_2(l1,l2):
	if l1 == []:
		return [l2]
	elif l2 == []:
		return [l1]
	else:
		aux1= [[l1[0]] + temp for temp in inter_all_2(l1[1:], l2)]
		aux2= [[l2[0]] + temp for temp in inter_all_2(l1, l2[1:])]
		return  aux1 + aux2 

### ÁRVORES BINÁRIAS
# construção de uma árvore binária de procura
# dado um pivot todos os elementos da sud-árvoreesquerda são menores
# os da sub-árvoredireita são maiores
# não admite elementos repetidos

def arv_bin_proc(lista):
	if lista == []:
		return lista
	else:
		pivot=lista[0]
		esq= [elem for elem in lista if elem < pivot]
		dir= [elem for elem in lista if elem > pivot]
		return [arv_bin_proc(esq)] + [pivot] + [arv_bin_proc(dir)]
		
def procura_abp(elem, abp):
	if abp == []:
		return False
	elif abp[1] == elem:
		return True
	elif abp[1] < elem:
		return procura_abp(elem,abp[2])
	else:
		return procura_abp(elem,abp[0])	


def procura_abp_v1(elem, abp):
	if abp == []:
		return False,abp
	elif abp[1] == elem:
		return True,abp
	elif abp[1] < elem:
		return procura_abp_v1(elem,abp[2])
	else:
		return procura_abp_v1(elem,abp[0])	

def insere_abp(elem,abp):
	if not procura_abp(elem,abp):
		return insere_abp_aux(elem,abp)
	else:
		return abp

def insere_abp_aux(elem,abp):
	if abp == []:
		return [[],elem,[]]	
	elif elem < abp[1]:
		return [insere_abp_aux(elem, abp[0]), abp[1],abp[2]]
	else:
		return [abp[0],abp[1],insere_abp_aux(elem, abp[2])]

def travessia_in(abp):
	if abp==[]:
		return []
	else:
		return travessia_in(abp[0]) + [abp[1]] + travessia_in(abp[2]) 

def travessia_pre(abp):
	if abp==[]:
		return []
	else:
		return [abp[1]] + travessia_pre(abp[0]) + travessia_pre(abp[2])

def travessia_post(abp):
	if abp==[]:
		return []
	else:
		return travessia_post(abp[0]) + travessia_post(abp[2]) + [abp[1]] 
		
		
def imprime_abp(abp,nivel):
	if abp == []:
		pass
	else:
		print(' ' * nivel,abp[1])
		imprime_abp(abp[0],nivel-2)
		print(' '* nivel, end=' ')
		imprime_abp(abp[2],nivel+2)
		
		
def main():
	#print inter([1,2,6,7],[3,4,5])
	#print inter_all([1,2],[3,4])
	#print inter_all_2([1,2],[3,4])
	abp= arv_bin_proc([4,7,1,3,9,8,2,5,6])
	print(abp)
	print(procura_abp(10,abp))
	print(procura_abp_v1(6,abp))
	print(insere_abp(10,abp))
	print('IN')
	print(travessia_in(abp))
	print('PRE')
	print(travessia_pre(abp))
	print('POST')
	print(travessia_post(abp))
	#print pot_op(2,10)



if __name__ == '__main__':
	main()

