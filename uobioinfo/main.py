import argparse


def say_something(phrase): # ... I'm giving up on you. 
    """Change this however you'd like!"""
    print(phrase)


# --- Don't change anything below this line -------


def cli():
    """Command line interface"""
    parser = argparse.ArgumentParser(
        description="Demo for bioinformatics and genomics program at UO.")
    parser.add_argument('phrase', help="What should I say?")
    args = parser.parse_args()
    main(args.phrase)


def main(phrase):
    """Main function to execute"""
    print("\nHello, Bioinformatics and genomics program at UO:")
    say_something(phrase)
    print("\n")
	print("My contribution here")


if __name__ == "__main__":
    main("Hello, World!")
