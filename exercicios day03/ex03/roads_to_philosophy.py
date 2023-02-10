import sys, requests
from bs4 import BeautifulSoup

def request_wikipedia_page(page: str):

    session = requests.Session()    
    url = f"https://en.wikipedia.org/wiki/{page.strip().replace(' ','_')}"

    result = session.get(url=url)
    session.close()
    if result.status_code == 200:
        return True, result.text
    elif result.status_code == 404:
        return False, "DeadEnd"
    else:
        return False, f"ERRO ao realizar a requisição {result.status_code}"



def get_first_link(html):
    soup = BeautifulSoup(html,'html.parser')
    print(str(soup.find(name="title")).replace(" - Wikipedia</title>","").replace("<title>",""))
    soup = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for paragraph in soup.find_all("p", recursive=False):
        for link in paragraph.find_all("a"):
            ref = link.get("href")
            if "#" not in ref and ":" not in ref and "//" not in ref:
                return ref



def main():
    target_page = "/wiki/Philosophy"
    count = 0
    error = ""
    pages_array = []
    if len(sys.argv) == 2:
        link = f"/wiki/{sys.argv[1]}"
        while link != target_page:  
            if link not in pages_array:
                try:
                    page = request_wikipedia_page(link.split("/")[2])
                except:
                    error = "DeadEnd"
                    break
                if page[0]:
                    pages_array.append(link)
                    link = get_first_link(str(page[1]))
                    count += 1
                else:
                    error = page[1]
                    break
            else:
                error = "Loop"
                break
            
        if error == "":  
            print("Philosophy")      
            print(f"{count-1} roads from {sys.argv[1]} to philosophy !")
        elif error == "DeadEnd":
            print("It's a dead end !")
        elif error == "Loop":
            print("It leads to an infinite loop !")
        else:
            print(error)

    else:
        print("Número de parâmetros incorreto")


if __name__ == '__main__':
    main()