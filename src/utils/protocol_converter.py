# Pomesh: August 2025
# converts protocols in word documents into json files
# input argument is either a single .docx file or a directory of .docx (no subdirectories)

# python modules
import re
import json
import os
import sys
import argparse
from pathlib import Path

# third-party modules
# pip install mammoth beautifulsoup4
import mammoth # conversion from word to html
from bs4 import BeautifulSoup # for parsing html to json

def main():
    print("contact pomesh for more information or errors!")
    print("starting conversion\n----------------------")  

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="can be a single .docx file or a directory of .docx")
    args = parser.parse_args()

    # create the output directory
    Path('output').mkdir(parents=True, exist_ok=True)
    
    # will abstract out the logic to separate function, avoid code reuse
    if (os.path.isfile(args.input)):
        input_file = Path(args.input)
        with open(input_file, "rb") as f:
            res = mammoth.convert_to_html(f)
            text = res.value
            parsehtml(text, input_file)
    elif (os.path.isdir(args.input)):
        files = Path(args.input).rglob('*.docx')
        for file in files:
            with open(file, "rb") as f:
                res = mammoth.convert_to_html(f)
                text = res.value
                parsehtml(text, file)
    else:
        print("argument needs to be either a word file with .docx or a directory of word files!")

    print("--------------------------\nend conversion")
    
def parsehtml(text, input_file):
    print("parsing " + str(input_file))
    final_dict = {} # master dictionary which we will append and dump to json
    soup = BeautifulSoup(text, 'html.parser')

    # get removed images for cleaner html, we may need individual sequence images 
    # i will work on those later
    # img = soup.find('img')
    # img.decompose()

    # temporary test html file, comment out
    # with open("clean_test.html", "w") as f:
    #     f.write(str(soup.prettify()))

    # extract all the labels
    final_dict['system'] = parse_single_line("System", soup)
    final_dict['spool'] = parse_single_line("Spole", soup)
    final_dict['contrast'] = parse_single_line("Kontrast", soup)
    final_dict['code'] = parse_single_line("Undersökningskod", soup)
    final_dict['time'] = parse_single_line("Undersökningstid", soup)   
    
    # extract all the lists
    ind_list = parse_list("Vanliga indikationer", soup)
    final_dict['indications'] = [i for i in ind_list]

    prep_list = parse_list("Förberedelser", soup)
    final_dict['preparations'] = [i for i in prep_list]    
    
    # extract the table
    table = soup.find('table')
    headers = [th.text.strip() for th in table.find_all('th')[1:]]
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = [td.text.strip() for td in row.find_all('td')]
        rows.append(cells)

    table_dict = {}
    table_dict['headers'] = [header for header in headers]
    # extract the table data, using id + 1 so we skip 0 and start at 1 for ids
    table_dict['data'] = [extract_table_data(row, id+1) for id, row in enumerate(rows)]
    
    final_dict['sequences'] = table_dict
    
    with open(os.path.join('output', input_file.stem) + ".json", "w") as file_handle:
        data = json.dumps(final_dict, ensure_ascii=False)
        file_handle.write(data)

    # print(final_dict)
    print(str(input_file) + " done writing data to html\n")


def parse_single_line(line_name, soup):
    # extract the information after a bold line, note that there should be a
    # semicolon : after line_name in the word document, otherwise the regex fails
    # an empty string is returned if no entry is found
    extract_info = re.compile(rf"<p><strong>{line_name}:</strong>(.*?)</p>")
    res = ''
    try:
        res = extract_info.findall(str(soup))[0]
    except:
        print(line_name + " entry does not exist!")
    return res

def parse_list(list_header, soup):
# extract lists
    extract_list = re.compile(list_header)
    try:
        lst = soup.find(string=extract_list).find_next('ul').find_all('li')
    except:
        yield ''
    else:
        for el in lst:
            yield el.get_text()

def extract_table_data(row, id):
    # create the data section of the table
    # check if the first element is empty, then return the next element only

    data_dict = {}
    if not row[0]:
        data_dict['id'] = id
        data_dict['row_info'] = handle_row_error(row, 1)
    else:
        data_dict['id'] = id
        data_dict['sequences'] = handle_row_error(row, 1)
        data_dict['scan_planes'] = handle_row_error(row, 2)
        data_dict['slice_thickness'] = handle_row_error(row, 3)
        data_dict['extra_info'] = handle_row_error(row, 4)

    return data_dict

def handle_row_error(row, index):
    # quick function to handle list index out of range for non-filled entries in the tables
    res = ''
    try:
        res = row[index]
    except:
        print("\tinserting empty string in row")
    return res
    

if __name__ == "__main__":
    main()