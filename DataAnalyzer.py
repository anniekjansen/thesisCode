import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyzer:

    def load_csv(self, input_csv):
        data = pd.read_csv(input_csv, index_col=0)
        return data

    def print_column_names(self, data):
        print("Columns:")
        for column in data.columns:
            print(column)

    def print_info(self, data):
        print(data.head())
        print(data.iloc[0])
        print(data.shape)
        print(data.dtypes)

    def print_histogram(self, data, column_title):
        data[column_title].value_counts().plot(kind='bar')
        plt.show()

    def print_selected_columns(self, data, columns): 
        print(data[columns])
    
    def print_selected_cell(self, data, rownumber, column_title):
        print(data.loc[rownumber, column_title])
        print(data.iloc[rownumber])

    def print_selected_value(self, data, column_title, value):
        print(data.loc[data[column_title] == value])

    def check_duplicates(self, data):
        print('Total # of duplicates:', data.duplicated().sum())

    def check_duplicates_columns(self, data, columns):
        for col in columns:
            print(col, ':', data.duplicated(subset=[col]).sum(), 'duplicates')

    def check_uniques(self, data):
        print(data.nunique())

