import csv
import sys
import json
import math

punctuations = ['.','?','!','\\','/',',']
master_dict = {"provide_info_color_blue":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_color_brown":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_color_black":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_category_boots":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_category_loafers":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_category_sandals":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_cost_cheap":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_cost_moderate":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_cost_expensive":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_yes":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_no":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_anything":{"tokenfreq":{}, "count": 0, "word_count":0},
               "provide_info_NA":{"tokenfreq":{}, "count": 0, "word_count":0},
              }

def scan_data_file(path_to_file):
    """
    Scans the csv file to get the supervised data
    """

    token_list = []
    tag_list = []

    fp = open(path_to_file, "r")
    reader = csv.DictReader(fp)
    
    for row in reader:
        token_str = row['Tokens']
        token_str = token_str.lower().strip()
        for item in punctuations:
            token_str = token_str.replace(item, "")
        tag = row['Tag'].strip()
        
        for token in token_str.split():
            if token not in master_dict[tag]["tokenfreq"]:
                master_dict[tag]["tokenfreq"][token] = 1
            else:
                master_dict[tag]["tokenfreq"][token] = master_dict[tag]["tokenfreq"][token] + 1
            master_dict[tag]["word_count"] = master_dict[tag]["word_count"] + 1
        
        master_dict[tag]["count"] = master_dict[tag]["count"] + 1

    fp.close()

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Not enough arguments: python nlu_learn.py <path_to_csv_file>")
        sys.exit(-1)

    print("Given File:" + sys.argv[1]) 
    
    # Scans the given csv file to build the model 
    scan_data_file(sys.argv[1])

    # Getting the vocabulary of the given data set
    all_word_list = []
    for key in master_dict:
        all_word_list = all_word_list + list(master_dict[key]["tokenfreq"])
    vocabulary = set(all_word_list)

    # Add one smoothing
    for key in master_dict:
        for word in master_dict[key]["tokenfreq"]:
            master_dict[key]["tokenfreq"][word] = float(master_dict[key]["tokenfreq"][word] + 1)/(float(master_dict[key]["word_count"]+len(vocabulary)))

    # Store the model in a file
    with open('Corpus_model.txt', 'w', encoding="latin1") as fp:
        json.dump(master_dict, fp)
    
    # Prints the learnt model
    #print(master_dict)
