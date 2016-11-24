from speech_recognizer import recognize_speech
from nlu_one import first_classifier
#from nlu_two import second_classifier
from speech_generation import generate_speech



# Global Variables
features_dict = {"info_initial_response":"empty","info_color":"empty","info_size":"empty","info_category":"empty","info_final_response":"empty"}
color_list = {"brown", "black", "blue"}
category_list = {"sandals", "loafers", "boots", "anything"}
cost_list = {"cheap", "moderate", "expensive"}
positive_response_list = {"yes", "correct", "right"}
state_initial = False
state_cost = False
state_category = False
state_size = False
state_final = False
state_color = False
  
def fetch_initial_statement():
    # generate_speech() is the function in the speech_generation module
    # recognize_speech() is the function in the speech_recognition module
    # first_classifier() is the function in the nlu_one module
    # second_classifier() is the function in the nlu_two module
    global state_initial, features_dict
    
    #generate_speech (" Hello. I'm your shoe shopping assistant. How can i help you", is_final = "False")
    generate_speech (features_dict, "initial", "True")
    
    
    while(state_initial == False):
        statement = recognize_speech()
        first_nlu_dict = first_classifier(statement, state = "initial")
        
        if (first_nlu_dict["info_initial_response"] != "empty" ):
            features_dict = first_nlu_dict
        
        if (features_dict["info_initial_response"] != "empty"):
            state_initial = True
        else:
            generate_speech (features_dict, "initial", first_nlu_dict)
            
    
def fetch_info_color():
    # generate_speech() is the function in the speech_generation module
    # recognize_speech() is the function in the speech recognition module
    # first_classifier() is the function in the nlu_one module
    # second_classifier() is the function in the nlu_two module
    global state_color, color_list, features_dict
    
    if(features_dict["info_color"] != "empty"):
        state_color = True
    else:
        generate_speech (features_dict, "color", "True")
    
    while(state_color == False):
        statement = recognize_speech()
        first_nlu_dict = first_classifier(statement, "color")
        
        
        if (first_nlu_dict["info_color"] != "empty" ):
            features_dict["info_color"] = first_nlu_dict["info_color"]
                
        if(features_dict["info_color"] != "empty"):
            state_color = True
        else:
            generate_speech (features_dict, "color", first_nlu_dict)


def fetch_info_category():
    # generate_speech() is the function in the speech_generation module
    # recognize_speech() is the function in the speech recognition module
    # first_classifier() is the function in the nlu_one module
    # second_classifier() is the function in the nlu_two module
    global state_category, category_list, features_dict
    
    if(features_dict["info_category"] != "empty"):
        state_category = True
    else:
        generate_speech (features_dict, "category", "True")
    
    while(state_category == False):
        statement = recognize_speech()
        first_nlu_dict = first_classifier(statement, "category")
        
        
        if (first_nlu_dict["info_category"] != "empty" ):
            features_dict["info_category"] = first_nlu_dict["info_category"]
                
        if(features_dict["info_category"] != "empty"):
            state_category = True
        else:
            generate_speech (features_dict, "category", first_nlu_dict)
            

def fetch_info_cost():
    # generate_speech() is the function in the speech_generation module
    # recognize_speech() is the function in the speech recognition module
    # first_classifier() is the function in the nlu_one module
    # second_classifier() is the function in the nlu_two module
    global state_cost, cost_list, features_dict
    
    if(features_dict["info_cost"] != "empty"):
        state_cost = True
    else:
        generate_speech (features_dict, "cost", "True")
    
    
    while(state_cost == False):
        statement = recognize_speech()
        first_nlu_dict = first_classifier(statement, "cost")
        
        
        if (first_nlu_dict["info_cost"] != "empty" ):
            features_dict["info_cost"] = first_nlu_dict["info_cost"]
                
        if(features_dict["info_cost"] != "empty"):
            state_cost = True
        else:
            generate_speech (features_dict, "cost", first_nlu_dict)

def fetch_final_statement():
    # generate_speech() is the function in the speech_generation module
    # recognize_speech() is the function in the speech recognition module
    # first_classifier() is the function in the nlu_one module
    # second_classifier() is the function in the nlu_two module
    global state_color, state_category, state_cost, state_final, positive_response_list, features_dict
    
    
    generate_speech (features_dict, "final", "True" )
    
    
    while(state_final == False):
        
        statement = recognize_speech()
        first_nlu_dict = first_classifier(statement, "final")
        
        if (first_nlu_dict["info_final_response"] == "yes" ):
            features_dict["info_final_response"] = first_nlu_dict["info_final_response"]
            state_final = True
        elif (first_nlu_dict["info_final_response"] == "no" ):
            state_category = False
            state_color = False
            state_cost = False
            features_dict["info_color"] = "empty"
            features_dict["info_category"] = "empty"
            features_dict["info_cost"] = "empty"
            fetch_info_category()
            fetch_info_color()
            fetch_info_cost()
            generate_speech (features_dict, "final", "True" )
        else:
            generate_speech (features_dict, "final", "True" )
         
        
                
def fetch_results_from_db():
    global features_dict
    generate_speech(features_dict, "final", "empty" )
        
    

if __name__ == '__main__':
    
    fetch_initial_statement()
    
    fetch_info_category()
    
    fetch_info_color()
    
    fetch_info_cost()

    fetch_final_statement()  
  
    fetch_results_from_db()
    
