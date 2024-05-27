def generate_random_mq_forced(F, n, m):
    Fxx = PolynomialRing(F, n, 'x')
    X = Fxx.gens()
    sols = [F.random_element() for i in range(n)]
    system = []
    for i in range(m):
        poly = F.random_element()
        for i in range(n):
            for j in range(i + 1, n):
                poly += X[i] * X[j] * F.random_element()
        for i in range(n):
            poly += X[i] * F.random_element()
        system += [poly - poly(sols)]
    return system

if __name__ == "__main__":
    p = 2
    params = [[x, x] for x in [10, 20, 30, 40]] + [[x, 3*x/2] for x in [10, 20, 30, 40]] + [[x, 2*x] for x in [10, 20, 30, 40]]
    F.<a> = GF(2)
    for param in params:
        n, m = param[0], param[1]
        system = generate_random_mq_forced(F, n, m)
        print(f"Generate MQ system for {n} variables and {m} equations")
        with open(f"./systems/sage_mq_{2}_{n}_{m}", 'w') as f:
            for poly in system:
                f.write(f"{poly}\n")