class UserInfo:
    """[summary]
    
    Class:
        ユーザー情報クラス
    """
    m_strEmail = ''     # メールアドレス
    m_strPass = ''      # パスワード
    
            
    def setEmail(self, strEmail: str):
        """[summary]

        Details:
            メールアドレスの設定
        Param:
            strEmail    メールアドレス
        """
        self.m_strEmail = strEmail
        
        
    def getEmail(self) -> str:
        """[summary]
        
        Details:
            メールアドレスの取得
        Return:
            メールアドレス
        """
        return self.m_strEmail
    
    
    def setPass(self, strPass: str):
        """[summary]
        
        Details:
            パスワードの設定
        Param:
            strPass     パスワード
        """
        self.m_strPass = strPass
        
        
    def getPass(self) -> str:
        """[summary]

        Details:
            パスワードの取得
        Return:
            strPass     パスワード
        """
        return self.m_strPass
    
    
class ProductInfo:
    """[summary]

    Class:
        商品情報クラス
    """
    # カテゴリー
    m_uCat1 = None
    m_uCat2 = None
    m_uCat3 = None
    # ブランド
    m_strBrand = ''
    # 商品の状態
    m_uProductStatus = None
    # 商品名
    m_strProductName = ''
    # 商品説明
    m_strProductExplanation = ''
    # 配送料の負担
    m_uBurdenOfShippingCharges = None
    # 配送の方法
    m_uDeliveryMethod = None
    # 配送元の地域
    m_uDeliveryArea = None
    # 配送までの日数
    m_uDaysToDelivery = None
    # 販売価格
    m_uSellingPrice = None