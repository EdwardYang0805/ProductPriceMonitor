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
        console.log(res.data);
        self.setData({
          goodsLists:res.data.data.goodsList,
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
    //检查是否已存在
    for(var i = 0; i < app.globalData.ordercart.length;i++)
    {
      if(app.globalData.ordercart[i]["goodsID"] == goods["goodsID"])
      {
        return;
      } 
    }
    app.globalData.ordercart.push(goods)
    
    app.SaveOrderCartToStorage()
  }
})