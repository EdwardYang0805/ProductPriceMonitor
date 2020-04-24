import os
from . import const_define
from . import jd
from . import wx_api
import json
from . import db_func
from DBModel.models import *
session_openid_map = {}
##################################登陆##########################################
def Do_Login(js_code):
    res = wx_api.code2Session(js_code)

    print(res.content)
    if res.status_code == 200:
        print("11")
        res_json = json.loads(res.content)
        if "errcode" in res_json:
            print("22")
            return None
        if db_func.UserIsExistInDB(res_json["openid"]) == False:
            print("33")
            db_func.AddUserInfoToDB(res_json["openid"], res_json["session_key"])
        return res_json["openid"]
    return None
##################################搜索商品 #########################################
def Do_Seach(openID,platform, keyword):
    if platform == 'JD':
        return jd.Do_Seach(keyword)
    else:
        return


#################################向订单车中添加商品####################################
def AddGoodsToCart(openID,platform,goodsID):
    goods_info = {}
    goods_info["platform"] = platform
    goods_info["goodsid"] = goodsID

    cart_goods_obj = db_func.GetUserMonitorCartGoodsList(openID)
    if cart_goods_obj == None:
        cart_goods_obj = {}
        goods_list = []
        goods_list.append(goods_info)
        cart_goods_obj["goodsList"] = goods_list
        db_func.UpdateGoodsToMonitorCart(openID, cart_goods_obj)
    else:
        cart_goods_obj["goodsList"].append(goods_info)
        db_func.UpdateGoodsToMonitorCart(openID, cart_goods_obj)
    return True

#################################订单车中删除商品####################################
def DelGoodsFromCart(openID,del_json):
    cart_goods_obj = db_func.GetUserMonitorCartGoodsList(openID)
    if cart_goods_obj == None:
        return False
    if del_json["delFlag"] == "all":
        cart_goods_obj["goodsList"].clear()
        db_func.UpdateGoodsToMonitorCart(openID, cart_goods_obj)
    else:
        delIndex =[]
        for delgoods in del_json["delGoods"]:
            for index in range(len(cart_goods_obj["goodsList"])):
                if delgoods["platform"] == cart_goods_obj["goodsList"][index]["platform"] and delgoods["goodsID"] == cart_goods_obj["goodsList"][index]["goodsid"]:
                    delIndex.append(index)

        #移除商品
        for index in delIndex:
            cart_goods_obj["goodsList"].pop(index)
        db_func.UpdateGoodsToMonitorCart(openID, cart_goods_obj)
    return True




