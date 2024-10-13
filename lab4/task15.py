def create_fractal():
    original_list = [1, 2]
    fractal_ = [0] + original_list * 2 + [2]
    return fractal_


fractal = create_fractal()

if __name__ == "__main__":
    print(fractal)
