const app = getApp()
Page({
  data: {
    indicatorDots: false,
    autoplay: false,
    interval: 5000,
    duration: 1000,
    goodsLists:null,
    searchstr:'',
  },
  onLoad: function () {
    //this.getProList();
  },
    /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    console.log("OnShow")
    if(this.data.goodsLists == null)
    {
      return
    }
    var goods_list = this.data.goodsLists
    for(var i = 0; i < goods_list.length;i++)
    {
        if(this.IsInCart(goods_list[i].goodsID) == true)
        {
          goods_list[i].goodsInCart = true
        }
        else{
          goods_list[i].goodsInCart = false
        }
    }
    this.setData({
      goodsLists:goods_list,
    })
  },
  getProList: function(platfrom,keyword){
    var self=this;
    wx.request({
      url: 'http://49.233.195.95:8000/seach',
      method:'GET',
      header:app.GetRequestHeader(),
      data: {
        platform: platfrom,
        keyword:keyword
      },
      success:function(res){
        console.log(res.data)
        
        //判断监测车中是否已添加
        var goods_list = res.data.data.goodsList
        for(var i = 0; i < goods_list.length;i++)
        {
            if(self.IsInCart(goods_list[i].goodsID) == true)
            {
              goods_list[i].goodsInCart = true
            }
            else{
              goods_list[i].goodsInCart = false
            }
        }
        self.setData({
          goodsLists:goods_list,
        })
      },
      fail({errMsg}) {
        console.log('seach fail, err is:', errMsg)
      }
    })
  },

  // 搜索框右侧 事件
  addhandle() {
    //console.log('触发搜索框右侧事件')
  },
  //搜索回调
  endsearchList(ev) {
    let e = ev.detail;
    this.setData({
      searchstr:e.detail.value,
    })
    console.log(e.detail.value,'搜索框回调函数')
    this.getProList("JD",e.detail.value)
  },
  // 取消搜索
  cancelsearch() {
    this.setData({
      searchstr: ''
    })
  },
  //清空搜索框
  activity_clear(e) {

    this.setData({
      searchstr: ''
    })
  },
  addCart(e){
    var goods = e.currentTarget.dataset.goods;
    console.log("4234234234234")
    //检查是否已存在
    for(var i = 0; i < app.globalData.ordercart.length;i++)
    {
      if(app.globalData.ordercart[i]["goodsID"] == goods["goodsID"])
      {
        /*wx.showToast({
          title: '已经在监测车中',
          icon: 'none',
          duration: 2000
        })   */
        return;
      } 
    }
    app.globalData.ordercart.push(goods)
    this.SetGoodsInCart(goods.goodsID)
    wx.showToast({
      title: '添加成功',
      icon: 'success',
      duration: 2000
    })     
    app.SaveOrderCartToStorage()
  },
  SetGoodsInCart:function(goodsID){
    if(this.data.goodsLists == null)
      return;
    for(var i= 0; i < this.data.goodsLists.length;i++)
    {
      if(parseInt(this.data.goodsLists[i].goodsID) == parseInt(goodsID))
      {
        this.data.goodsLists[i].goodsInCart = true
        break;
      }
    }
    this.setData({
      goodsLists : this.data.goodsLists
    })
  },
  IsInCart:function(goodID){
    for(var i= 0; i < app.globalData.ordercart.length;i++)
    {
      if(parseInt(app.globalData.ordercart[i].goodsID) == parseInt(goodID))
      {
        return true
      }
    }
    return false
  }
})