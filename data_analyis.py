import pandas as pd
import matplotlib.pyplot as plt

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
        # Display summary statistics
        print("Summary Statistics:")
        print(data.describe())

        # Encode categorical columns
        categorical_cols = data.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            print("Encoding categorical columns...")
            encoded_data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)
            print("Encoded Data:")
            print(encoded_data.head())
            
            # Update the 'data' DataFrame with the encoded data
            data = encoded_data
        else:
            print("No categorical columns found.")

        # Plot histograms for numeric columns
        print("Histograms:")
        for col in data.select_dtypes(include=['int', 'float']):
            data[col].plot(kind='hist', bins=10)
            plt.title(col)
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        
        # Plot bar plot for the class label (string type)
        if 'Class' in data.columns:
            class_label_counts = data['Class'].value_counts()
            class_label_counts.plot(kind='bar')
            plt.title('Class Label Distribution')
            plt.xlabel('Class Label')
            plt.ylabel('Count')
            plt.show()
        else:
            print("No 'Class' column found.")

def main():
    file_path = input("Enter the path to the CSV file: ")
    data = load_data(file_path)
    analyze_data(data)

if __name__ == "__main__":
    main()
