# chatbot
`2018-TOC`
## Introduction
* 可以查詢系上教授lab的網址和照片
* 可以輸入姓(Last Name)，會回應相同姓的教授名字
* 輸入 hello , 會回應 Hello!!!
* 輸入 help , 會回應操作提示
## FSM
![picture](https://github.com/ArielWu0203/chatbot/blob/master/fsm.png)

## Interact with the chatbot
1. input : `help`</br>
    output : `Input name or search or hello or help`
2. input : `hello`</br>
    output : `Hello!!!`
3. input : `search`</br>
    output : `Input Last name`</br>
    input : `蘇`</br>
    output : `蘇文鈺 \ 蘇銓清 \`</br>
4. input : `search`</br>
    output : `Input Last name`</br>
    input : `哈`</br>
    output : `Search nothing`</br>
5. input : `name`</br>
    output : `Input teacher's name`</br>
    input : `蘇文鈺`</br>
    output : `choose the button
              Picture
              lab website`</br>
    choose Picture button</br>
    output : [picture]
 6. input : `name`</br>
    output : `Input teacher's name`</br>
    input : `莊坤達`</br>
    output : `choose the button
              Picture
              lab website`</br>
    choose lab website button</br>
    output : [http://dlt.csie.ncku.edu.tw]


## parsing website
* 使用 BeautifulSoup , 抓取教授的名字、lab website、image
* [link](https://github.com/ArielWu0203/chatbot/blob/master/bug_test.py)
## database
* 使用 sqlite3 , 將教授的名字都存進資料庫中(先用爬蟲抓取所有教授的名字，再放進資料庫中)
* [link](https://github.com/ArielWu0203/chatbot/blob/master/test_data.py)
## 傳送圖片
* [link](https://github.com/ArielWu0203/chatbot/blob/master/utils.py)
```=json
curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"1254459154682919"
  },
  "message":{
    "attachment":{
      "type":"image", 
      "payload":{
        "url":"http://www.messenger-rocks.com/image.jpg", 
        "is_reusable":true
      }
    }
  }
}' "https://graph.facebook.com/v2.6/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
```
## 傳送回傳按鈕
```
curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"<PSID>"
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":"Try the postback button!",
        "buttons":[
          {
            "type":"postback",
            "title":"Postback Button",
            "payload":"DEVELOPER_DEFINED_PAYLOAD"
          }
        ]
      }
    }
  }
}' "https://graph.facebook.com/v2.6/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
```
