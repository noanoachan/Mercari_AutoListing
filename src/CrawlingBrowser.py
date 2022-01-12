import Const
import time
import os
from selenium.webdriver.support.select import Select


class CrawlingBrowser():
    """[summary]

    Class:
        ブラウザのクロールクラス
    """
    def loginMercari(self, driver, objUserInfo):
        """[summary]

        Details:
            メルカリログイン
        Param:
            driver          ドライバー
            objUserInfo     ユーザー情報
        Return:
            driver  2段階認証突破後のドライバー
        """        
        objConst = Const.CssSelector
        
        try:
            # メルカリを開く
            url = 'https://jp.mercari.com/'
            driver.get(url)
            
            # ログイン
            time.sleep(2)
            driver.find_element_by_css_selector(objConst.BTN_LOGIN).click()
            # メールアドレスでログイン
            time.sleep(2)
            driver.find_element_by_css_selector(objConst.BTN_MAIL_ADDRESS_LOGIN).click()
            
            # ユーザー情報入力
            elmEmail = driver.find_element_by_name('email')
            elmEmail.send_keys(objUserInfo.m_strEmail)
            elmPass = driver.find_element_by_name('password')
            elmPass.send_keys(objUserInfo.m_strPass)
            
            # ログイン実行
            elmLoginBtn = driver.find_element_by_css_selector(objConst.BTN_LOGIN_EXECUTION)
            elmLoginBtn.click()
            time.sleep(3)
            
            # 2段階認証は手動対応
            MERCARI_HOME = 'https://jp.mercari.com/'
            strCurrentURL = driver.current_url
            
            # 現在のURLを取得し、変更されたら突破したと解釈しループを抜ける
            nWaitCount = 0
            while strCurrentURL != MERCARI_HOME:
                time.sleep(2)
                strCurrentURL = driver.current_url
                
                # 3分間、2段階認証が通過される事を待つ
                nWaitCount += 1
                if nWaitCount == 90:
                    print('Error : タイムアウト\n')
                    print('2段階認証の通過が確認できませんでした。\n')
                    
                    # ブラウザ/プログラム終了
                    driver.close()
                    driver.quit()
                    time.sleep(2)
                    exit()
        
        except:
            print('Details : クローリングに失敗しました。')
            raise
            
        return driver
    
    
    def listingProduct(self, driver, objProductInfo, blContinue) -> bool:
        """[summary]

        Details:
            商品を出品
        Param:
            driver              メルカリログイン後のドライバー
            objProductInfo      商品情報
            blContinue          続けて出品するか否か
        Return:
            blRet   True:成功 / False:失敗
        """
        
        blRet = True
        objConst = Const.CssSelector
        
        try:
            # ステータスバー「出品」
            time.sleep(2)
            btmListing = driver.find_element_by_css_selector(objConst.BTN_LISTING)
            btmListing.click()
            
            # メニュー「出品する」
            time.sleep(2)
            btnSell = driver.find_element_by_css_selector(objConst.BTN_SELL)
            btnSell.click()
            time.sleep(2)
            
            # 画像を選択する
            strPicPath = os.path.abspath('..//img/sample.png')
            driver.find_element_by_css_selector(objConst.BTN_PRODUCT_PIC).send_keys(strPicPath)
            time.sleep(2)
            # カテゴリー「1」: 家電・スマホ・カメラ
            elmSelectCategory_1 = driver.find_element_by_css_selector(objConst.CATEGORY_1)
            Select(elmSelectCategory_1).select_by_value(objProductInfo.m_uCat1)
            # カテゴリー「2」: PC/タブレット
            elmSelectCategory_2 = driver.find_element_by_css_selector(objConst.CATEGORY_2)
            Select(elmSelectCategory_2).select_by_value(objProductInfo.m_uCat2)
            # カテゴリー「3」: その他
            elmSelectCategory_3 = driver.find_element_by_css_selector(objConst.CATEGORY_3)
            Select(elmSelectCategory_3).select_by_value(objProductInfo.m_uCat3)
                        
            # ブランド（任意）
            elmSelectBrand = driver.find_element_by_css_selector(objConst.BRAND)
            elmSelectBrand.send_keys(objProductInfo.m_strBrand)
            
            # 商品の状態
            elmSelectProductStatus = driver.find_element_by_css_selector(objConst.PRODUCT_STATUS)
            Select(elmSelectProductStatus).select_by_value(objProductInfo.m_uProductStatus)
            
            # 商品名
            elmInputProductName = driver.find_element_by_css_selector(objConst.PRODUCT_NAME)
            elmInputProductName.send_keys(objProductInfo.m_strProductName)
            
            # 商品の説明
            elmInputProductExplanation = driver.find_element_by_css_selector(objConst.PRODUCT_EXPLANATION)
            elmInputProductExplanation.send_keys(objProductInfo.m_strProductExplanation)
            
            # 配送料の負担
            elmSelectBurdenOfShippingCharges = driver.find_element_by_css_selector(objConst.SELECT_BURDEN_OF_SHIPPING_CHARGES)
            Select(elmSelectBurdenOfShippingCharges).select_by_value(objProductInfo.m_uBurdenOfShippingCharges)
            
            # 配送の方法
            elmSelectDeliveryMethod = driver.find_element_by_css_selector(objConst.SELECT_DELIVERY_METHOD)
            Select(elmSelectDeliveryMethod).select_by_value(objProductInfo.m_uDeliveryMethod)
            
            # 配送元の地域
            elmSelectDeliveryArea = driver.find_element_by_css_selector(objConst.SELECT_DELIVERY_AREA)
            Select(elmSelectDeliveryArea).select_by_value(objProductInfo.m_uDeliveryArea)
            
            # 配送までの日数
            elmSelectDaysToDelivery = driver.find_element_by_css_selector(objConst.SELECT_DAYS_TO_DELIVERY)
            Select(elmSelectDaysToDelivery).select_by_value(objProductInfo.m_uDaysToDelivery)
            
            # 販売価格
            elmInputSellingPrice = driver.find_element_by_css_selector(objConst.INPUT_SELLING_PRICE)
            elmInputSellingPrice.send_keys(objProductInfo.m_uSellingPrice)
            
            # 出品する
            btnLastSell = driver.find_element_by_css_selector(objConst.SEND_SELL)
            btnLastSell.click()
            
            # 続けて出品する
            if blContinue:
                btnContinueSell = driver.find_element_by_css_selector(objConst.CONTINUE_SELL)
                btnContinueSell.click()
        
        except:
            blRet = False
            raise
        
        return blRet