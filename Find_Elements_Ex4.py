def FindEl(input_list, val):
    occ_val = []
    for index, value in enumerate(input_list):
        if value == val:
            occ_val.append([index])
        elif isinstance(input_list[index], list):
            for f in FindEl(input_list[index], val):
                occ_val.append([index] + f)
    return occ_val

example = [[[1,2,3],2,[1,3]],[1,2,3]]
print(FindEl(example, 2))
print(FindEl(example, [1,2,3]))