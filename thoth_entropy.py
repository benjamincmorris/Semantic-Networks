import sys
import thoth.thoth as thoth

def main():
	counts = sys.argv[1:]
	results = thoth.calc_entropy([int(count) for count in counts], 100000)
	print(results)

if __name__ == "__main__":
  main()
