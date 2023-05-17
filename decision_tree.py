import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Relative file path for dataset
file_path = './assets/data/Triyaj.xls'

# Read the XLS file
data_set = pd.read_excel(file_path, sheet_name=3)

# multiply data
copies = 25
rows_to_copy = [data_set] * copies
data_set = pd.concat(rows_to_copy, ignore_index=True)

# Convert "BELİRTİ AD" column to categorical values using LabelEncoder
label_encoder = LabelEncoder()
label_values = data_set['BELİRTİ AD'].unique()
label_encoder.fit(label_values)
data_set["BELİRTİ_SAYISAL"] = label_encoder.transform(data_set["BELİRTİ AD"])

# Remove rows with 0.0 in a specific column
data_set = data_set[data_set['GÖZLENME SIKLIĞI'] > 0.1]

# Add new columns to increase diversity
data_set['BELİRTİ_GÖZLENME'] = data_set['BELİRTİ_SAYISAL'] * \
    data_set['GÖZLENME SIKLIĞI']


data_set['BELİRTİ_GÖZLENME1'] = data_set['BELİRTİ_SAYISAL'] / \
    data_set['GÖZLENME SIKLIĞI']


# Decision tree algorithm implementation
# Separating data
X = data_set.iloc[:, 2:7]  # input values
Y = data_set.iloc[:, 0]  # output, target values

# Split data as train and test
# Test data will be 30% percent of the data and it will be selected randomly
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.30)

# Create a decision tree classifier
clf_entropy = DecisionTreeClassifier(
    criterion="entropy", max_depth=12, min_samples_leaf=10)

# Train the decision tree model on the provided training data
clf_entropy.fit(X_train, Y_train)

# Make prediction
Y_prediction = clf_entropy.predict(X_test)

# Display prediction accuracy
ac_score = accuracy_score(Y_test, Y_prediction) * 100
print("Accuracy of prediction is : ", ac_score)
