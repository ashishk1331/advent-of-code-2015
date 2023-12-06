from hashlib import md5 as MD5

# PART 1: find hash starting with 5 and 6 zeros for the same input
def part_one(data):
	count = 0
	while True:
		prod = MD5((data + str(count)).encode('utf-8'))
		if prod.hexdigest().startswith("000000"):
			return count
		count += 1
	return -1

# PART 2: 
def part_two(data):
	pass

def main():
	input = []

	with open("input.txt", "r") as file:
		input = file.read()

	print("Part 1:", part_one(input))
	# print("Part 2:", part_two(input))

if __name__ == '__main__':
	main()