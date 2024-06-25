import csv
from collections import defaultdict

def process_csv(file_path):
    # Initialize a dictionary to store data based on Killcount
    KillCount_dict = defaultdict(list)
    
    
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV
        for row in reader:
            KillCount = row["KillCount"]
            
            data = [row["Date"], row["Item"], row["Drop_Quantity"], row["Drop_Price"]]
           
            KillCount_dict[KillCount].append(data)
    
    return KillCount_dict


file_path = 'C:\\Users\\nvkid\\OneDrive\\Desktop\\Data Science Project\\CSV Outputs\\Vorkath.csv'
KillCount_data = process_csv(file_path)


for KillCount, data in KillCount_data.items():
    print(f"Killcount: {KillCount}")
    for entry in data:
        print(entry)
        

def calculate_total_drop_value(killcount_data):
    total_values = {}
    
    for killcount, entries in killcount_data.items():
        total_value = 0.0
        
        for entry in entries:
            drop_quantity = int(entry[2])  
            drop_price = float(entry[3])
            total_value += drop_price * drop_quantity
        
        total_values[killcount] = total_value
    
    return total_values


def aggregate_entries_with_total(killcount_data, total_values):
    aggregated_data = []
    
    for killcount, entries in killcount_data.items():
        total_value = total_values[killcount]
        
        if entries:
            date = entries[0][0] 
            aggregated_data.append([killcount, date, total_value])
    
    return aggregated_data


total_values = calculate_total_drop_value(KillCount_data)
aggregated_data = aggregate_entries_with_total(KillCount_data, total_values)


for entry in aggregated_data:
    print(f"Killcount: {entry[0]}, Date: {entry[1]}, Total Drop Value: {entry[2]:.2f}")
    
def export_to_csv(aggregated_data, output_file_path):
    # Define the header
    header = ["Killcount", "Date", "Total Drop Value"]
    
    # Open the output file and write the data
    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(aggregated_data)


output_file_path = 'aggregated_data.csv'

killcount_data = process_csv(file_path)
total_values = calculate_total_drop_value(killcount_data)
aggregated_data = aggregate_entries_with_total(killcount_data, total_values)
export_to_csv(aggregated_data, output_file_path)

# Print a message to confirm the data has been exported
print(f"Aggregated data has been exported to {output_file_path}")