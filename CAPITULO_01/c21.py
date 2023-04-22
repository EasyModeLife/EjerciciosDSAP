"""C-1.21 Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D)."""

if __name__ == "__main__":
    output = []
    fp = open('texto.txt')
    for line in fp:
        try:
            input()
            output.append(line)
        except EOFError:
            break
    print(output)
