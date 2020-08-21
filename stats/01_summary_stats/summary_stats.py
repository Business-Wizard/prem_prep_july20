def mean(lst):
    return sum(lst) / len(lst)

# # using the accumulator pattern
# def mean(lst):
#     accum = 0
#     for num in lst:
#         accum += num

#     return accum / len(lst)

# lst1 = [1,2,3,4,5,6,7,8,9]
# print(mean(lst1))

# urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
# farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

# print('urban:', mean(urban))
# print('farmhouse:', mean(farmhouse))

# # print(sorted(urban))
# # print(sorted(urban)[1:-1])
# # print(sorted(farmhouse)[1:-1])
# print('urban:', mean(sorted(urban)[1:len(urban)-1]))
# print('farmhouse:', mean(sorted(farmhouse)[1:len(farmhouse)-1]))



'''Median'''

lst1 = 13, 18, 13, 14, 13, 16, 14, 21, 13
lst2 = 15, 14, 10, 8, 12, 8, 16, 13

# sort list
lst1_sorted = sorted(lst1)
lst2_sorted = sorted(lst2)

# print(lst1_sorted)
# print(lst2_sorted)

def median(lst):
    lst_sorted = sorted(lst)
    
    if len(lst) % 2 == 1:
        median_idx = int(len(lst) / 2)
        return lst_sorted[median_idx]
    else:
        higher_mid = lst_sorted[int(len(lst)/2)]
        lower_mid = lst_sorted[int(len(lst)/2)-1]

        return (higher_mid + lower_mid) / 2

# print(median(lst1))
# print(median(lst2))
    

urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0]


# print(median(urban))
# print(median(farmhouse))


# house_values = [500000, 125000, 36000, 70000, 650000, 3400000, 560000]

# print(sorted(house_values))
# print('mean ', mean(house_values) )
# print('median ', median(house_values) )


''' Mode '''

def mode(lst):
    most_occurring = lst[0]

    for item in lst[1:]:
        if lst.count(item) > lst.count(most_occurring):
            most_occurring = item

    return most_occurring

mode_lst = ['cat', 'dog', 'bear', 'bear', 'bear', 'bear', 'bear', 'cat', 'cat', 'cat', 'cat', 'cat', 'dog']

# print(mode(mode_lst))



''' Five Number Summary, IQR, Qualifying Outliers '''
def five_num_summary(lst):
    min_ = min(lst)
    max_ = max(lst)
    med = median(lst)

    if len(lst) % 2 == 1:
        move_mid_idx_by = 1
    else:
        move_mid_idx_by = 0

    sorted_lst = sorted(lst)
    lst_low = sorted(lst)[0:int(len(lst)/2)]
    q1 = median(lst_low)

    lst_high = sorted(lst)[int(len(lst)/2)+move_mid_idx_by: ]
    q3 = median(lst_high)

    print(f'list low: {lst_low}')
    print(f'list high: {lst_high}')

    return min_, q1, med, q3, max_

b = [6,1,4,51,7,16,10,14,46,22,24,56,48,54]
a = [15,2,9,5,6,7,27,12,18,19,1]

print(five_num_summary(b))

house_values = [-6000000, 450000, 652234, 89000, 750000, 224968, 500000, 125000, 36000, 70000, 650000, 3400000, 560000]

# print(five_number_summary(house_values))

def iqr(lst):
    _, q1, _, q3, _ = five_number_summary(lst)
    return q3 - q1

# print(iqr(house_values))

def detect_outliers(lst):
    _, q1, _, q3, _ = five_number_summary(lst)
    iqr_ = iqr(lst)

    outliers = []

    for item in lst:
        if item < q1 - 1.5*iqr_:
            outliers.append(item)
        if item > q3 + 1.5*iqr_:
            outliers.append(item)
    return outliers

# print(detect_outliers(house_values))

a = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]
a_trimmed = list(set(a) - set(detect_outliers(a)))

# print(a)
# print(a_trimmed)
# print(five_number_summary(a))
# print(iqr(a))
# print(detect_outliers(a))
# print(five_number_summary(a_trimmed))
# print(mean(a_trimmed))


''' Breakout '''

# a = [18, 15, 7, 27, 2, 9, 12, 1, 6, 19, 5]

# print(five_number_summary(a))

# print(iqr(a))

# print(detect_outliers(a))

# print(sorted(a))
# print(mean(a))
# print(median(a))


''' Variance '''

def variance(lst, sample=True):
    total = 0
    mean_ = mean(lst)

    for item in lst:
        total += (item - mean_)**2

    if sample:
        return total / (len(lst) - 1)
    else:
        return total / len(lst)
a = [1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27]

a_var_pop = variance(a, sample=False)
a_var_samp = variance(a, sample=True)

print(sorted(a))
print(a_var_pop)
print(a_var_samp)

''' standard deviation '''

def stdev(lst, sample=True):
    return variance(lst, sample)**(1/2)

a_sd_pop = stdev(a, sample=False)
a_sd_samp = stdev(a, sample=True)


print(a_sd_pop)
print(a_sd_samp)
