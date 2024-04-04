import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from an Excel file."""
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
    """Perform data analysis based on the roll number."""
    if data is not None:
        # Display summary statistics
        print("Summary Statistics:")
        print(data.describe())
        
        # Perform specific analysis based on the roll number
        if roll_number % 2 == 0:  # If roll_number is even
            # List out missing values, if any
            print("Missing Values:")
            print(data.isnull().sum())
        else:  # If roll_number is odd
            # Encode categorical values
            categorical_cols = data.select_dtypes(include=['object']).columns
            for col in categorical_cols:
                data[col] = data[col].astype('category').cat.codes
            print("Categorical Values Encoded.")
        
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
    file_path = input("Enter the path to the Excel file: ")
    roll_number = int(input("Enter your roll number: "))
    data = load_data(file_path)
    analyze_data(data, roll_number)

if __name__ == "__main__":
    main()
