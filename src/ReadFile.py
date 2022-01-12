import Const
import xml.etree.ElementTree as ET


class ReadXml:
    """[summary]
    
    Class:
        xmlファイル読み込み
    """
    
    def readUserInfo(self, objUserInfo) -> bool:
        """[summary]
        
        Details:
            ユーザー情報の取得
        Param:
            ユーザー情報
        Return:
            blRet   True:成功 / False:失敗
        """
        blRet = True
        try:
            tree = ET.parse('./doc/UserInfo.xml')
            root = tree.getroot()
            for userInfo in root.findall('UserInfo'):
                objUserInfo.setEmail(userInfo.find('Email').text)
                objUserInfo.setPass(userInfo.find('Pass').text)
            
            if objUserInfo.getEmail() == '' or objUserInfo.getPass() == '':
                print('Error : 各要素が空です。 .xmlに適切な情報を入力して下さい。\n')
                blRet = False
                
        except Exception:
            blRet = False
            print('Details : .xmlの取得に失敗しました。\n')
            raise

        return blRet
    
    
    # def checkElement(self, objProductInfo) -> bool:
    #     """[summary]

    #     Param:
    #         objProductInfo      商品情報
    #     Return:
    #         blRet   True:成功 / False:失敗
    #     """
    
    
    def readProductInfo(self, objProductInfo) -> bool:
        """[summary]

        Details:
            商品情報の取得
        Param:
            objProductInfo      商品情報
        Returns:
            blRet   True:成功 / False:失敗
        """
        blRet = True
        objXmlElement = Const.XmlElement
        try:
            tree = ET.parse('./doc/ProductInfo.xml')
            root = tree.getroot()
            for category in root.findall(objXmlElement.CATEGORY_TAG):
                objProductInfo.m_uCat1 = category.find(objXmlElement.CATEGORY_1).text
                objProductInfo.m_uCat2 = category.find(objXmlElement.CATEGORY_2).text
                objProductInfo.m_uCat3 = category.find(objXmlElement.CATEGORY_3).text
            for other in root.findall(objXmlElement.OTHER_TAG):
                objProductInfo.m_strBrand = other.find(objXmlElement.BRAND).text
                objProductInfo.m_uProductStatus = other.find(objXmlElement.PRODUCT_STATUS).text
                objProductInfo.m_strProductName = other.find(objXmlElement.PRODUCT_NAME).text
                objProductInfo.m_uBurdenOfShippingCharges = other.find(objXmlElement.BURDEN_OF_SHIPPING_CHARGES).text
                objProductInfo.m_uDeliveryMethod = other.find(objXmlElement. DELIVERY_METHOD).text
                objProductInfo.m_uDeliveryArea = other.find(objXmlElement.DELIVERY_AREA).text
                objProductInfo.m_uDaysToDelivery = other.find(objXmlElement.DAYS_TO_DELIVERY).text
                objProductInfo.m_uSellingPrice = other.find(objXmlElement.SELLING_PRICE).text
                
        except Exception:
            blRet = False
            print('Details : .xmlの取得に失敗しました。\n')
            raise

        return blRet
    
    
    
class ReadText:
    """[summary]
    
    Class:
        textファイル読み込み
    """
    
    def readText(self, objProductInfo) -> bool:
        """[summary]
        
        Details:
            商品説明取得
        Param:
            objProductInfo      商品情報
        Return:
            blRet   True:成功 / False:失敗
        """
        blRet = True
        try:
            with open('./doc/DescriptionItem.txt') as f:
                objProductInfo.m_strProductExplanation = f.read()
            
            if objProductInfo.m_strProductExplanation == '':
                print('Error : 商品説明が空です。 入力して下さい。\n')
                blRet = False
        
        except Exception:
            blRet = False
            print('Details : .txtの取得に失敗しました。')
            raise
        
        return blRet
    