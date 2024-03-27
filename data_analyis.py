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

### Encoding the categorical values 
def Encode_data(data):
    data['Class'] = data['Class'].astype('category').cat.codes
    print(data['Class'])
    
def main():
    file_path = '/home/maverick/DL_ops_GitHub/dlops_activity/DryBeanDataset/Dry_Bean_Dataset.xlsx'
    data = load_data(file_path)
    print(data)
    Encode_data(data)
    print(data)
    analyze_data(data)

if __name__ == "__main__":
    main()
