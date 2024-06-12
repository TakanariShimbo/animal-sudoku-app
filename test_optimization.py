import numpy as np

from optimization import Optimizer, Table


init_number_array = np.array(
    [
        [0, 8, 0, 4, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 1, 3, 0],
        [0, 0, 1, 7, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 5, 0, 0],
        [7, 0, 5, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 3],
        [5, 2, 0, 3, 0, 0, 0, 7, 6],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
    ],
    dtype=int,
)
init_table = Table(number_array=init_number_array)
optimizer = Optimizer(table=init_table, seed=123)
result_table = optimizer.run()

print("-------- Probrem --------")
print(init_table.get_number_df())

print("-------- Solution --------")
if result_table:
    print(result_table.get_number_df())
else:
    print("Not found")
