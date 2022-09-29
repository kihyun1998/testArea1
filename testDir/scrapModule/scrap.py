#requests import
from requests import get
#bs4 import
from bs4 import BeautifulSoup

def notices(targetUrl):
    #targetURL
    base_url=targetUrl

    #응답 값은 response에
    response = get(f"{base_url}")

    #응답에 실패하면
    if response.status_code != 200:
        #그냥 print
        print("Can't")
    #응답에 성공하면
    else:
        #결과 저장 리스트
        results=[]
        #BeautifulSoup 생성해서 soup으로 사용
        soup=BeautifulSoup(response.text,"html.parser")
        #td태그들 값을 저장(find_all)
        tds = soup.find_all('td',class_="_artclTdTitle")
        for td in tds:
            #td 중 a태그 추출
            anchors = td.find_all('a')
            #추출한 a태그 정제
            for anchor in anchors:
                link = f"https://community.bu.ac.kr{anchor['href']}"
                #a태그 속 title이 저장된 span태그 find하기
                title = anchor.find('span')
                rst={
                    'title':title.string,
                    'link':link
                }
                results.append(rst)
        return results