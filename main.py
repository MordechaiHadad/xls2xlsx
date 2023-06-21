def convert_numeric(value):
    if type(value) is float:
        return value

    if value.isdigit():
        return int(value)
    elif value.replace('.', '', 1).isdigit():
        return float(value)
    else:
        return value

def convert(input_path, output_path):
    import pandas as pd
    data = pd.read_html(input_path)
    table = data[0]

    # table = table.iloc[2:]

    table = table.applymap(convert_numeric)

    table.to_excel(output_path, header=False, index=False)


import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='path to the input file')
    parser.add_argument('-o', '--output_file', default='./output.xlsx', help='path to the output file')
    args = parser.parse_args()

    input_file_path = args.input_file
    output_file_path = args.output_file

    convert(input_file_path, output_file_path)


if __name__ == '__main__':
    main()