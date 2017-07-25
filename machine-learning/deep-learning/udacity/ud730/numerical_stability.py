#big_num = 10**9
big_num = 1
small_num = 10**-6
#total_sum = 10**9
total_sum = 1
for _ in range(10**6):
    total_sum += small_num
total_sum -= big_num
print("total sum ", total_sum)