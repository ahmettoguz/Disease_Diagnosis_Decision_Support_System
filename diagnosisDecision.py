import pandas as pd

file_path = './assets/data/Triyaj.xls'

# Read the XLS file
data_frame = pd.read_excel(file_path, sheet_name=3)

# Print the contents of the XLS file
print(data_frame)
