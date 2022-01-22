import tkinter
from tkinter import ttk

class operatGui():
    """[summary]
    
    """
    tkWindow = None
    nListingNum = 1
    
    def __init__(self):
        """[summary]
        
        Details:
            コンストラクタ
        """
        # ウィンドウの作成
        self.tkWindow = tkinter.Tk()
        
    def getListingNum(self):
        """[summary]

        Details:
            出品数の取得
        Return:
            nListingNum     出品数
        """
        return self.nListingNum

    def getButtonEvent(self, event):
        """[summary]
        
        Details:
            選択された出品数を取得
        """
        self.tkWindow.destroy()
        self.nListingNum = event.num
        

    def selectListings(self):
        """[summary]
        
        Details: 
            出品数の選択
        """
        self.tkWindow.title('出品個数の選択')
        # 幅 x 高さ + x座標 + y座標
        self.tkWindow.geometry('500x300+800+500')
        self.tkWindow.resizable(False, False)
        
        # ウィンドウ情報をアップデートしてサイズ取得
        self.tkWindow.update_idletasks()
        windowWidth = self.tkWindow.winfo_width()
        windowHeight = self.tkWindow.winfo_height()
        # フレームの作成
        tkFrame = tkinter.Frame(self.tkWindow, width=windowWidth*0.7, height=windowHeight*0.7, bg='#9900FF')
        # フレームサイズ(ウィンドウの真ん中に来るように設定)
        x_posFrame = (windowWidth - windowWidth * 0.7) / 2      # 75px
        y_posFrame = (windowHeight - windowHeight * 0.7) / 2    # 45px
        tkFrame.place(x=x_posFrame, y=y_posFrame)
        tkFrame.update_idletasks()
        
        # 出品個数を選択するプルダウンの作成
        lstPullDown = ('1', '2', '3', '4', '5')
        comboBox = ttk.Combobox(tkFrame, values=lstPullDown, state='readonly')
        comboBox.set('1')   # 初期値
        # コンボボックスサイズ（フレームの真ん中に来るように設定 ※幅のみ）
        frameWidth = tkFrame.winfo_width()
        frameHeight = tkFrame.winfo_height()
        x_posComboBox = (frameWidth - frameWidth * 0.5) / 2         # 87.5px
        y_posComboBox = (frameHeight - frameHeight * 0.5) - 32      # 73px
        comboBox.place(x=x_posComboBox, y=y_posComboBox, width=frameWidth/2)
        tkFrame.update_idletasks()
        
        # ボタンの作成
        btnSelect = tkinter.Button(tkFrame, text='選択')
        btnSelect.bind('<1>', self.getButtonEvent)
        x_posButton = (frameWidth - frameWidth * 0.5) / 2     # 87.5px
        btnSelect.place(x=x_posButton, y=y_posComboBox+27+15, width=frameWidth/2)
        
        # 注意点（ウィジェットの配置に使用する「pack」「grid」「place」等は、混在して使用する事ができない）
        
        # ウィンドウのループ処理(※必須 待機処理)
        self.tkWindow.mainloop()
        