import csv

# Your list of data
data_list = [
    ['John', 30, 'Engineer'],
    ['Jane', 28, 'Designer'],
    ['Bob', 35, 'Manager'],
]

result = list(zip(a, b, c))

# Print the result
for row in result:
    print(row)


# Specify the CSV file path
csv_file_path = 'file.csv'  # Replace this with your desired file path

# Write the data to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write each row in the list to the CSV file
    for row in data_list:
        csv_writer.writerow(row)

print(f'Data has been written to {csv_file_path}')
