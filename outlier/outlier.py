"""
@ author : sourav kumar (101883068)
@ made for UCS633 - PROJECT - II
@ Timestamp : 2020 / 2 / 6 , 12 : 10 : 13 . 836206
"""
import numpy as np
import pandas as pd
import sys
# Class for outlier algorithm module
class outlier:
    """
    Attributes:
    df : original dataframe of input file
    input_file : file to be read and perform outlier removal algorithm
    output_file : file to be written into after performing the algorithm
    """
    def __init__(self, read_file, write_file):
        """
        Args:
        input_file : file to be read and perform outlier removal algorithm
        output_file : file to be written into after performing the algorithm
        """
        # check for proper csv file
        assert "csv" in f"{read_file}", "Could not recognize csv file, try checking your input file"
        assert "csv" in f"{write_file}", "Could not recognize csv file, try checking your output file"
        # load and read csv file
        self.df = pd.read_csv(read_file).iloc[:, 1:]
        print('file read succesfully !', f'Shape of original file : {self.df.shape}')
        self.input_file = read_file
        self.output_file = write_file

    # function for detecting missing values and reporting it
    def detect_missing(self):
        # checking missing values
        null_series = self.df.isnull().sum()
        missing_cols = []
        # looping over the found missing item list dictionery
        for i, j in null_series.items():
            if j != 0:
                missing_cols.append(i)
        # reporting missing values columns
        if len(missing_cols):
            print(f'following columns contains missing values : {missing_cols}')
            return True
        else:
            return False

    # main outlier functions caller to execute all the steps of the algorithm
    def outlier_main(self, method='z_score'):
        """
        Args:
        method : choose which algorithm to use for outlier removal - possible \
        values are z_score or iqr
        """
        # run if method is z_score
        if method == 'z_score':
            self.detect_missing()
            # list of all column values which are of type int/float excluding all object type
            l = [column for column in self.df.columns if self.df[column].dtype != 'object']
            if len(l):
                print(f"following columns considered for outlier removal : {l}")
            else:
                print('None of columns are considered for outlier removal')
            removed_rows = 0
            # going over all those list columns which contains valid numerical values
            for i in l:
                # setting threshold value of 3 means any numeric value outside 3 std deviations of
                # distribution will be considered as outlier
                threshold = 3
                # getting mean along column
                mean = np.mean(self.df[i])
                # getting std along column
                std = np.std(self.df[i])
                # checking and filtering all those values of outlier and getting their indices
                outliers = self.df[abs((self.df[i] - mean) / std) > threshold].index
                # removing all those rows found containing outlier value for columns
                self.df.drop(outliers, inplace = True)
                removed_rows += len(outliers)
            print(f'Total {removed_rows} rows removed , new shape of DataFrame : {self.df.shape}')
            # writing into output file , new dataset after outlier removal
            self.df.to_csv(self.output_file, index = False)
            print(f"DataFrame written to {self.output_file}")
        # run if method is iqr
        elif method == 'iqr':
            if self.detect_missing():
                print('Warning : Algorithm may not work properly for IQR method in case of missing data')
            # list of all column values which are of type int/float excluding all object type
            l = [column for column in self.df.columns if self.df[column].dtype != 'object']
            if len(l):
                print(f"following columns considered for outlier removal : {l}")
            else:
                print('None of columns are considered for outlier removal')
            removed_rows = 0
            # here anything below lower bound and anything above upper bound will be considered
            # as outlier for the specified column
            for i in l:
                # calculating 25th and 75th percentiles
                quartile_1, quartile_3 = np.percentile(self.df[i], [25, 75])
                # calculating interquartile range
                iqr = quartile_3 - quartile_1
                lower_bound = quartile_1 - (iqr * 1.5)
                upper_bound = quartile_3 + (iqr * 1.5)
                # checking and filtering all those values of outlier and getting their indices
                iqr_outliers = self.df[(self.df[i] < lower_bound) | (self.df[i] > upper_bound)].index
                self.df.drop(iqr_outliers, inplace = True)
                removed_rows += len(iqr_outliers)
            print(f'Total {removed_rows} rows removed , new shape of DataFrame : {self.df.shape}')
            # writing into output file , new dataset after outlier removal
            self.df.to_csv(self.output_file, index = False)
            print(f"DataFrame written to {self.output_file}")
        # report if any other invalid method is passed
        else:
            print('Must pass only methods - z_score or iqr')

# main driver function
if __name__ == '__main__':
    print('WELCOME TO OUTLIER REMOVAL ALGORITHM USING Z_SCORE OR IQR')
    print('EXPECTED ARGUMENTS TO BE IN ORDER : python -m outlier.outlier <InputFile.csv> <OutputFile.csv> <method>')
    # runs if and only if it contains atleast inputfile, output file
    if len(sys.argv) >= 3:
        read_file = sys.argv[1]
        write_file = sys.argv[2]
        print(f"file given : {read_file}")
        o = outlier(read_file, write_file)
        # if method is not provided, then use z_score
        if len(sys.argv) == 3:
            print('Using default method - z score...')
            o.outlier_main(method='z_score')
        else:
            o.outlier_main(method=sys.argv[3])
    # report for incorrect order of arguments passed
    else:
        print('PLEASE PASS ARGUMENTS IN ORDER : python -m outlier.outlier <InputFile.csv> <OutputFile.csv> <method>')
