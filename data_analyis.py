import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_excel(file_path)  # Assuming the file is an Excel file based on the existing code.
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

        # Check and print missing values
        print("Missing Values:")
        missing_values = data.isnull().sum()
        print(missing_values[missing_values > 0])  # This will print columns with missing values and their counts

        # Plot histograms for numeric columns
        print("Histograms:")
        for col in data.select_dtypes(include=['int', 'float']):
            data[col].plot(kind='hist', bins=10)
            plt.title(col)
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        
        # Plot bar plot for the class label (string type), if 'Class' column exists
        if 'Class' in data.columns:
            print("Class Label Distribution:")
            class_label_counts = data['Class'].value_counts()
            class_label_counts.plot(kind='bar')
            plt.title('Class Label Distribution')
            plt.xlabel('Class Label')
            plt.ylabel('Count')
            plt.show()

def main():
    file_path = input("Enter the path to the CSV file: ")  # Make sure this matches the file type you're expecting
    data = load_data(file_path)
    analyze_data(data)

if __name__ == "__main__":
    main()

