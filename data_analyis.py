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

def analyze_data(data, roll_number):
    """Perform data analysis based on roll number."""
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
        
        if roll_number % 2 == 0:
            # List out missing values, if any
            print("Missing Values:")
            print(data.isnull().sum())
        else:
            # Encode categorical values
            le = LabelEncoder()
            data['Class'] = le.fit_transform(data['Class'])
        
        # Plot bar plot for the class label
        class_label_counts = data['Class'].value_counts()
        class_label_counts.plot(kind='bar')
        plt.title('Class Label Distribution')
        plt.xlabel('Class Label')
        plt.ylabel('Count')
        plt.show()

def main():
    file_path = input("Enter the path to the CSV file: ")
    roll_number = int(input("Enter your roll number: ").split('M21AIE')[-1])
    data = load_data(file_path)
    analyze_data(data, roll_number)

if __name__ == "__main__":
    main()
