import re

#global variables

def first_classifier(statement, state):

	nlu_dict = {}
	if(state == "initial" or state == "color"):
		colors = ['brown', 'black', 'blue']
		found = False
		for color in colors:
			search_obj = re.findall(r' ' + color  + ' ', statement, re.M|re.I)
			if search_obj != []:
				search_obj[0] = search_obj[0].strip().lower()
				if found:
					nlu_dict["info_color"].append(search_obj[0])
				else:
					nlu_dict["info_color"] = [search_obj[0]]
					found = True
			if not found:
				nlu_dict["info_color"] = "empty"

	if(state == "initial" or state == "cost"):
		costs = ['cheap', 'moderate', 'expensive']
		found = False
		for cost in costs:
			search_obj = re.findall(r' ' + cost  + ' ', statement, re.M|re.I)
			if search_obj != []:
				search_obj[0] = search_obj[0].strip().lower()
				if found:
					nlu_dict["info_cost"].append(search_obj[0])
				else:
					nlu_dict["info_cost"] = [search_obj[0]]
					found = True
			if not found:
				nlu_dict["info_cost"] = "empty"

	if(state == "initial" or state == "category"):
		categories = ['sandals', 'loafers', 'boots']
		found = False
		for category in categories:
			search_obj = re.findall(r' ' + category + ' ', statement, re.M|re.I)
			if search_obj != []:
				search_obj[0] = search_obj[0].strip().lower()
				if found:
					nlu_dict["info_category"].append(search_obj[0])
				else:
					nlu_dict["info_category"] = [search_obj[0]]
					found = True

			if not found:
				nlu_dict["info_category"] = "empty"

	if(state != "initial" and state != "final"):
		search_obj = re.findall(r' any | anything | all ', statement, re.M|re.I)
		if search_obj != []:
			nlu_dict["info_"+state] = ["anything"]

	if state == "initial":
		nlu_dict["info_initial_response"] = "filled"
		nlu_dict["info_final_response"] = "empty"

	if state == "final":
		search_obj1 = re.findall(r' yes | correct | yup | yeah | right | yep | ya ', statement, re.M|re.I)
		search_obj2 = re.findall(r' no | incorrect | nope | nah | wrong | not ', statement, re.M|re.I)

		if search_obj1 != []:
			nlu_dict["info_final_response"] = "yes"
		elif search_obj2 != []:
			nlu_dict["info_final_response"] = "no"
		else:
			nlu_dict["info_final_response"] = "empty"

	return nlu_dict
    
def main():
	global statement, state
	print(first_classifier(" thats not what i want ", "final"))

if __name__ == '__main__':
	main()
