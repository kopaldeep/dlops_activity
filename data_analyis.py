import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_excel(file_path)
        # convert categorical to numerical
        data=catogerical_Numerical(data)
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

def catogerical_Numerical(data):
    for i in range(len(data['Class'])):
        if data['Class'].iloc[i]=='SEKER':
            data['Class'].iloc[i]= 1
        elif data['Class'].iloc[i]=='BARBUNYA':
            data['Class'].iloc[i]= 2
        elif data['Class'].iloc[i]=='BOMBAY':
            data['Class'].iloc[i]= 3
        elif data['Class'].iloc[i]=='CALI':
            data['Class'].iloc[i]= 4
        elif data['Class'].iloc[i]=='HOROZ':
            data['Class'].iloc[i]= 5
        elif data['Class'].iloc[i]=='SIRA':
            data['Class'].iloc[i]= 6
        elif data['Class'].iloc[i]=='DERMASON':
            data['Class'].iloc[i]= 7
    return data


def main():
    file_path = input("Enter the path to the CSV file: ")
    data = load_data(file_path)
    analyze_data(data)

if __name__ == "__main__":
    main()
