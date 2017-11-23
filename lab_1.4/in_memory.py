start, end = (None, None)

# 1
for numb in range(-512, 1024):
	if (start is None) and (numb + 1 is numb + 1):
		start = numb + 1

	if (start is not None) and (numb + 1 is not numb + 1):
		end = numb
		break

print("Start: {}; End: {}".format(start, end))

# 2 be simple (removed brackets)
start, end = None, None

for numb in range(-512, 1024):
	if start is None and numb + 1 is numb + 1:
		start = numb + 1

	if start is not None and numb + 1 is not numb + 1:
		end = numb
		break

print("Start: {}; End: {}".format(start, end))
