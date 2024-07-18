# import configparser

# config = configparser.ConfigParser()

# config.read('configtxt.txt')

def read_config(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip()  # Đọc dòng đầu tiên và loại bỏ khoảng trắng
        values = [value.strip() for value in line.split(',')]  # Tách các giá trị và loại bỏ khoảng trắng
    return values

# Đọc tệp cấu hình
config_values = read_config('configtxt.txt')

# # In ra các giá trị để kiểm tra
# for i, value in enumerate(config_values, start=1):
#     print(f"Value {i}: {value}")
# Kiểm tra xem danh sách có đủ 3 giá trị hay không và in ra giá trị thứ ba
if len(config_values) >= 3:
    print(f"Value 3: {config_values[2]}")
else:
    print("The list does not contain enough values.")