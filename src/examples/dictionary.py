
def displatDict(text, dictOfElements) :
    print("*************")
    print(text)
    for key , value in dictOfElements.items():
        print(key, " :: ", value)

first_name = "vinod"
last_names = ["sharma","kapoor","mishra","tyagi","malhotra","singh"]
name_dic = {}
for x in last_names:
    name_dic.update({first_name + " " + x : 2})
#newlist = [first_name + x for x in last_names]
#print(newlist)
displatDict("Dictionary from two Lists ", name_dic)

#zipbObj = zip(first_name, last_names)
#dictOfWords = dict(zipbObj)
#displatDict("Dictionary from two Lists ", dictOfWords)
