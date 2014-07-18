# -*- coding: utf-8 -*-
from Tkinter import *
from datetime import *
 
class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
 
    def createWidgets(self):
        
        self.branch = Label(self)
        self.branch["text"] = "請選擇院區:"
        #self.branch["font"] = ("Helvetica",16)
        #self.branch["fg"] = "red"
        self.branch.grid(row=0, column=0, columnspan=1)

        self.branchVal = StringVar()
        self.ysvh1 = Radiobutton(self)
        self.ysvh1["text"] = "員山分院"
        self.ysvh1["value"] = "0634070018"
        self.ysvh1["variable"] = self.branchVal
        self.ysvh1.grid(row=1, column=0)
        
        self.ysvh2 = Radiobutton(self)
        self.ysvh2["text"] = "員山鄉門診"
        self.ysvh2["value"] = "2634070010"
        self.ysvh2["variable"] = self.branchVal
        self.ysvh2.grid(row=1, column=1)
        
        self.ysvh3 = Radiobutton(self)
        self.ysvh3["text"] = "宜蘭市區門診"
        self.ysvh3["value"] = "2634010014"
        self.ysvh3["variable"] = self.branchVal
        self.ysvh3.grid(row=1, column=2, columnspan=2)
        
        self.savh1 = Radiobutton(self)
        self.savh1["text"] = "蘇澳分院"
        self.savh1["value"] = "0634030014"
        self.savh1["variable"] = self.branchVal
        self.savh1.grid(row=2, column=0)

        self.savh2 = Radiobutton(self)
        self.savh2["text"] = "蘇澳市區門診"
        self.savh2["value"] = "2634031022"
        self.savh2["variable"] = self.branchVal
        self.savh2.grid(row=2, column=1)

        self.branch = Label(self)
        self.branch["text"] = "自訂院區編號："
        self.branch.grid(row=2, column=2)
        self.branchField = Entry(self)
        self.branchField["width"] = 10
        self.branchField.grid(row=2, column=3)
        
        
        self.IDText = Label(self)
        self.IDText["text"] = "身分證字號："
        self.IDText.grid(row=3, column=0)
        self.IDField = Entry(self)
        self.IDField["width"] = 20
        self.IDField.grid(row=3, column=1, columnspan=2)

        self.BYearText = Label(self)
        self.BYearText["text"] = "民國出生年："
        self.BYearText.grid(row=4, column=0)
        self.BYearField = Entry(self)
        self.BYearField["width"] = 20
        self.BYearField.grid(row=4,column=1, columnspan=2)

        self.betelNutText = Label(self)
        self.betelNutText["text"] = "嚼檳榔現況："
        self.betelNutText.grid(row=5,column=0)

        self.betelNut = StringVar()
        self.betelNut1 = Radiobutton(self)
        self.betelNut1["text"] = "無"
        self.betelNut1["value"] = "0"
        self.betelNut1["variable"] = self.betelNut
        self.betelNut1.grid(row=5, column=1)

        self.betelNut2 = Radiobutton(self)
        self.betelNut2["text"] = "已戒"
        self.betelNut2["value"] = "1"
        self.betelNut2["variable"] = self.betelNut
        self.betelNut2.grid(row=5, column=2)

        self.betelNut3 = Radiobutton(self)
        self.betelNut3["text"] = "目前有嚼檳榔"
        self.betelNut3["value"] = "6"
        self.betelNut3["variable"] = self.betelNut
        self.betelNut3.grid(row=5, column=3)
        

        self.smokeText = Label(self)
        self.smokeText["text"] = "吸菸現況："
        self.smokeText.grid(row=6,column=0)

        self.smoke = StringVar()
        self.smoke1 = Radiobutton(self)
        self.smoke1["text"] = "無"
        self.smoke1["value"] = "0"
        self.smoke1["variable"] = self.smoke
        self.smoke1.grid(row=6, column=1)

        self.smoke1 = Radiobutton(self)
        self.smoke1["text"] = "已戒"
        self.smoke1["value"] = "1"
        self.smoke1["variable"] = self.smoke
        self.smoke1.grid(row=6, column=2)

        self.smoke1 = Radiobutton(self)
        self.smoke1["text"] = "目前有吸菸"
        self.smoke1["value"] = "6"
        self.smoke1["variable"] = self.smoke
        self.smoke1.grid(row=6, column=3)

        self.clear = Button(self)
        self.clear["text"] = "重設"
        self.clear.grid(row=7, column=0)
        self.clear["command"] = self.clearMethod

        self.keyIn = Button(self)
        self.keyIn["text"] = "登錄"
        self.keyIn.grid(row=7, column=3)
        self.keyIn["command"] = self.keyInMethod
 
        self.displayText = Label(self)
        self.displayText["text"] = "菸檳行為登錄小工具 V1.0  開發：丁振新 2014"
        self.displayText.grid(row=8, column=0, columnspan=4)

        #self.displayText2 = Label(self)
        #self.displayText2["text"] = "開發工具：Python 2.7, Tkinter 8.6, Py2exe 0.6.9"
        #self.displayText2.grid(row=9, column=0, columnspan=4)

    def keyInMethod(self):
        if self.checkInput():
            
            if self.branchField.get() :
                branchCode = self.branchField.get()
            else:
                branchCode = self.branchVal.get()

            #開啟檔案
            t = datetime.now()
            
            fname = "oral_"+branchCode+"_"+str(t.year)+"%02d"%(t.month)+".csv"
            f = open( fname ,"a")

            #串接csv字串
            bYear = int(branchCode) + 1911
            sex = self.sexVal(self.IDField.get()[1])
            output = branchCode + "," + self.IDField.get().upper() + ","
            output += str(bYear) + "," + sex + "," + self.betelNut.get() + ","
            output += self.smoke.get() + "," + str(t.year) + "%02d"%(t.month) + "%02d"%(t.day) + "\n"

            #寫入檔案
            f.write(output)

            #顯示登錄完成訊息，並清空除院區以外的資料
            self.displayText["fg"] = "black"
            self.displayText["text"] = time.strftime(datetime.now().time(),"%H:%M:%S")+"登錄成功！"
            f.close()
            self.IDField.delete(0,END)
            self.BYearField.delete(0,END)
            self.betelNut.set("")
            self.smoke.set("")

    def clearMethod(self):
        self.branchVal.set("")
        self.IDField.delete(0,END)
        self.BYearField.delete(0,END)
        self.betelNut.set("")
        self.smoke.set("")

    def checkInput(self):
        #check all fields, if all are valid, return True
        error_msg = "請"
        if not self.branchField.get() and not self.branchVal.get():
            error_msg += "選擇院區或輸入院區代號" 
        elif len(self.IDField.get()) != 10 or int(self.IDField.get()[1]) > 2:
            error_msg += "輸入正確身分證字號"
        elif not self.BYearField.get():
            error_msg += "輸入出生年"
        elif not self.betelNut.get():
            error_msg += "點選檳榔嚼食情形"
        elif not self.smoke.get():
            error_msg += "點選抽菸情形"

        if error_msg != "請" :
            self.displayText["fg"] = "red"
            self.displayText["text"] = error_msg
            return False
        else:
            return True

    def sexVal(self,sex):
        if sex == "1":
            return "M"
        elif sex == "2":
            return "F"
        
if __name__ == '__main__':
    root = Tk()
    root.title("菸檳行為登錄小工具 V1.0")

    #視窗永遠最上層
    root.wm_attributes('-topmost', 1)

    #設定視窗起始位置在畫面右下角
    x = root.winfo_screenwidth()-430
    y = root.winfo_screenheight()-300
    root.geometry("400x220+"+str(x)+"+"+str(y))

    app = GUI(master=root)
    app.mainloop()
