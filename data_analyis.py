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

    # Conditional tasks based on roll_number
    roll_number = int(input("Enter your roll number:M21AIE245 "))
    if roll_number % 2 == 0:
      # List out missing values
      print("Missing values:")
      print(data.isnull().sum())
    else:
      # Encode categorical values
      categorical_cols = data.select_dtypes(include=['object']).columns
      for col in categorical_cols:
        data[col] = pd.Categorical(data[col]).codes
      print("Categorical values encoded.")

def main():
  file_path = input("Enter the path to the CSV file: ")
  data = load_data(file_path)
  analyze_data(data)

if __name__ == "__main__":
  main()