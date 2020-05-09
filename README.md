# uwindsor-timetable-scraper
scrapes the pdf timetables usually found here: http://www.uwindsor.ca/registrar/541/timetable-information

## how to run

install requirements.txt, basically just tika lol

create a folder in data called pdfs

then, run tts.py. This is how I run it:
```python tts.py w2020 > log.txt```

I include the filename which is stored at: data/pdfs/w2020.pdf

the program will scrape the pdf and convert it to a txt at: data/pdfs/w2020.txt
then it will convert the timetable to json, provided that it follows the same file structure
as each previous file is structured. 
Example is here: http://www.uwindsor.ca/registrar/sites/uwindsor.ca.registrar/files/summer_2020_full_timetable.pdf
