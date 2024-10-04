def moveTower(height, SP, MP, EP):
    if height >= 1:
        moveTower(height - 1, SP, EP, MP)
        moveDisk(height, SP, EP)
        moveTower(height - 1, MP, SP, EP)


def moveDisk(disk, sp, ep):
    print(f"move disk[{disk}] from {sp} to {ep}")


if __name__ == "__main__":
    moveTower(25, "#1", "#2", "#3")
