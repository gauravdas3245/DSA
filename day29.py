
def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(source, "->", destination)
        return

    tower_of_hanoi(n - 1, source, destination, helper)

    print(source, "->", destination)

    tower_of_hanoi(n - 1, helper, source, destination)


tower_of_hanoi(3, "A", "B", "C")
