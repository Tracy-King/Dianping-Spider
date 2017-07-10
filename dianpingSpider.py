# coding=utf-8 


import random
import codecs
import re
from bs4 import BeautifulSoup
from urllib import error
import urllib.request
import time
import randomProxy
import emailAlert
import time
import winsound

user_agent_list = [
        'Mozilla/40.0.3 (Macintosh; Intel Mac OS X 10_10_4)',\
        'AppleWebKit/536.5 (KHTML, like Gecko)',\
        'Chrome/19.0.1084.54 Safari/536.5',\
        \
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31',\
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',\
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',\
        \
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',\
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',\
        'Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',\
        \
        'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',\
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',\
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:15.0) Gecko/20120910144328 Firefox/15.0.2',\
        \
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',\
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',\
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13; ) Gecko/20101203',\
        \
        'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',\
        'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',\
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',\
        \
        'Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285',\
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.7pre) Gecko/20070815 Firefox/2.0.0.6 Navigator/9.0b3',\
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',\
    ]

headers = {
    'Host':'www.dianping.com',
    'User-Agent':random.choice(user_agent_list),
    'Refer':'https://www.baidu.com/',
    'Connection': 'Keep-Alive',  
    'Accept': 'text/html, application/xhtml+xml, */*',  
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3', 
    }

url = 'https://www.dianping.com/member/109276339/reviews'

#109276339
#2124372
#13672722
userid = 0

pageNum = 0



def getNumber(href):
    number = ''
    for i in range(len(href)):
        if '0' <= href[i] <= '9':
            number = number + href[i]
    return number


#review = soup.find_all('div', id = re.compile('rev-dpReviewsMostHelpfulAUI'))

def init():
    
    proxy = randomProxy.getRandomProxy('proxy_list.txt')
    print(proxy)
    proxy_handler = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)
    
    
def visit(url):
    try:
        request = urllib.request.Request(url, headers = headers)
        response = urllib.request.urlopen(request)
    except:
        winsound.Beep(400,1000)
        print('Request Error at:' + url)
        return None
    data = response.read()
    data = data.decode('UTF-8')
    soup = BeautifulSoup(data, 'lxml')
    return soup

def list2str(l):
    s = '['
    for i in l:
        for j in range(len(i)):
            if i[j] == '\t' or i[j] == '\n':
                continue
            s = s + str(i[j])
        s = s + ', '
    s = s + ']'
    return s

def iconClassify(href):
    return str(href[9])

def getMoreInfo(more):
    loveStatus = ' '
    birthday = ' '
    constellation = ' '
    if more is not None:
        for s in more.ul.strings:
            if '恋爱' in s:
                loveStatus = '1'
            elif '生日' in s:
                birthday = '1'
            elif '星座' in s:
                constellation = '1'
            elif loveStatus == '1':
                loveStatus = str(s)
            elif birthday == '1':
                birthday = str(s)
            elif constellation == '1':
                constellation = str(s)
    return loveStatus, birthday, constellation

def review(soup, freview):
    
    review = soup.find_all('div', class_ = 'txt J_rptlist')
    #print("Review:", len(review))
    for i in review:
        shopNum = getNumber(str(i.find('a', class_ = 'J_rpttitle')['href']))

        shopAddr = str(i.find('div', class_ = 'mode-tc addres').p.string)

        shopStar = i.find('span', class_ = re.compile('item-rank'))
        if shopStar is not None:
            shopStar = getNumber(str(shopStar['class']))
        else:
            shopStar = '-1'

        avgPrice = i.find('div', class_ = re.compile('comm-rst')).contents
        if len(avgPrice) <= 3:
            avgPrice = '-1'
        else:
            avgPrice = getNumber(str(avgPrice[3]))

        HeartNum = i.find('span', class_ = 'heart-num')
        if HeartNum is not None:
            HeartNum = HeartNum.string
        else:
            HeartNum = '0'
        

        Comment = i.find('div', class_ = re.compile('comm-entry'))
        if Comment is not None:
            Comment = Comment.contents
        else:
            Comment = ['']

        pictureNum = i.find('div', class_ = 'mode-tc comm-photo')
        if pictureNum is not None:
            pictureNum = getNumber(str(pictureNum.a.contents[1]))
        else:
            pictureNum = '0'
            
        favDishes = i.find('div', class_ = re.compile('comm-shop-info'))
        if favDishes is not None:
            favDishes = favDishes.ul.li.contents[2]
            favDishes = re.split('\t\n', str(favDishes))
        else:
            favDishes = []

        reviewTime = getNumber(str(i.find('div', class_ = 'mode-tc info').span.string))

        freview.write('{ShopNum: ' +shopNum
            + ',\tShopAddr: ' + shopAddr
            + ',\tShopStar: ' + shopStar
            + ',\tAvgPrice: ' + avgPrice
            + ',\tLike: ' + HeartNum
            + ',\tComment: ' + list2str(Comment)
            + ',\tPictureNum: ' + pictureNum
            + ',\tDishes: ' + list2str(favDishes)
            + ',\tTime: ' + reviewTime
            +'},\n')
    time.sleep(0.1)

def travelReviews(Userid):
    filename = 'Data/User/' + str(Userid) + '.txt'
    url = 'https://www.dianping.com/member/' + str(Userid) + '/reviews'
    freview = codecs.open(filename,'w',encoding = "utf-8")
    pageNum = 1
    #print("PageNum: ", pageNum)
    soup = visit(url)
    if(validation(soup)):
        freview.close()
        return
    nextPage = soup.find('a', class_ = 'page-next') 
    review(soup, freview)
    

    
    while nextPage is not None:
        pageNum = pageNum + 1
        #print("PageNum: ", pageNum)
        if(pageNum % 5 == 0):
            print("PageNum: ", pageNum)
        freview.close()
        freview = codecs.open(filename,'a',encoding = "utf-8")
        link = url + str(nextPage['href'])
        soup = visit(link)
        if(validation(soup)):
            freview.close()
            return
        review(soup, freview)
        nextPage = soup.find('a', class_ = 'page-next')

    freview.close()

def travelHomepage(Userid):
    url = 'https://www.dianping.com/member/' + str(Userid)
    print(Userid)
    filename = 'Data/UserList.txt'
    soup = visit(url)
    if(validation(soup)):
        return
    
       
    fpage = codecs.open(filename,'a',encoding = "utf-8")

    userName = str(soup.find('h2', class_ = 'name').string)

    iconPic = soup.find('div', class_ = 'pic').a.img['src']
    iconPic = iconClassify(iconPic)

    place = soup.find('span', class_ = 'user-groun')
    if place is not None:
        place = place.string
    else:
        place = ''

    ReviewNum = soup.find('a', href = '/member/' + str(Userid) + '/reviews')
    if ReviewNum is not None:
        ReviewNum = getNumber(ReviewNum.string)
    else:
        ReviewNum = '0'

    WishlistNum = soup.find('a', href = '/member/' + str(Userid) + '/wishlists')
    if WishlistNum is not None:
        WishlistNum = getNumber(WishlistNum.string)
    else:
        WishlistNum = '0'

    CheckinNum = soup.find('a', href = '/member/' + str(Userid) + '/checkin')
    if CheckinNum is not None:
        CheckinNum = getNumber(CheckinNum.string)
    else:
        CheckinNum = '0'

    PhotosNum = soup.find('a', href = '/member/' + str(Userid) + '/photos/album')
    if PhotosNum is not None:
        PhotosNum = getNumber(PhotosNum.string)
    else:
        PhotosNum = '0'

    MylistNum = soup.find('a', href = '/member/' + str(Userid) + '/photos/album')
    if MylistNum is not None:
        MylistNum = getNumber(MylistNum.string)
    else:
        MylistNum = '0'

    GroupsNum = soup.find('a', href = '/member/' + str(Userid) + '/groups')
    if GroupsNum is not None:
        GroupsNum = getNumber(GroupsNum.string)
    else:
        GroupsNum = '0'

    FollowsNum = soup.find('a', href = '/member/' + str(Userid) + '/follows')
    if FollowsNum is not None:
        FollowsNum = FollowsNum.strong.string
    else:
        FollowsNum = '0'

    FansNum = soup.find('a', href = '/member/' + str(Userid) + '/fans')
    if FansNum is not None:
        FansNum = FansNum.strong.string
    else:
        FollowsNum = '0'

    Column = soup.find('div', class_ = 'user-time').contents

    contribute = getNumber(str(Column[1].find('span', id = 'J_col_exp')))
    
    registerTime = getNumber(str(Column[5]))

    more = soup.find('div', class_ = 'user-message')
    loveStatus, birthday, constellation = getMoreInfo(more)

    fpage.write('{UserName: ' + userName
            + ',\tUserId: ' + str(Userid)
            + ',\tIconPic: ' + str(iconPic)
            + ',\tRegisterTime: ' + str(registerTime)
            + ',\tReviewNum: ' + str(ReviewNum)
            + ',\tWishlistNum: ' + str(WishlistNum)
            + ',\tCheckinNum: ' + str(CheckinNum)
            + ',\tPhotosNum: ' + str(PhotosNum)
            + ',\tMylistNum: ' + str(MylistNum)
            + ',\tGroupsNum: ' + str(GroupsNum)
            + ',\tFollowsNum: ' + str(FollowsNum)
            + ',\tFansNum: ' + str(FansNum)
            + ',\tPlace: ' + str(place)    
            + ',\tContribution: ' + str(contribute)
            + ',\tloveStatus: ' + str(loveStatus)
            + ',\tbirthday: ' + str(birthday)
            + ',\tconstellation: ' + str(constellation)
            +'},\n')

    fpage.close()
    
def validation(soup):
    if soup is None:
        winsound.Beep(400,1000)
        return 1
    error = soup.find('div', class_ = "aboutBox errorMessage")
    if error is not None:
        if error.h2.string == "会员不存在！！":
            print("Member invalid")
            winsound.Beep(400,1000)
            return 1
    return 0
    
    
def getUserInfo(Userid):
    travelHomepage(Userid)
    travelReviews(Userid)
    
    
def initUserList(start, end):
    useridList = []
    for i in range(start, end):
        useridList.append(i)
    return useridList
    

'''star = i.find('span', class_ = re.compile('a-icon-alt')).string
    name = i.find('a', class_='noTextDecoration', href=re.compile('profile'))
    comment = i.find('div', class_ = 'a-section')
    vote = i.find('span', class_= 'a-size-base a-color-secondary cr-vote-buttons')
    '''

if (__name__=='__main__'):
    
    init()
    useridList = initUserList(100000,150000)
    for i in useridList:
        startTime = time.time()
        getUserInfo(str(i))
        endTime = time.time()
        print('Time expired:' + str(endTime - startTime))


'''
while(1):
    soup = visit(url)
    review = soup.find_all('div',class_='a-section review')
    print("Review:", len(review))
    f.write(soup.prettify())
    f.close()
    print("PageNum:", pageNum)
    
    for i in review:
        star = i.find('a', class_ = 'a-link-normal')['title']
        time = i.find('span', class_ = re.compile('review-date')).string
        name = i.find('a', class_ = re.compile('author'), href=re.compile('profile')).string
        comment = i.find('span', class_ = re.compile('review-text')).string
        vote = i.find('span', class_= 'review-votes')
        freview.write('{' +str(star)
              + '\t{' + str(time)
              + '\t{' + str(name)
              + '\t{' + str(comment))
        #print(type(vote))
        if(vote is not None):  
              freview.write('{' + str(vote.string) + '}')
        #print(type(vote))
        freview.write('}}}},\n')
        

    nextPage = soup.find('li', class_='a-last')
    if(nextPage is None):
        break

    nextText = str(nextPage.a['href'])

    url =  str('https://www.amazon.cn' + nextText[9:])
    print(url)
    t.sleep(10)
    #break
'''

