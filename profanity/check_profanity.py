import requests
#import urllib

def read_text():
    quotes = open("/Users/sunzheng-jie/Desktop/git/udacity/profanity/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    #url = 'http://www.wdylike.appspot.com/?q=' +text_to_check
    connection = requests.get('http://www.wdylike.appspot.com/?q='+ text_to_check)
    print(connection.text)
    connection.close()
    #按照課程的原本的寫法，應該是import urllib.request
    #check_profanity的寫法是
    #f = urllib.parse.quote(text_to_check)
    #connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q='+f)
    #output = connection.read()
    #print(output)
    #可是我怎樣試都只會得到400的錯誤

read_text()