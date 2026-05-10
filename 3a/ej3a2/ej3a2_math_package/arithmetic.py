# arithmetic.py
import math

def power(base: float, exponent: float) -> float:
	# Funció Power (potència)
	if exponent == 0:
		return "Error: L'exponent no pot ser 0."
	return base ** exponent
	pass

def square_root(num_1: float) -> float:
	# Funció square_root (Arrel quadrada)
	return math.sqrt(num_1)
	pass


