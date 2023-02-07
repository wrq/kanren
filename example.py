from kanren import eq, lall, lany, run, vars

observations = [(0, 1), (1, 0)]

def generate(pixels):
    pairs = [(a, b) for a, b in zip(pixels[:-1], pixels[1:])]
    return lall(
        *[lany(*[eq(obs, pair) for obs in observations]) for pair in pairs]
    )

N = 10
pixels = vars(N)
res = run(1, pixels, generate(pixels))