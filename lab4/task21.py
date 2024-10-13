def defractalize(fractal):
    while fractal.count(fractal) > 0:
        fractal.remove(fractal)


if __name__ == "__main__":
    fractal = [2, 5]
    fractal.append(fractal)
    fractal.append(3)
    defractalize(fractal)
    print(fractal)
