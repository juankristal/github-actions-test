def add_1(x):
	return x + 1

def test_answer():
	assert add_1(1) == 2

def test_fail():
	assert add_1(5) == 2