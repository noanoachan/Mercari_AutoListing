import CrawlingBrowser
import Info
import ReadFile
from typing import Iterator
from selenium import webdriver


def main(nListingProductNum):
    """[summary]
    
    Details:
        main関数
    Param:
        nListingProductNum  出品数
    """
    try:
        objReadXml = ReadFile.ReadXml()
        
        # xmlからユーザー情報を取得
        objUserInfo = Info.UserInfo()
        if not objReadXml.readUserInfo(objUserInfo):
            exit()
        # xmlから商品情報を取得
        objProductInfo = Info.ProductInfo()
        if not objReadXml.readProductInfo(objProductInfo):
            exit()
            
        objReadText = ReadFile.ReadText()
        # textから商品説明を取得
        if not objReadText.readText(objProductInfo):
            exit()
                
    except Exception as e:
        print('Exception : ' + repr(e))
        exit()
        
    # メルカリへアクセス
    driver = webdriver.Chrome()
    try:
        objCrawlingBrowser = CrawlingBrowser.CrawlingBrowser()
        objCrawlingBrowser.loginMercari(driver, objUserInfo)

        for num in range(nListingProductNum):
            nRemainingCount = nListingProductNum
            if nRemainingCount > 1:
                blContinue = True
            else:
                blContinue = False
            try:
                if objCrawlingBrowser.listingProduct(driver, objProductInfo, blContinue):
                    print(f'{num + 1}品目の出品が完了しました。')
                else:
                    print('Warning : 出品に失敗した商品があります。')
                
                #「続けて出品する」商品残数
                nRemainingCount -= 1

            except Exception as e:
                print(f'Details : {num + 1}品目の出品が失敗しました。')
                print('Exception : ' + repr(e))
                pass

    except Exception as e:
        print('Exception : ' + repr(e))

        # ブラウザ終了
        driver.close()
        driver.quit()
        exit()

    # ブラウザ終了
    driver.close()
    driver.quit()


if __name__ == '__main__':
    # if len(sys.argv) != 0:
    #     print('Error : コマンドライン引数が入力されていません。\n')
    #     print('商品を幾つ出品するかを数値で指定して下さい。（※上限:5つ）\n')
    #     exit()

    # elif len(sys.argv) > 1:
    #     print('Error : 引数は1つだけ入力して下さい。\n')
    #     exit()

    # else:
    #     if int(sys.argv[0]) > 5:
    #         print('Error : 一度に出品可能な個数は5つまでです。\n')
    #         print('引数を「5」以下で再入力し、実行して下さい。\n')    
    #         exit()

    # main(sys.argv[0])

    main(2)
