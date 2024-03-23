import numpy as np

arr = np.array([12, 4, 7, 2, 13, 7, 3, 21, 7, 19, 4, 9, 3, 7, 3, 6])

# Min-Max normalization
min_val = np.min(arr)
max_val = np.max(arr)

normalized_arr = (arr - min_val) / (max_val - min_val)

print("Normalized array:", normalized_arr + 0.0)

