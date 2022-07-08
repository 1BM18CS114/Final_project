import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import re

#Removes non-alphabetic characters:
def text_clean(text):

    try:
        #ORDER OF REGEX IS VERY VERY IMPORTANT!!!!!!
        
        text=re.sub("(\\t)", ' ', str(text)).lower() #remove escape charecters
        text=re.sub("(\\r)", ' ', str(text)).lower() 
        text=re.sub("(\\n)", ' ', str(text)).lower()
        
        text=re.sub("(__+)", ' ', str(text)).lower()   #remove _ if it occors more than one time consecutively
        text=re.sub("(--+)", ' ', str(text)).lower()   #remove - if it occors more than one time consecutively
        text=re.sub("(~~+)", ' ', str(text)).lower()   #remove ~ if it occors more than one time consecutively
        text=re.sub("(\+\++)", ' ', str(text)).lower()   #remove + if it occors more than one time consecutively
        text=re.sub("(\.\.+)", ' ', str(text)).lower()   #remove . if it occors more than one time consecutively
        
        text=re.sub(r"[<>()|&©ø\[\]\'\",;?~*!]", ' ', str(text)).lower() #remove <>()|&©ø"',;?~*!
        
        text=re.sub("(mailto:)", ' ', str(text)).lower() #remove mailto:
        text=re.sub(r"(\\x9\d)", ' ', str(text)).lower() #remove \x9* in text
        text=re.sub("([iI][nN][cC]\d+)", 'INC_NUM', str(text)).lower() #replace INC nums to INC_NUM
        text=re.sub("([cC][mM]\d+)|([cC][hH][gG]\d+)", 'CM_NUM', str(text)).lower() #replace CM# and CHG# to CM_NUM
        
        
        text=re.sub("(\.\s+)", ' ', str(text)).lower() #remove full stop at end of words(not between)
        text=re.sub("(\-\s+)", ' ', str(text)).lower() #remove - at end of words(not between)
        text=re.sub("(\:\s+)", ' ', str(text)).lower() #remove : at end of words(not between)
        
        text=re.sub("(\s+.\s+)", ' ', str(text)).lower() #remove any single charecters hanging between 2 spaces
        
        #Replace any url as such https://abc.xyz.net/browse/sdf-5327 ====> abc.xyz.net
        try:
            url = re.search(r'((https*:\/*)([^\/\s]+))(.[^\s]+)', str(text))
            repl_url = url.group(3)
            text = re.sub(r'((https*:\/*)([^\/\s]+))(.[^\s]+)',repl_url, str(text))
        except:
            pass #there might be emails with no url in them
        

        
        text = re.sub("(\s+)",' ',str(text)).lower() #remove multiple spaces
        
        #Should always be last
        text=re.sub("(\s+.\s+)", ' ', str(text)).lower() #remove any single charecters hanging between 2 spaces
    except:
        text = None

    yield text


