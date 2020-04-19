const app = getApp()
Page({
  data: {
    indicatorDots: false,
    autoplay: false,
    interval: 5000,
    duration: 1000,
    proLists:null
  },
  onLoad: function () {
    this.getProList();
  },
  getProList: function(){
    var self=this;
    wx.request({
      url: 'http://49.233.195.95:8000/seach',
      method:'GET',
      data: {
        platform: "JD",
        keyword:"iphone"
      },
      success:function(res){
        console.log(res.data);
        self.setData({
          proLists:res.data.data.goodsList,
        })
        //下载图片
        /*var goodsList = self.proLists
        goodsList.forEach(function (item, index) {
          wx.downloadFile({
            url:'http://49.233.195.95:8000/img/' + item.goodsImg,
            success:function(res){
              console.log(res.data);
              goodsList[index].goodsImg = res.tempFilePath
            }
            })
        })
        self.setData({
          proLists:goodsList
        })*/
      },
      fail({errMsg}) {
        console.log('downloadFile fail, err is:', errMsg)
      }
    })
  }
})