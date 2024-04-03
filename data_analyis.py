import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_excel(file_path, engine='openpyxl')
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def analyze_data(data):
    """Perform basic data analysis."""
    if data is not None:
        # Display summary statistics
        print("Summary Statistics:")
        print(data.describe())

        # Plot histograms for numeric columns
        print("Histograms:")
        for col in data.select_dtypes(include=['int', 'float']):
            data[col].plot(kind='hist', bins=10)
            plt.title(col)
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        
        # Plot bar plot for the class label (string type)
        class_label_counts = data['Class'].value_counts()
        class_label_counts.plot(kind='bar')
        plt.title('Class Label Distribution')
        plt.xlabel('Class Label')
        plt.ylabel('Count')
        plt.show()
#my roll number ends with 3, so encoding the categorical values

def encode_categorical(data):
    """Encode categorical columns using LabelEncoder."""
    label_encoders = {}
    for col in data.select_dtypes(include=['object']):
        le = LabelEncoder()
        data[col + '_encoded'] = le.fit_transform(data[col])
        label_encoders[col] = le

    # Print the encoded values
    print("Encoded Values:")
    for col, le in label_encoders.items():
        print(f"{col}:", dict(zip(le.classes_, le.transform(le.classes_))))

    # Display the first few rows of the modified DataFrame, refer column Class_encoded, still Cat col Class is also there, didn't remove it
    print("Modified DataFrame:")
    print(data.head())

def main():
    file_path = input("Enter the path to the CSV file: ")
    data = load_data(file_path)
    analyze_data(data)
    encode_categorical(data)

if __name__ == "__main__":
    main()

