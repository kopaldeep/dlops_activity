import pandas as pd
import matplotlib.pyplot as plt

roll_number = 203 #m22aie203

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

def analyze_data(data):
    """Perform basic data analysis."""
    if data is not None:
        # Check if roll number is even or odd
        if roll_number % 2 == 0:  # Even roll number
            # List missing values
            missing_values = data.isnull().sum()
            if not missing_values.empty:
                print("Missing Values:")
                print(missing_values)
            else:
                print("No missing values.")
        else:  # Odd roll number
            # Encode categorical values
            categorical_cols = data.select_dtypes(include=['object'])
            if not categorical_cols.empty:
                print("Categorical Columns:")
                print(categorical_cols)
                data_encoded = pd.get_dummies(data, columns=categorical_cols.columns)
                print("Encoded Data:")
                print(data_encoded)
            else:
                print("No categorical columns to encode.")
        
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
    analyze_data(data)

if __name__ == "__main__":
    main()
