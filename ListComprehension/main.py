file1 = open("./ListComprehension/file1.txt")
file2 = open("./ListComprehension/file2.txt")
file1_data = file1.readlines()
file2_data = file2.readlines()
result = [int(num) for num in file1_data if num in file2_data]

print(result)