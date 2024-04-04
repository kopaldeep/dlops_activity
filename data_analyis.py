import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from a file. Automatically determines if the file is CSV or Excel based on the extension."""
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            data = pd.read_excel(file_path)
        else:
            print("Unsupported file format. Please provide a CSV or Excel file.")
            return None
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
        print("Summary Statistics:")
        print(data.describe())

        print("Histograms:")
        numeric_cols = data.select_dtypes(include=['int', 'float']).columns
        if numeric_cols.empty:
            print("No numeric columns to plot.")
        else:
            for col in numeric_cols:
                data[col].plot(kind='hist', bins=10)
                plt.title(col)
                plt.xlabel(col)
                plt.ylabel('Frequency')
                plt.show()
        
        if 'Class' in data.columns:
            print("Class Label Distribution:")
            class_label_counts = data['Class'].value_counts()
            class_label_counts.plot(kind='bar')
            plt.title('Class Label Distribution')
            plt.xlabel('Class Label')
            plt.ylabel('Count')
            plt.show()
        else:
            print("No 'Class' column found for distribution plot.")

def main():
    file_path = input("Enter the path to the file: ")
    data = load_data(file_path)
    analyze_data(data)

if __name__ == "__main__":
    main()
