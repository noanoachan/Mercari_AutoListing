import os
    
    
class CssSelector:
    """[summary]
    
    Class:
        メルカリ内クローリング時のCSSセレクター
    """
    # ログイン
    BTN_LOGIN = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-navigation-top-menu-item:nth-child(2) > mer-text'
    # メールアドレスでログイン
    BTN_MAIL_ADDRESS_LOGIN = '#root > div > div > div > main > div > div > div > div > mer-button.style_loginButton__1-1k6.mer-spacing-b-24.style_email__1PIYq > a'
    # ログイン実行
    BTN_LOGIN_EXECUTION = '#root > div > div > div > main > div > div > form > mer-button > button'
    
    # ステータスバー「出品」
    BTN_LISTING = '#gatsby-focus-wrapper > div > div > header > mer-navigation-top > nav > mer-navigation-top-menu > mer-button > a'
    # メニュー「出品する」
    BTN_SELL = '#main > section:nth-child(2) > div > a.Home__ListItemButton-sc-14s4t2-0.eBlAra.mer-spacing-r-16'
    
    # 画像を選択する
    BTN_PRODUCT_PIC = '#main > form > section:nth-child(1) > div > div.FileUploader__InputContainer-sc-f66k10-3.cCfDjr > input[type=file]'
    # カテゴリー「1」
    CATEGORY_1 = '#main > form > section:nth-child(2) > mer-select:nth-child(2) > div > label > div.mer-select > select'
    # カテゴリー「2」
    CATEGORY_2 = '#main > form > section:nth-child(2) > mer-select:nth-child(3) > div > div.mer-select > select'
    # カテゴリー「3」
    CATEGORY_3 = '#main > form > section:nth-child(2) > mer-select:nth-child(4) > div > div.mer-select > select'
    # ブランド（任意）
    BRAND = '#main > form > section:nth-child(2) > mer-autocomplete > mer-text-input > div > label > div.mer-text-input-container > input'
    # 商品の状態
    PRODUCT_STATUS = '#main > form > section:nth-child(2) > mer-select:nth-child(6) > div > label > div.mer-select > select'
    # 商品名
    PRODUCT_NAME = '#main > form > section:nth-child(3) > mer-text-input > div > label > div.mer-text-input-container > input'
    # 商品の説明（任意）
    PRODUCT_EXPLANATION = '#main > form > section:nth-child(3) > mer-textarea > div > label > textarea.input-node'
    # 配送料の負担
    SELECT_BURDEN_OF_SHIPPING_CHARGES = '#main > form > section:nth-child(4) > div:nth-child(2) > mer-select:nth-child(1) > div > label > div.mer-select > select'
    # 配送の方法
    SELECT_DELIVERY_METHOD = '#main > form > section:nth-child(4) > div:nth-child(2) > mer-select.mer-spacing-t-24 > div > label > div.mer-select > select'
    # 配送元の地域
    SELECT_DELIVERY_AREA = '#main > form > section:nth-child(4) > mer-select:nth-child(3) > div > label > div.mer-select > select'
    # 配送までの日数
    SELECT_DAYS_TO_DELIVERY = '#main > form > section:nth-child(4) > mer-select:nth-child(4) > div > label > div.mer-select > select'
    # 販売価格
    INPUT_SELLING_PRICE = '#main > form > section:nth-child(5) > div:nth-child(2) > mer-text-input > div > label > div.mer-text-input-container > input'
    
    # 出品する（最終）
    SEND_SELL = '#main > form > div.layout__FlexWrapper-sc-1lyi7xi-8.eJmmiy > mer-button:nth-child(1) > button'
    # 続けて出品する
    CONTINUE_SELL = 'body > mer-information-popup > div:nth-child(2) > mer-button:nth-child(1) > a'
    
    
class XmlElement:
    """[summary]
        
    Class:
        商品情報のXML要素
    """
    # カテゴリー要素
    CATEGORY_TAG = 'ProductInfo/Category'
    # カテゴリ「1」
    CATEGORY_1 = 'Cat1'
    # カテゴリ「2」
    CATEGORY_2 = 'Cat2'
    # カテゴリ「3」
    CATEGORY_3 = 'Cat3'
    
    # その他詳細要素
    OTHER_TAG = 'ProductInfo'
    # ブランド
    BRAND = 'Brand'
    # 商品の状態
    PRODUCT_STATUS = 'ProductStatus'
    # 商品名
    PRODUCT_NAME = 'ProductName'
    # 配送料の負担
    BURDEN_OF_SHIPPING_CHARGES = 'BurdenOfShippingCharges'
    # 配送の方法
    DELIVERY_METHOD = 'DeliveryMethod'
    # 配送元の地域
    DELIVERY_AREA = 'DeliveryArea'
    # 配送までの日数
    DAYS_TO_DELIVERY = 'DaysToDelivery'
    # 販売価格
    SELLING_PRICE = 'SellingPrice'