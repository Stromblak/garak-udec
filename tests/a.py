import numpy as np




arr1 = np.array([9.55,
4.78,
4.18,
7.48,
5.9,
8.1,
2.6,
3.65,
10.93,
])

arr2 = np.array([7,
13,
19,
6,
3,
4,
16,
2,
21,

])



# Min-Max normalization
min_val1 = np.min(arr1)
max_val1 = np.max(arr1)

normalized_arr1 = (arr1 - min_val1) / (max_val1 - min_val1)


# Min-Max normalization
min_val2 = np.min(arr2)
max_val2 = np.max(arr2)

normalized_arr2 = (arr2 - min_val2) / (max_val2 - min_val2)


for i in normalized_arr1:
    continue
    print(str(round(i, 2)))

for i in range(len(normalized_arr1)):
    aux = (normalized_arr1[i] + normalized_arr2[i]) / 2.0
    print(str(round(aux, 2)))