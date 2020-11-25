# note: i would recommend redirecting stdout to a log file
from tika import parser
import re
import json
import sys


def scrape_timetable(filename):
    print("---------------")
    print(filename)
    print("---------------")
    # parses uses tika apache pdf bindings
    raw = parser.from_file("data/pdfs/"+filename+".pdf")

    raw = raw["content"]
    raw = raw[raw.index("Bldg/Room Professor")+len("Bldg/Room Professor"):]
    raw = raw.split("\n")
    i = 0
    for s in raw:
        # removes unnecessary pdf junk
        if s.find("Course Offerings") != -1:
            for j in range(11):
                #print(raw[i])
                raw.pop(i)
        i += 1

    courses_dict = {}
    i = 0    
    # organizes pdf using regex into json
    for s in raw:
        code = re.findall("[A-Z][A-Z][A-Z][A-Z]- *[0-9][0-9X][0-9X][0-9X][A-Z]*|$", s)[0]
        if code: # should almost always work
            print(f"i: {i}")
            j = i + 1
            while not re.findall("[A-Z][A-Z][A-Z][A-Z]- *[0-9][0-9X][0-9X][0-9X][A-Z]*|$", raw[j])[0]:
                s += " " + raw[j]
                j += 1
                if j >= len(raw): break
            print(f"s: {s}, raw[j]: {raw[j]}")
        i += 1

    fp = open("data/pdfs/"+filename+".txt", "w")
    fp.write("\n".join(raw))
    fp.close()

    fp = open("data/"+filename+".json", "w")
    json.dump(courses_dict, fp, indent=4)
    fp.close()

    fp = open("data/api.txt", "a")
    fp.write(filename)
    fp.close()

# allows arguments except for 1st argument (which is just what program is running...)
ARGS = sys.argv[1:]
# if no arguments given, run default file
DEFAULT_FILENAME = "f2020"

if ARGS:
    for arg in ARGS:
        scrape_timetable(arg)
else:
    scrape_timetable(DEFAULT_FILENAME)