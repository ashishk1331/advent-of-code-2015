# PART 1: summation of wrapping paper required
def part_one(data):
	paper = 0
	for box in data:
		l, w, h = tuple(map(int, box.split("x")))
		extra = sorted([l, w, h])[:2]
		total = 2*(w*(l+h) + l*h) + extra[0]*extra[1]
		paper += total
	return paper

# PART 2: length of ribbon required
def part_two(data):
	length = 0
	for box in data:
		l, w, h = tuple(map(int, box.split("x")))
		small = sorted([l, w, h])[:2]
		length += 2*(small[0] + small[1]) + l*w*h
	return length

def main():
	input = []

	with open("input.txt", "r") as file:
		input = file.read().split("\n")

	print("Part 1:", part_one(input))
	print("Part 2:", part_two(input))

if __name__ == '__main__':
	main()