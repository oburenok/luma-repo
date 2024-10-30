import csv
import pandas as pd

from utils import globl


def excel_to_dict_ext(file_path, sheets_list):
    """
    Reads test data from xlsx file and returning dictionary

    :param file_path: path to Excel file
    :type file_path: str
    :param sheets_list: list of Excel sheets
    :type sheets_list: lst

    Example:
            read_data.excel_to_dict_ext('Test07_ReadFromFileAndSearch.xlsx', ['SearchResults', 'HomePage'])

    :return:
        dict of data
    """
    test_data = {}

    for sheet in sheets_list:
        # data_xlsx = pd.read_excel(globl.test_path + '\\' + file_path, sheet)
        data_xlsx = pd.read_excel(file_path, sheet)
        data_xlsx = data_xlsx.to_dict()
        test_data[sheet] = {}

        for row in range(0, len(data_xlsx['data_id'])):
            test_data[sheet][data_xlsx['data_id'][row]] = {}

            for column in data_xlsx:
                if column == 'data_id':
                    continue
                test_data[sheet][data_xlsx['data_id'][row]][column] = data_xlsx[column][row]

    return test_data


def csv_to_dict(file_path):
    """
    Reads test data from csv file and returning dictionary

    :param file_path: path to Excel file
    :type file_path: str

    Example:
            read_data.csv_to_dict("Test07_ReadFromFileAndSearch.csv")

    :return:
        dict of data
    """
    test_data = []

    with open(file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            test_data.append(row)

    return test_data


def excel_to_dict(file_path, sheet):
    """
    Reads test data from xlsx file and returning dictionary. File sould start with column 'data_id'

    :param file_path: path to Excel file
    :type file_path: str
    :param sheet: Excel sheet
    :type sheet: str

    Example:
            read_data.excel_to_dict('Test07_ReadFromFileAndSearch.xlsx', 'SearchResults')

    :return:
        list of dicts
    """
    test_data = []

    data_xlsx = pd.read_excel(file_path, sheet)
    data_xlsx = data_xlsx.to_dict()

    for row in range(0, len(data_xlsx['data_id'])):
        test_data.append({})
        for column in data_xlsx:
            test_data[row][column] = data_xlsx[column][row]

    return test_data

