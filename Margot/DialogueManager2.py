from speech_recognizer import recognize_speech
from nlu_two import second_classifier
from speech_generation import generate_speech



# Global Variables
features_dict = {"info_color":"empty","info_cost":"empty","info_category":"empty","info_final_response":"empty"}
color_list = {"brown", "black", "blue", "anything"}
category_list = {"sandals", "loafers", "boots", "anything"}
cost_list = {"cheap", "moderate", "expensive", "anything"}
positive_response_list = {"yes", "correct", "right", "anything"}
state_cost = False
state_category = False
state_color = False
state_final = False

  

def fetch_info_color():
    # generate_speech() is the function in the speech_generation module
    # recognize_speech() is the function in the speech recognition module
    # first_classifier() is the function in the nlu_one module
    # second_classifier() is the function in the nlu_two module
    global state_color, color_list, features_dict
    
    generate_speech (features_dict, "color", "True")
    
    while(state_color == False):
        statement = recognize_speech()
        second_nlu_dict = second_classifier(statement, "color")
        
        
        if (second_nlu_dict["info_color"] != "empty"):
            if(second_nlu_dict["info_color"] in color_list):
                features_dict["info_color"] = [second_nlu_dict["info_color"]]
            else:
                generate_speech (features_dict, "color", second_nlu_dict)
        else:
            generate_speech (features_dict, "color", second_nlu_dict)
                
                
        
        if(features_dict["info_color"] != "empty"):
            state_color = True


def fetch_info_category():
    # generate_speech() is the function in the speech_generation module
    # recognize_speech() is the function in the speech recognition module
    # first_classifier() is the function in the nlu_one module
    # second_classifier() is the function in the nlu_two module
    global state_category, category_list, features_dict
    
    
    generate_speech (features_dict, "category", "True")   
    while(state_category == False):
        statement = recognize_speech()
        second_nlu_dict = second_classifier(statement, "category")
        
        
        if (second_nlu_dict["info_category"] != "empty"):
            if(second_nlu_dict["info_category"] in category_list):
                features_dict["info_category"] = [second_nlu_dict["info_category"]]
            else:
                generate_speech (features_dict, "category", second_nlu_dict)
        else:
            generate_speech (features_dict, "category", second_nlu_dict)
                
                
        
        if(features_dict["info_category"] != "empty"):
            state_category = True
            

def fetch_info_cost():
    # generate_speech() is the function in the speech_generation module
    # recognize_speech() is the function in the speech recognition module
    # first_classifier() is the function in the nlu_one module
    # second_classifier() is the function in the nlu_two module
    global state_cost, cost_list, features_dict
    
    
    generate_speech (features_dict, "cost", "True")
    
    while(state_cost == False):
        statement = recognize_speech()
        second_nlu_dict = second_classifier(statement, "cost")
        
        
        if (second_nlu_dict["info_cost"] != "empty"):
            if(second_nlu_dict["info_cost"] in cost_list):
                features_dict["info_cost"] = [second_nlu_dict["info_cost"]]
            else:
                generate_speech (features_dict, "cost", second_nlu_dict)
        else:
            generate_speech (features_dict, "cost", second_nlu_dict)
                
                
        
        if(features_dict["info_cost"] != "empty"):
            state_cost = True

def fetch_final_statement():
    # generate_speech() is the function in the speech_generation module
    # recognize_speech() is the function in the speech recognition module
    # first_classifier() is the function in the nlu_one module
    # second_classifier() is the function in the nlu_two module
    global state_color, state_category, state_cost, state_final, positive_response_list, features_dict
    
    
    generate_speech (features_dict, "final", "True" )
    
    
    while(state_final == False):
        
        statement = recognize_speech()
        second_nlu_dict = second_classifier(statement, state = "final_response")
        
        # print (second_nlu_dict["info_final_response"])        
        if(second_nlu_dict["info_final_response"] == "yes"):
            state_final = True
        elif(second_nlu_dict["info_final_response"] == "no"):
            state_category = False
            state_color = False
            state_cost = False
            
            features_dict["info_category"] = "empty"
            features_dict["info_cost"] = "empty"
            features_dict["info_color"] = "empty"
 
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
    
    fetch_info_category()
    
    fetch_info_color()
    
    fetch_info_cost()
    
    fetch_final_statement()
    
    fetch_results_from_db()
    
