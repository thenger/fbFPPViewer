import urllib.request
import string

#this is the string that leads to the profile picture in the html page
ctrlF = "class=\"profilePicThumb\""


#transform the public url to get the hiden one
def parseUrl(urlSmall):
        place = ""
        name = ""
        res = ""
        if urlSmall.startswith("http://profile.ak.fbcdn.net/hprofile-"):
                iii = urlSmall.index("/",37)
                place = urlSmall[37:iii]
                nameStartIndex = urlSmall.rindex("/") + 1
                name = urlSmall[nameStartIndex:]
                print("name: " + name)
                print("place: " + place)
                print("full pic link:")
                res = "http://sphotos-g.ak.fbcdn.net/hphotos-"+place+"/"+name
                print("http://sphotos-g.ak.fbcdn.net/hphotos-"+place+"/"+name)
                
        else:
                if urlSmall.startswith("https://fbcdn-profile-a.akamaihd.net/hprofile-"):
                        iii = urlSmall.index("/",46)
                        place = urlSmall[46:iii]
                        nameStartIndex = urlSmall.rindex("/") + 1
                        name = urlSmall[nameStartIndex:]
                        print("name: " + name)
                        print("place: " + place)
                        print("full pic link:")
                        res = "http://sphotos-g.ak.fbcdn.net/hphotos-"+place+"/"+name
                        print("http://sphotos-g.ak.fbcdn.net/hphotos-"+place+"/"+name)
                
                else:
                        print("this:")
                        print(urlSmall)
                        print("should be:")
                        print("http://profile.ak.fbcdn.net/hprofile-.....")
                        print("or\nhttps://fbcdn-profile-a.akamaihd.net/hprofile-.....")
                        res = ""
        return res


#test the connection and lauch searchKey
def test (profilUrl):
    print ("Url : "+profilUrl)
    try:
        page = urllib.request.urlopen(profilUrl)
        data = page.read()
        searchKey(data)
    except IOError:
        print ("No internet connexion :c")
        time.sleep(3)

#search the 'ctrlF' string and retrieve profile picture url
def searchKey (htmlPage):
    pos = str(htmlPage).find(ctrlF)
    posSrc = str(htmlPage).find("src=",pos)
    posUrl = posSrc + 5
    endUrl = str(htmlPage).find("\" ",posUrl)
    print (str(htmlPage)[posUrl:endUrl])
    url = str(htmlPage)[posUrl:endUrl]
    urlBig = parseUrl(url)
    
#loop if you want to test multiple profiles
def loopy():
        print ("Hey !")
        print ("(type 'q' to exit)")
        inpt = input("enter the profile url:"+'\n')
        while (inpt != "q" and inpt != "exit"):
                test(inpt)
                inpt = input("again ?"+'\n')
        print("bye")


def main():
        print("boop")
        loopy()
main()

