# more info in the json including classes from classes.json
# saves at data/FILENAME_more.json, where FILENAME is the file specified
# run from root, not from helper, to work properly
import json
import sys

DEFAULT_FILENAME = "f2019"

def more_info(filename):
    fp = open("helper/classes.json", "r")
    classes = json.load(fp)
    fp.close()
    class_codes = classes.keys()

    fp = open("data/" + filename + ".json", "r")
    old_dict = json.load(fp)
    old_keys = old_dict.keys()
    new_dict = {}

    for class_code in class_codes: 
        new_dict[class_code] = {}
        new_dict[class_code]['name'] = classes[class_code]
        sub_classes = {}
        for key in old_keys:
            if class_code == key[:4]:
                sub_classes[key] = old_dict[key]
        new_dict[class_code]['classes'] = sub_classes
    
    fp = open("data/" + filename + "_more.json", "w")
    json.dump(new_dict, fp, indent=4)
    fp.close()


ARGS = sys.argv[1:]
if ARGS:
    for arg in ARGS:
        more_info(arg)
else:
    more_info(DEFAULT_FILENAME)    