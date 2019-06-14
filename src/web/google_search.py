import requests
from bs4 import BeautifulSoup
import math
import sys

def number_of_results(text):
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
  r = requests.get("https://www.google.com/search?q="+text.replace(" ","+"),params={"gl":"in"},headers=headers)
  soup = BeautifulSoup(r.text, "lxml")
  res = soup.find("div", {"id": "resultStats"})
  print(res.text)
  for t in res.text.split():
    try:
      number = float(t.replace(",",""))
      print("{} results for {}".format(number,text))
      return number
    except:
      pass
  raise Exception("Couldn't find a valid number of results on Google")

# N = number_of_results("the")
N = 25270000000.0
N = math.log(N,2)

def normalized_google_distance(w1, w2):
  f_w1 = math.log(number_of_results(w1),2)
  f_w2 = math.log(number_of_results(w2),2)
  f_w1_w2 = math.log(number_of_results(w1+" "+w2),2)

  return (max(f_w1,f_w2) - f_w1_w2) / (N - min(f_w1,f_w2))


def displatDict(text, dictOfElements) :
    print("*************")
    print(text)
    for key , value in dictOfElements.items():
        print(key, " :: ", value)


def get_score(w1,w2):
    score = normalized_google_distance(w1, w2)
    nscore = round(score,2)
    return nscore

def main(w1,w2):
  score = normalized_google_distance(w1,w2)
  print("Score is",round(score,2))
  print("W1='"+ w1+ "' W2='"+ w2+ "'")



if __name__ == '__main__':
    # Usage example
    first_name = "vinod"
    last_names = ["sharma","kapoor","mishra","tyagi","malhotra","singh"]
    name_diction = {}
    for x in last_names:
        name_diction.update({first_name + " " + x : get_score(first_name,x)})
    displatDict("dictionary", name_diction)
