fractal = []


def create_fractal():
    fractal = [0, [], [], 2]
    fractal[1] = fractal
    fractal[2] = fractal


if __name__ == "__main__":
    create_fractal()
    print(fractal)
