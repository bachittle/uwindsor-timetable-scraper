"""
name: Bailey Chittle
date: Aug 1 2020
program desc: parses a uwindsor PDF document from plain text to an easy to read 
            JSON format. Format looks like this:

course-code {
    name: //name of the course, ex: intro to physics
    type: //lecture or lab?
    sections: [
        {
            number:
            full?
            credits
            datetimes: [
                {
                    days: MWF
                    time: {
                        start
                        end
                    }
                    room
                    prof
                }
            ]
        }
    ]
}

idea:
    remove bloat from document, then have each line have all the details required. 
    This is done with some regex magic (find the course code, read lines and append until a new course appears,
        since (for now) courses only have their code written once)
"""

# imports are global for ease of access
from tika import parser                 # the pdf to text converter
import re                               # regex to parse text to variables
import json                             # variables to json formatter
import sys                              # sys.argv usage when running this in command line with arguments
import os

DATAPATH = "data"

class TimetableScraper:
    # attributes
    filenames = []      # a list of file names, stripped to basename
    pdf_text = []       # this will store a list of strings, which is a pdf text value
    json_results = {}   # this will have the nice json results data, looks like comment above. 

    # methods
    """
    tts constructor

    parameters:
        filename: input filename string to pdf to parse (maybe might do other parsers) "f2020" 
        or array of strings ["f2020", "w2020"]

    """
    def __init__(self, filename=None):
        if filename:
            self.set_filename(filename)

    def __str__(self):
        result = f"filenames: {self.filenames}"
        if self.pdf_text: result += f"\npdf_text: {self.pdf_text}"
        if self.json_results: result += f"\njson_results: {self.json_results}"
        return result
        

    # main things this program can do:
    # - convert a pdf encoded by uwindsor's standards to a text file: pdf_text
    # - read the split text into an easy-to-read and easy-to-use json file: to_json 
    # - create the proper "insert into" queries for a database: to_db


    def to_text(self):
        for filename in filenames:
            raw = parser.from_file(f"{DATAPATH}/pdfs/{self.filename}")
            raw = self._remove_raw_junk(raw)

    # to_json: converts pdf file to json
    def to_json(self):
        for raw in pdf_text:
            courses_dict = {}   # final json result
            i = 0               # index of the line in raw
            for s in raw:
                code = re.findall("[A-Z][A-Z][A-Z][A-Z]- *[0-9][0-9X][0-9X][0-9X][A-Z]*|$", s)[0]
                if code: 
                    print(f"i: {i}")
                    j = i + 1           # j spans up until the next course code's index in raw

                    # while not at next course code, get all data since data for one course
                    #       spans multiple lines
                    while not re.findall("[A-Z][A-Z][A-Z][A-Z]- *[0-9][0-9X][0-9X][0-9X][A-Z]*|$", raw[j])[0]:
                        s += " " + raw[j]
                        j += 1
                        if j >= len(raw): break
                    print(f"s: {s}, raw[j]: {raw[j]}")
                i += 1


    # helper functions
    # set_filename: stores a filename properly by only storing its basename
    #
    # input: string, or a list that eventually has strings
    # output: True if program is successful, false otherwise
    def set_filename(self, filename):
        if type(filename) == str:
            self.filenames.append(os.path.splitext(filename)[0])
            return True
        else:
            # duck typing assuming iterable input. On any error just return false (failed)
            try:
                #self.filenames.extend([os.path.splitext(name)[0] for name in filename])
                self.filenames.extend([os.path.splitext(name)[0] for name in filename])
                return True
            except Exception as e:
                print(e)
                return False
    
    """
    remove_raw_junk: takes a raw file and makes it a list of strings split by new lines (\n)
                    This makes traversing easier, as each line contains a course.
    """
    def _remove_raw_junk(self, raw):
        raw = raw["content"]
        raw = raw[raw.index("Bldg/Room Professor")+len("Bldg/Room Professor"):]
        raw = raw.split("\n")
        i = 0
        for s in raw:
            # removes unnecessary pdf junk
            if s.find("Course Offerings") != -1:
                for j in range(11):
                    # print(raw[i])
                    raw.pop(i)
            i += 1
        return raw
    

if __name__ == "__main__":
    tts = TimetableScraper(sys.argv[1:])
    print(tts)