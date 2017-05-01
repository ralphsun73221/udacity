# udacity
這邊是我根據上課的內容做出來的程式

# 搞SMS這個程式的時候出了很多奇妙的問題，順便記錄一下
在twilio的[官方網站上面](www.twilio.com/docs/libraries/python)的程式碼跟我現在這串是一模一樣

但是執行的時候卻一直跟我說

__message: 'E1102:Client is not callable'__

意思就是說call不到Client這串class，本來想說會不會是在安裝Library的時候出了什麼問題，可是沒有啊，他很順利的安裝到目錄底下，我也確定環境有切換成功，後來看了一下安裝的library才發現，rest下面的__ int __.py裡面壓根就沒有Client這個Class，上網Google了一下看到twilio有open source放在Githob[下面](github.com/twilio/twilio-python/blob/master/twilio/rest/__init__.py)乖乖一看不得了，這跟我現在的東西完全不一樣啊XDDD，為了解決問題，索性將整個source直接下回來覆蓋到本機library下面才恢復正常。

官方的文檔有說明，SDK在6.X版之前的寫法跟現在完全不同，之前要寫成

```from twilio.rest import TwilioRestClient```

但在6.X之後就只要

```from twilio.rest import Client```

有報錯的可以將Client改成舊版的寫法就可以了