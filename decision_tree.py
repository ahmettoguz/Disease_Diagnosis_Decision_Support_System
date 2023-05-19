import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="assets/html")


@app.route('/diagnosis', methods=['GET'])
def diagnosis():

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
    data_set["BELİRTİ_SAYISAL"] = label_encoder.transform(
        data_set["BELİRTİ AD"])

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
    # print("Accuracy of prediction is : ", ac_score)

    # Get user symptom and create dataframe as similar to used in test and train
    multiple_predictons = list()

    user_symptom = request.args.get('symptom')
    # user_symptom = "baş ağrısı,ateş,bel ağrısı"
    try:
        user_symptoms = user_symptom.split(",")
    except AttributeError:
        return jsonify({'success': 'false', 'error': 'No sympton.'})

    for symptom in user_symptoms:
        user_predictions_list = list()
        try:
            user_symptom_int = data_set.loc[data_set['BELİRTİ AD']
                                            == symptom, 'BELİRTİ_SAYISAL'].iloc[0]
        except IndexError:
            return jsonify({'success': 'false', 'error': 'Enter valid sympton.'})

        for i in range(7, 10):
            user_symptom_df = {'GÖZLENME SIKLIĞI': [(i / 10)],
                               'BELİRTİ_SAYISAL': [user_symptom_int],
                               'BELİRTİ_GÖZLENME': [((i / 10) * user_symptom_int)],
                               'BELİRTİ_GÖZLENME1': [((i / 10) + user_symptom_int)]
                               }

            user_symptom_df = pd.DataFrame(user_symptom_df)

            # Make prediction for user
            user_prediction = clf_entropy.predict(user_symptom_df)
            user_predictions_list.append(user_prediction[0])

        multiple_predictons.append(user_predictions_list)

    # get common disease by merging
    merged_list = [item for sublist in multiple_predictons for item in sublist]

    # Create a dictionary to store the frequency of elements
    frequency_dict = {}
    for item in merged_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    # Sort frequency dictionary
    sorted_freq = sorted(frequency_dict.items(),
                         key=lambda x: x[1], reverse=True)

    # If the number of results is more than expected, get first 3
    if len(sorted_freq) > 3:
        result = [item[0] for item in sorted_freq[:3]]
    else:
        result = [item[0] for item in sorted_freq]

    # Read the XLS file for create relation with other columns
    clinic_set = pd.read_excel(file_path, sheet_name=2)

    # Use only the first 27 rows
    clinic_set = clinic_set[:27]

    # Replace unwanted values with "unknown"
    clinic_set.fillna("belirsiz", inplace=True)
    clinic_set['CİNS'].replace('e', 'belirsiz', inplace=True)
    clinic_set['CİNS'].replace('f', 'kadın', inplace=True)
    clinic_set['CİNS'].replace('m', 'erkek', inplace=True)

    # Add other columns
    detailed_result = {}
    for i in result:
        sub_dictionary = {}
        row = clinic_set[clinic_set['AD'] == i]
        json_row = {
            "klinik": row['KLİNİK AD'].iloc[0], "cinsiyet": row['CİNS'].iloc[0], "yaş": row['YAŞ'].iloc[0]}

        detailed_result[i] = json_row

    # Return result as json
    return jsonify({'success': 'true', 'result': detailed_result})


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the form data here
        name = request.form['name']
        age = request.form['age']
        return f"Name: {name}, Age: {age}"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
