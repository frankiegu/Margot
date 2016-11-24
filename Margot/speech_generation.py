from speechSyn import speak
import sqlite3

def generate_speech(features_dict,state,help_dict):
    if(state == "initial"):
        speak("Hello ! I'm your shoe shopping assistant. What can i help you with ?")
    elif( state == "final" and help_dict == "empty"):
        print_result(features_dict)
    elif( state == "final" and help_dict == "True"):
        confirm_results(features_dict)
    elif( type(help_dict) == type(dict()) ):
        ask_other_question(features_dict,state,help_dict)
    else:
        ask_question(features_dict,state)
        
def print_result(features_dict):
    len1 = print_results(features_dict,0)
    if(len1 < 1):
        speak("We are sorry, we do not have footwear based on your requirements.")
        if("expensive" in features_dict["info_cost"]):
            if("moderate" not in features_dict["info_cost"]):
                features_dict["info_cost"].append("moderate")
            if("cheap" not in features_dict["info_cost"]):
                features_dict["info_cost"].append("cheap")
            len2 = print_results(features_dict,1)
        elif("moderate" in features_dict["info_cost"]):
            if("expensive" not in features_dict["info_cost"]):
                features_dict["info_cost"].append("expensive")
            if("cheap" not in features_dict["info_cost"]):
                features_dict["info_cost"].append("cheap")
        elif("cheap" in features_dict["info_cost"]):
            if("expensive" not in features_dict["info_cost"]):
                features_dict["info_cost"].append("expensive")
            if("moderate" not in features_dict["info_cost"]):
                features_dict["info_cost"].append("moderate")
            len2 = print_results(features_dict,1)
        if(len2 < 1):
            speak("We are sorry, we do not have footwear based on your requirements.")
            if("black" in features_dict["info_color"]):
                if("brown" not in features_dict["info_color"]):
                    features_dict["info_color"].append("brown")
                if("blue" not in features_dict["info_color"]):
                    features_dict["info_color"].append("blue")
                len3 = print_results(features_dict,1)
            elif("brown" in features_dict["info_color"]):
                if("black" not in features_dict["info_color"]):
                    features_dict["info_color"].append("black")
                if("blue" not in features_dict["info_color"]):
                    features_dict["info_color"].append("blue")
            elif("blue" in features_dict["info_color"]):
                if("black" not in features_dict["info_color"]):
                    features_dict["info_color"].append("black")
                if("brown" not in features_dict["info_color"]):
                    features_dict["info_color"].append("brown")
                len3 = print_results(features_dict,1)
            if(len3 < 1):
                speak("We are sorry, we do not have footwear based on your requirements.")

def print_results(features_dict,no):
    conn = sqlite3.connect('test.db')
    if_and = 0
    initial = "SELECT * FROM footwear"
    query = ""
    company = {}
    if( features_dict["info_color"] !="empty" or features_dict["info_category"] !="empty" or features_dict["info_cost"] !="empty"):
        query += " WHERE "
        if(features_dict["info_color"] !="empty"):
            if(features_dict["info_color"][0] != "anything"):
                query += "color in "+repr(features_dict["info_color"]).replace('[','(').replace(']',')')
                if_and = 1
        if(features_dict["info_category"] !="empty"):
            if(features_dict["info_category"][0] != "anything"):
                if(if_and == 1):
                    query += " and "
                    if_and = 0
                query += "category in "+repr(features_dict["info_category"]).replace('[','(').replace(']',')')
                if_and = 1
        if(features_dict["info_cost"] !="empty"):
            if(features_dict["info_cost"][0] != "anything"):
                if(if_and == 1):
                    query += " and "
                query += "cost in "+repr(features_dict["info_cost"]).replace('[','(').replace(']',')')
    if(features_dict["info_cost"] == "empty" or len(features_dict["info_cost"]) == 1 ):
        if(query != " WHERE "):
            initial += query
        initial += " ORDER BY name"
        cursor = conn.execute(initial)
        len1 = 0
        flag_and = 0
        temp = ""
        if(no == 1):
            temp = "But we have cheaper options"
        output = "Top options that we have are"
        output1 = "\nFollowing are the top options that we have for you:\n"
        prev = ""
        prev_len = 0;
        for row in cursor:
            len1 += 1
            if(len1 < 6):
                    output1 += str(len1)+". "+str(row[2])+" "+str(row[0])+" "+str(row[1])+" from "+str(row[4])+"\n"
                    if(row[4] not in company):
                        company[row[4]] = 1
                    else:
                        company[row[4]] = company[row[4]]+1
            if(str(row[4]) == prev):
                prev_len += 1
            else:
#                if(len1 < 6):
#                    if(prev_len > 1 and prev != ""):
#                        output += ", "+str(prev_len)+" options from "+prev
#                    elif(prev != ""):
#                        output += ", "+str(prev_len)+" option from "+prev
                prev_len = 1
                prev = str(row[4])
#            if(len1 > 4):
#                if(flag_and == 0):
#                    output += " and"
#                flag_and = 1
            if(len1>5):
                break
#        if(prev_len > 1 and prev != ""):
#            output += ", "+str(prev_len)+" options from "+prev
#        elif(prev != ""):
#            output += ", "+str(prev_len)+" option from "+prev
    else:
        if(query != " WHERE "):
            initial += query
        initial += " ORDER BY cost, name"
        cursor = conn.execute(initial)
        len1 = 0
        flag_and = 0
        temp = ""
        if(no == 1):
            temp = "But we have other options"
        output = "Top options that we have are"
        output1 = "\nFollowing are the top options that we have for you:\n"
        prev = ""
        prev_len = 0;
        pr = 1
        for row in cursor:
            len1 += 1
            if(str(row[2]) == prev):
                prev_len += 1
                pr = 1
                if(prev_len == 3):
                    prev_len -= 1
                    len1 -= 1
                    pr = 0
            else:
                pr = 1
                prev_len = 1
                prev = str(row[2])
            if(len1 < 7 and pr == 1):
                if(row[4] not in company):
                    company[row[4]] = 1
                else:
                    company[row[4]] = company[row[4]]+1
                output1 += str(len1)+". "+str(row[2])+" "+str(row[0])+" "+str(row[1])+" from "+str(row[4])+"\n"
#            if(len1 > 4):
#                if(flag_and == 0):
#                    output += " and"
#                flag_and = 1
            if(len1>6):
                break
    for co in company:
        if(int(company[co])>1):
            output += ", "+str(company[co])+" options from "+str(co)
        else:
            output += ", "+str(company[co])+" option from "+str(co)
    if(len1 < 1):
        return len1
    else:
        if(temp != ""):
            speak(temp)
        print(output1)
        speak(output)
        return len1
            
def confirm_results(features_dict):
    query = "Are you looking for"
    if(features_dict["info_cost"] !="empty"):
        if(features_dict["info_cost"][0] != "anything"):
            query += " "+features_dict["info_cost"][0]
            if(len(features_dict["info_cost"])>1):
                for elem in features_dict["info_cost"][1:]:
                    query += " or "+elem
    if(features_dict["info_color"] !="empty"):
        if(features_dict["info_color"][0] != "anything"):
            query += " "+features_dict["info_color"][0]
            if(len(features_dict["info_color"])>1):
                for elem in features_dict["info_color"][1:]:
                    query += " or "+elem
    if(features_dict["info_category"] !="empty"):
        if(features_dict["info_category"][0] != "anything"):
            query += " "+features_dict["info_category"][0]
            if(len(features_dict["info_category"])>1):
                for elem in features_dict["info_category"][1:]:
                    query += " or "+elem
        else:
            query += " shoes"
    speak(query)           
        
def ask_other_question(features_dict,state,help_dict):
    if( state == "color" ):
        speak("We have black, brown or blue.")
    elif( state == "category" ):
        speak("We have sandals, loafers and boots.")
    elif( state == "cost" ):
        speak("You can choose from cheap, moderate or expensive")
    
def ask_question(features_dict,state):
    if( state == "color" ):
        speak("What color do you prefer?")
    elif( state == "category" ):
        speak("What kind of footwear are you looking for?")
    elif( state == "cost" ):
        speak("Would you prefer cheap, moderate or expensive ones?")

if( __name__ == "__main__"):
    generate_speech({"info_initial_response":"empty","info_color":["black"],"info_cost":["cheap"],"info_category":"empty","info_final_response":"empty"},"final","empty")
    
