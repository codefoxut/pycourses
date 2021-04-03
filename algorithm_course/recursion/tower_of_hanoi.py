

def hanoi(disk, source, middle, destination):

    # base case
    if disk == 0:
        print(f'Disk {disk} from {source} to {destination}')
        return

    hanoi(disk - 1, source, destination, middle)
    print(f'Disk {disk} from {source} to {destination}')
    hanoi(disk - 1, middle, source, destination)


if __name__ == '__main__':
    hanoi(4, 'A', 'B', 'C')