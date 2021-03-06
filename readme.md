#國民健康局 菸檳篩檢小工具#

## 簡介 ##
國民健康局要求醫院登錄病人的檳榔與抽煙行為，將其輸出為csv檔格式如下：

| 欄位序 | 欄位名稱 | 長度 | 資料型態 | 說明 |
|--------|----------|------|----------|------|
| 1      |醫院機構代碼| 10 |  文字    | 請填入醫院機構代碼 (程式有提供員山榮民醫院代碼)|
| 2      |身份證統一編號|10|  文字    |若無則填入外籍居留證號碼或護照號碼|
| 3      |出生年 | 4       |  文字    |YYYY(西元年)|
| 4      |性別   | 1       |  文字    |M=男；F=女|
| 5      |嚼檳榔現況 | 1   |  文字    |0:無，1:已戒，6:目前有嚼檳榔|
| 6      |吸煙現況 | 1     |  文字    |0:無，1:已戒，6:目前有吸煙|
| 7      |詢問日期 | 8     |  文字    |YYYYMMDD (西元年月日)|

為幫助員山榮民醫院迅速登錄資料，設計一 Windows 圖形使用者介面使醫院健康管理中心容易登錄菸檳行為，圖形界面如下：

![AltText](http://i.imgur.com/Wf0ICqM.png)

按下登錄以後，會寫入檔案 "oral_醫院機構代碼_資料西元年月.csv"

例如：oral_0123456789_201404.csv

## 編譯事前準備 ##

所需程式： 

Python 2.7 [連結](https://www.python.org/downloads/)

Tkinter 本程式使用的圖形界面 [Tk 8.6.1 Windows Sources 連結](http://www.activestate.com/activetcl/downloads)
[中文安裝教學](http://blog.got7.org/2009/06/atcltk.html)

Py2exe 可以將 python 編譯成 windows 執行檔 [連結](http://www.py2exe.org/)

## 編譯 ##

開啟 windows 命令提示字元 (開始->搜尋 "cmd") 切換到程式資料夾後輸入：

python setup.py py2exe

即可編譯成exe檔，放在dist資料夾內。

## 執行 ##

從dist資料夾內點選 "betel_smoke_tool.exe 即可開啟使用。

如果想要直接執行本程式不想編譯成exe檔，則可以執行 betel_smoke_tool.py 檔即可，不需加入任何程式參數。

## DEMO 程式 ##

編譯好的執行檔可以在這裡下載玩玩看 [連結](http://goo.gl/T72dYq)
