import matplotlib.pyplot as plt
import os


class Sprite:
    PIXEL_WEIGHT = 0.001
    def __init__(self, matrix, mass):
        self._matrix = matrix
        self._mass = mass

    def normalizeData(self):
        return

    @classmethod
    def fromFile(cls, path, threshold=0.5):
        data = plt.imread(path)
        # print(data)

        matrix = []
        mass = 0

        for y, row in enumerate(data):
            matrix.append([])
            for x, pixel in enumerate(row):
                if sum(pixel) / len(pixel) > threshold:
                    mass += cls.PIXEL_WEIGHT
                    matrix[y].append("1")
                else:
                    matrix[y].append("0")

        return cls(matrix, mass)

        # print("\n".join(map("".join, matrix)))

    @property
    def area(self) -> float:
        return len(self._matrix[0])

    @property
    def mass(self):
        return self._mass

    @property
    def coefficientOfDrag(self) -> float:
        return 1

    @property
    def data(self):
        return self._matrix

if __name__ == '__main__':
    print(Sprite.fromFile("../assets/Untitled.png"))