def get_next_position(current, move):
	if move == "<":
		current[0] -= 1
	elif move == ">":
		current[0] += 1
	elif move == "^":
		current[1] += 1
	elif move == "v":
		current[1] -= 1
	return current

# PART 1: count number of houses with atleast 1 delieverd present
def part_one(data):
	position = [0, 0]
	delivered = set([tuple(position)])
	for move in data:
		position = get_next_position(position, move)

		delivered.add(tuple(position))
	return len(delivered)

# PART 2: santa and robo santa takes turn for instructions
def part_two(data):
	spos, rpos = [0, 0], [0, 0]
	sdel, rdel = set([tuple(spos)]), set([tuple(rpos)])
	for ind, move in enumerate(data):
		if ind%2:
			spos = get_next_position(spos, move)
			sdel.add(tuple(spos))
		else:
			rpos = get_next_position(rpos, move)
			rdel.add(tuple(rpos))
	return len(sdel.union(rdel))

def main():
	input = []

	with open("input.txt", "r") as file:
		input = file.read()

	print("Part 1:", part_one(input))
	print("Part 2:", part_two(input))

if __name__ == '__main__':
	main()