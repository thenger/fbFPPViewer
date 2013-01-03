import string

def parseUrl(urlSmall):
        place = ""
        name = ""
        if urlSmall.startswith("http://"):
                urlSmall = urlSmall[7:]
        if urlSmall.startswith("profile.ak.fbcdn.net/hprofile"):
                iii = urlSmall.index("/",30)
                place = urlSmall[30:iii]
                nameStartIndex = urlSmall.rindex("/") + 1
                name = urlSmall[nameStartIndex:]
                print("name: " + name)
                print("full pic link:")
                print("http://sphotos-g.ak.fbcdn.net/hphotos-"+place+"/"+name)
        else:
                print("this:")
                print(urlSmall)
                print("should be:")
                print("profile.ak.fbcdn.net/hprofile.....")

def loopy():
        print ("Hey !")
        print ("(type 'q' to exit)")
        inpt = input("enter the url of the tiny profile picture:"+'\n')
        while (inpt != "q" and inpt != "exit"):
                parseUrl(inpt)
                inpt = input("again ?"+'\n')
        print("bye")


def main():
        print("boop")
        loopy()
main()

