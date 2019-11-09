import csv

temp_arr = []
with open("input.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row, row["MaSP"])
        # for k, v in row.items():
        #     print(temp_dict)
        #     if k not in temp_dict.keys():
        #         temp_dict[k] = v
        #     else:
        #         temp_dict[k] = temp_dict.get(k, 0) + v if type(v) == "int" else str(v)
        #     print(temp_dict)
        # temp_arr.append(temp_dict)
        if row not in temp_arr:
            temp_arr.append(row)
print(temp_arr, len(temp_arr))
