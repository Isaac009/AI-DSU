# # Matrices manipulations
# import numpy as np
# # Manage and process the user input file
# import json
# # Parser for command-line options, arguments and sub-commands
# import argparse
# # Maths operations
# import math
# # Functions creating iterators for efficient looping
# import itertools


# # 'X': unknown
# # '*': black
# # ' ': white
# DISPLAY_CHARACTERS = ['X', '*', ' ']

# class NonogramSolver(object):
# 	def __init__(self, input_file_path):
# 		self.marks = []
# 		with open(input_file_path, 'r') as f:
# 			self.marks = json.load(f)
# 		self._verbose = False
# 		self.__print(self.marks)

# 		self.RC = len(self.marks['r'])
# 		self.CC = len(self.marks['c'])

# 		self.NONO_MATRIX = np.zeros((self.RC, self.CC), dtype=np.int)

# 	def __str__(self):
# 		return '\n'.join([''.join([DISPLAY_CHARACTERS[c] for c in r]) for r in self.NONO_MATRIX])

# 	# def set_verbose(self, verbose):
# 	# 	self._verbose = verbose

# 	'''
# 	row solving algorithm:
# 	generate all combinations that doesn't violate previously found cells
# 	for each possible combination mark common cells
# 	return result of common cells as new solution row

# 	@param ar: Array an array of count of consecutive black marks
# 	@param ref: int current solution for this row
# 	@return Array yielded possible combination of marks starting and ending with num of empty
# 	'''
# 	@staticmethod
# 	def solve_row(ar, ref):
# 		if np.sum(ref == 0) == 0:
# 			return ref
# 		N = len(ref)
# 		K = N - sum(ar)
# 		res_ar = False
# 		for comb in itertools.combinations(range(0, K+1), len(ar)):
# 			# print(comb)
# 			c_ar = [0] + list(comb) + [K] # combination position array
# 			w_ar = [c_ar[i+1]-c_ar[i] for i in range(len(c_ar)-1)] # zero count array

# 			w_ar = [[2]*x for x in w_ar] # white int array
# 			b_ar = [[1]*x for x in ar] # black int array

# 			for i,v in enumerate(b_ar): # merge two string arrays to generate possible placement
# 				w_ar.insert(2*i+1, v)

# 			res = [x for r in w_ar for x in r]
# 			match = True
# 			for i in range(N):
# 				if ref[i] == 0 or ref[i] == res[i]:
# 					continue
# 				match = False
# 				break
# 			if not match:
# 				continue
# 			if not res_ar:
# 				res_ar = res
# 				continue
# 			for i in range(N):
# 				if res_ar[i] != res[i]:
# 					res_ar[i] = 0
# 		return np.array(res_ar)


# 	'''
# 	@param ar: Array an array of consecutive black marks
# 	@param N: int total of
# 	@return int number of possible combination of marks
# 	'''
# 	# @staticmethod
# 	# def get_probs_count(ar, N):
# 	# 	N -= sum(ar) - 1
# 	# 	R = len(ar)
# 	# 	f = math.factorial
# 	# 	return f(N)/f(N-R)/f(R)

# 	# def __print(self, *args, **kwargs):
# 	# 	if self._verbose:
# 	# 		print(*args, **kwargs)

# 	'''
# 	Algorithm is very simple:
# 	repeat until all cells are solved:
# 		turn every column and row into rows
# 		solve for generated row
# 		update result matrix
# 	@param self
# 	'''
# 	def solve(self):
# 		pass_cnt = 1
# 		while np.sum(self.NONO_MATRIX == 0) != 0:
# 			self.__print('Pass:', pass_cnt)
# 			#add check if get any improvements
# 			for i, r in enumerate(self.marks['r']):
# 				self.NONO_MATRIX[i, :] = NonogramSolver.solve_row(r, self.NONO_MATRIX[i])
# 			# pass cols
# 			for j, c in enumerate(self.marks['c']):
# 				self.NONO_MATRIX[:, j] = NonogramSolver.solve_row(c, self.NONO_MATRIX[:, j])
# 			self.__print(self)
# 			pass_cnt += 1


# def solve(input_file_path):
# 	return NonogramSolver(input_file_path).solve()

# if __name__ == '__main__':
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument('-f', '--file', required=True, help='nongram file in json format')
# 	args = parser.parse_args()

# 	solver = NonogramSolver(args.file)
# 	solver.solve()
# 	print(solver)


# Matrices manipulations
import numpy as np
# Manage and process the user input file
import json
# Parser for command-line options, arguments and sub-commands
import argparse
# Maths operations
import math
# Functions creating iterators for efficient looping
import itertools


# 'X': unknown
# '*': black
# ' ': white
DISPLAY_CHARACTERS = ['X', '*', ' ']

class NonogramSolver(object):
	def __init__(self, input_file_path):
		self.marks = []
		with open(input_file_path, 'r') as f:
			self.marks = json.load(f)
		self.RC = len(self.marks['r'])
		self.CC = len(self.marks['c'])

		self.NONO_MATRIX = np.zeros((self.RC, self.CC), dtype=np.int)

	def __str__(self):
		return '\n'.join([''.join([DISPLAY_CHARACTERS[c] for c in r]) for r in self.NONO_MATRIX])

	@staticmethod
	def solve_row(input_array, ref):
		if np.sum(ref == 0) == 0:
			return ref
		N = len(ref)
		K = N - sum(input_array)
		res_ar = False
		for comb in itertools.combinations(range(0, K+1), len(input_array)):
			combination_array = [0] + list(comb) + [K]
			white_array = [combination_array[i+1]-combination_array[i] for i in range(len(combination_array)-1)]

			white_array = [[2]*x for x in white_array]
			b_ar = [[1]*x for x in input_array]

			for i,v in enumerate(b_ar):
				white_array.insert(2*i+1, v)

			res = [x for r in white_array for x in r]
			match = True
			for i in range(N):
				if ref[i] == 0 or ref[i] == res[i]:
					continue
				match = False
				break
			if not match:
				continue
			if not res_ar:
				res_ar = res
				continue
			for i in range(N):
				if res_ar[i] != res[i]:
					res_ar[i] = 0
		return np.array(res_ar)

	def solve(self):
		while np.sum(self.NONO_MATRIX == 0) != 0:
			for i, r in enumerate(self.marks['r']):
				self.NONO_MATRIX[i, :] = NonogramSolver.solve_row(r, self.NONO_MATRIX[i])
			for j, c in enumerate(self.marks['c']):
				self.NONO_MATRIX[:, j] = NonogramSolver.solve_row(c, self.NONO_MATRIX[:, j])


def solve(input_file_path):
	return NonogramSolver(input_file_path).solve()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', required=True, help='Nonogram user input file in json format')
	args = parser.parse_args()

	nono_solution = NonogramSolver(args.file)
	nono_solution.solve()
	print(nono_solution)

