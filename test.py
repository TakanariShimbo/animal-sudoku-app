import pandas as pd

from optimization import OrtoolOptimizer, Consts

fixed_numbers_data = [
    [0, 8, 0, 4, 0, 0, 0, 9, 0],
    [0, 6, 0, 0, 0, 0, 1, 3, 0],
    [0, 0, 1, 7, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 5, 0, 0],
    [7, 0, 5, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 3],
    [5, 2, 0, 3, 0, 0, 0, 7, 6],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
]
fixed_numbers_df = pd.DataFrame(data=fixed_numbers_data, dtype=int)

consts = Consts(fixed_numbers_df=fixed_numbers_df)

optimizer = OrtoolOptimizer(consts=consts)
result_numbers_df = optimizer.run()

print("-------- Probrem --------")
print(consts.fixed_numbers_df)

print("-------- Solution --------")
print(result_numbers_df)
