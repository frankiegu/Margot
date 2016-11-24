import csv
import sys
import json

punctuations = ['.','?','!','\\','/',','] 
master_dict = {}
tag_prob = {}
vocabulary = []

def fill_master_dict():
    """
    Reconstructs the master dictionary from the stored model
    """

    global master_dict
    global vocabulary

    json_data = open("Corpus_model.txt", encoding="latin1").read()
    master_dict = json.loads(json_data)

    # Getting the vocabulary of the given data set
    all_word_list = []
    for key in master_dict:
        all_word_list = all_word_list + list(master_dict[key]["tokenfreq"])
    vocabulary = set(all_word_list)

    # Getting the probability of each of the tags
    total_entry_count = 0.0
    for key in master_dict:
        total_entry_count = total_entry_count + master_dict[key]["count"]
    for key in master_dict:
        tag_prob[key] = float(master_dict[key]["count"])/float(total_entry_count)

def second_classifier(statement, state):
    """
    Classifies the given statement into one of the dialogue states 
    """

    global master_dict
    global vocabulary

    # Rebuild the model if necessary
    fill_master_dict()

    # Initialize the dictionary to be returned
    info_dict = {}

    # Tokenize the given statement
    token_str = statement
    token_str = token_str.lower().strip()
    for item in punctuations:
        token_str = token_str.replace(item, "")
    for token in token_str.split():
        for key in master_dict:
            # Calculating the probability of the dialogue belonging to each tag 
            if token in master_dict[key]["tokenfreq"]:
                tag_prob[key] = tag_prob[key] * master_dict[key]["tokenfreq"][token]
            else:
                tag_prob[key] = tag_prob[key] * (1.0/(len(vocabulary) + master_dict[key]["word_count"]))

    # Getting the list of all tags
    key_list = []
    for key in tag_prob.keys():
        key_list.append(key)

    # Predicting the tag for the given dialogue based on probabilities
    predicted_tag = key_list[0]
    for i in range(1,len(key_list)):
        if tag_prob[key_list[i]] > tag_prob[predicted_tag]:
            predicted_tag = key_list[i]

    # Extracting the value of the required info  
    predicted_tag = predicted_tag.replace("provide_info_", "")
    if state == "color" or state == "category" or state == "cost":
        if state in predicted_tag:
            predicted_tag = predicted_tag.replace(state + "_", "")
    
    info_dict["info_"+state] = predicted_tag

    return info_dict

if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        print("Not enough arguments: python nlu_two.py <statement_to_be_classified> <state>")
        sys.exit(-1)

    print("Given Statement:" + sys.argv[1]) 
    print("Given state:" + sys.argv[2])

    # Reconstructs the master dictionary from the stored model
    fill_master_dict()    

    # Classify the given statement
    print(second_classifier(sys.argv[1], sys.argv[2]))
