import csv
import pandas as pd
import numpy as np


fic="c:\\tmp\\data\\jenkins.json"
csv_path = "c:\\tmp\\data\\results.csv"

data = ""


def write_csv(row):
    with open (csv_path, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['methodName', 'ScenarioKey''browser','lang','status'])
        filewriter.writerow(row)

def create_dataframe():
    columns = ['methodName' , 'ScenarioKey', 'browser','lang','status']
    df_row = read_row()
    #lst = range(50)
      #  np.array_split(lst, 5)
    print(df_row)
    df = pd.DataFrame(np.array(df_row), columns=columns)
    #df = pd.DataFrame(df_row, columns = columns).transpose()
    #print(df)
    return df_row


def read_row():
    row = []
    dataset = []
    with open(fic, 'r') as file:
        data = file.read()
        replaced_quotes = data.replace('"',"")
        replaced_columns = replaced_quotes.replace(':',"")
        res = replaced_columns.split()
        print("res :" + str(res))
    for i in range(len(res)):
            if (res[i] == "methodName"):
                row.append(res[i + 1])
            if (res[i] == "classScenarioKey"):
                row.append(res[i + 1])
            if (res[i] == "browser") and (res[i + 1] !="{"):
                row.append(res[i + 1])
            if (res[i] == "lang"):
                row.append(res[i + 1])
            if (res[i] == "status"):
                row.append(res[i + 1])
    print(row)
    return row

    
def main():
    read_row()
    #create_dataframe()
    #write_csv(row)    


if __name__ == '__main__':
    main()

