
def fibonachi(numb):
	prev_numb, last_numb = 0, 1
	for x in range(numb):
		prev_numb, last_numb = last_numb, prev_numb+last_numb
	print (last_numb)
	return numb


def f(n , key,*args):
	if not args:
		res = 0
		for numb in n:
		 if res < key(numb):
		     res = numb
	         
		return res
	else:
	 res = n 
	 for numb in args:
	     if res < numb:
	         res = numb
	 return res