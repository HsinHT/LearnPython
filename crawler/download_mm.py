import urllib.request
import os
import base64
import time

def get_base64EncodeStr(pageNum):
    # 取得刪除 \x00 後，base64 編碼的 bytes-like
    getPageByteslike = pageNum.to_bytes(16, 'big').decode('ascii').strip().strip('\x00')

    # 將 base64 編碼的 bytes-like 轉成字串
    encodePageStr = base64.encodebytes(str.encode(getPageByteslike))

    return str(encodePageStr).replace('b\'', '').replace('\\n\'', '')

def url_open(url):
    global html
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept-Encoding':'*',
        'Connection':'keep-alive'
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
        html = response.read()
        response.close()
    except urllib.error.URLError as e:
        print(e.reason)

    time.sleep(1)

    return html

def get_page(url):
    get_page_html = url_open(url).decode('utf-8')

    #<span class="current-comment-page">[5]</span>
    x = get_page_html.find('current-comment-page') + 23
    y = get_page_html.find(']', x)

    # 取得頁面數
    pageCurrNum = get_page_html[x:y]

    #<a title="Older Comments" href="//jandan.net/ooxx/MjAxOTEwMTMtNA==#comments" class="previous-comment-page">下一页</a>
    a = get_page_html.find('Older Comments" href="//jandan.net/ooxx/') + 40
    b = get_page_html.find('#comments', a)

    # 取得 base64 編碼的字串
    base64PrevPageStr = get_page_html[a:b]

    # 將字串轉乘 bytes-like
    base64PrevPageByteslike = bytes(base64PrevPageStr, 'utf-8')

    # 取得 base64 解碼的 bytes-like
    decodePrevPage = base64.decodebytes(base64PrevPageByteslike)

    # 將 bytes-like 轉成 int
    getPrevPageNumInt = int.from_bytes(decodePrevPage, byteorder='big')

    # 取得當前頁面的整數
    getCurrPageNumInt = (getPrevPageNumInt + 1)

    # 取得當前頁面的 base64 編碼字串
    newEncodePageStr = get_base64EncodeStr(getCurrPageNumInt)

    base64EncodeDict = {}
    # 將當前頁面的 base64 編碼字串儲存
    base64EncodeDict[pageCurrNum] = newEncodePageStr

    # 將每個頁面的 base64 編碼字串儲存
    for i in range(int(pageCurrNum)):
        newEncodePageStr = get_base64EncodeStr(getCurrPageNumInt - i)
        base64EncodeDict[str(int(pageCurrNum) - i)] = newEncodePageStr

    return base64EncodeDict

def find_img(url):
    find_img_html = url_open(url).decode('utf-8')
    img_addrs = []

    a = find_img_html.find('img src=')

    while a != -1:
        b = find_img_html.find('.jpg', a, a+255)
        if b != -1:
            img_addrs_str = 'http:' + find_img_html[a+9:b+4]

            # 將圖片網址存儲
            img_addrs.append(img_addrs_str)
        else:
            b = a + 9

        a = find_img_html.find('img src=', b)

    return img_addrs

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        # 將圖片存檔
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder='OOXX', pages=10):
    # 建立存儲目錄
    os.makedirs(folder, exist_ok=True)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    # 取得每個頁面 base64 編碼字串
    base64Dict = get_page(url)

    for i in range(len(base64Dict), 0, -1):
        # 取得頁面網址
        page_url = url + base64Dict[str(i)] + '#comments'
        # 取得圖片網址
        img_addrs = find_img(page_url)
        # 存儲圖片
        save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()
