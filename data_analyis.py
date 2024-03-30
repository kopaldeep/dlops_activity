import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


def plot_class_distribution(data):
        class_label_counts = data['Class'].value_counts()
        class_label_counts.plot(kind='bar')
        plt.title('Class Label Distribution')
        plt.xlabel('Class Label')
        plt.ylabel('Count')
        plt.show()

def main():
    file_path = input("Enter the path to the CSV file: ")
    data = pd.read_excel(file_path)
    class_label_encoder = LabelEncoder()
    data['Class'] = class_label_encoder.fit_transform(data['Class'])
    plot_class_distribution(data)

if __name__ == "__main__":
    main()
