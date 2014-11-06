import BeautifulSoup
import string

def parse_things():
    f = open("baklava-recipe", 'r')
    soup = BeautifulSoup.BeautifulSoup(f)
    ingr = soup.findAll("li",{"itemprop":"ingredients"})
    
    for item in ingr:
        item = str(item)

        item.replace("<a href", " ").replace("</a>,"," ")


        item = BeautifulSoup.BeautifulSoup(item)
        single_ing = item.getText()
        single_ing = single_ing.encode('ascii')
        print single_ing



def main():
    parse_things()

if __name__=="__main__":
    main()

