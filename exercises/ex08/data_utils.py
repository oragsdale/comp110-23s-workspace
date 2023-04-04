"""EX08 Data Wrangling"""

__author__ = "730560351"

from csv import DictReader

DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close

    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    # step through table
    for row in table:
        # save every value under key "header"
        result.append(row[header])

    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that its a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns the number of rows of the data set given in the function call."""
    first_rows: dict[str, list[str]] = {}
    for columns in table: 
        n_values: list[str] = []
        for n in range(0, rows):
            n_values.append(table[columns][n])
        first_rows[columns] = n_values

    return first_rows

#
def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only a specific subset of the original columns."""
    selected_columns: dict[str, list[str]] = {}
    for column in columns: 
        selected_columns[column] = table[column]

    return selected_columns


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new table by combining two column-based tables."""
    new_table: dict[str, list[str]] = {}
    for column in table_1:
        new_table[column] = table_1[column]
    for column in table_2:
        if column in new_table: 
            new_table[column] += table_2[column]
        else: 
            new_table[column] = table_2[column]

    return new_table


def count(values: list[str]) -> dict[str, int]:
    """Produces a dictionary of the number of appearances of each value within the given list."""
    counts: dict[str, int] = {}
    for item in values: 
        if item in counts:
            counts[item] += 1
        else: 
            counts[item] = 1

    return counts