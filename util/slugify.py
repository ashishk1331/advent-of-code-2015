def slugify(s):
	return "".join(filter(lambda x: x.isalnum() or x.isspace(), s.strip().lower())).replace(" ", "_")

def main():
	string = """
		Doesn't He Have Intern-Elves For This?
	"""
	print(slugify(string))

if __name__ == '__main__':
	main()