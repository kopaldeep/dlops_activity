import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def label_encode_data(data):
    obj_cols=data.select_dtypes(include=['O']).columns
    for col in obj_cols:
        print(f'Categorical Encoding column: {col}, n_categories: {pd.unique(data[col]).__len__()}')
        data[col]=LabelEncoder().fit_transform(data[col])
    return data

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

def main():
    file_path = input("Enter the path to the CSV file: ")
    data = load_data(file_path)
    data = label_encode_data(data)
    analyze_data(data)

if __name__ == "__main__":
    main()