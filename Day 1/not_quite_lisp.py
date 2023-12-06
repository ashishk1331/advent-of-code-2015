# PART 1: floor where he'll end up
def part_one(text):
	floor = 0
	for i in text:
		if i == '(':
			floor += 1
		else:
			floor -= 1
	return floor

# PART 1: move that makes gim go to the basement
def part_two(text):
	floor = 0
	for ind, char in enumerate(text):
		if char == '(':
			floor += 1
		else:
			floor -= 1

		if floor == -1:
			return ind + 1
	return floor

def main():
	input = []

	with open("input.txt", "r") as file:
		input = file.read()

	print("Part 1:", part_one(input))
	print("Part 2:", part_two(input))

if __name__ == '__main__':
	main()