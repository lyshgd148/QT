from big_o import big_o, datagen

best, others = big_o(
    sorted,
    lambda n: datagen.integers(n, 10000, 50000),
    min_n=10000,
    max_n=100000,
    n_measures=1000,
)
print(best)
