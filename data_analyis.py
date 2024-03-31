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

def analyze_data(data, roll_number):
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

        if int(roll_number) % 2 == 0:
            print("Missing Values:")
            # Listing out missing values, if any
            print(data.isnull().sum())  
        elif int(roll_number) % 2 != 0: 
            # Encoding categorical values if any
            categorical_cols = data.select_dtypes(include=['object']).columns
            if not categorical_cols.empty:
                print("Encoding Categorical Values...")
                data_encoded = pd.get_dummies(data, columns=categorical_cols)
                print("Categorical values encoded successfully.")
                return data_encoded

def main():
    file_path = input("Enter the path to the CSV file: ")
    roll_number = input("Enter roll number in numeric only.\nFor example M22AIE249 then please enter 249 only: ")
    data = load_data(file_path)
    analyze_data(data, roll_number)

if __name__ == "__main__":
    main()
