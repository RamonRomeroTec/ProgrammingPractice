_len = int(input())
word = [x for x in input()]
my_dict = dict(A=0, C=0, G=0, T=0)
qmarks = 0


def get_max():
	global my_dict
	_max = 0
	for x in my_dict:
		if my_dict[x] > _max:
			_max = my_dict[x]
	if _max == 0:
		return 1
	return _max

def all_equal():
	global my_dict
	a = my_dict['A']
	for x in my_dict:
		if a != my_dict[x]:
			return False
	return True

def get_letter():
	global my_dict
	for key in my_dict:
		if my_dict[key] < get_max():
			my_dict[key] += 1
			return key
	if all_equal():
		my_dict[key] += 1
		return key
	print("===")
	exit()

for x in word:
	if x not in my_dict:
		qmarks += 1
	else:
		my_dict[x] += 1

for x in range(_len):
	if word[x] == '?':
		word[x] = get_letter()
		if word[x] == None:
			set_trace()
out = "".join(word)

if len(set(out)) == 4 and len(out)%4 == 0:
	print("".join(word))
else:
	print("===")
		
