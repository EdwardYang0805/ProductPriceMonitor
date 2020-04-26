// pages/ordercart.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data:{
    goods:[],
    selected:true,
    selectedAll:true,
    totalPrice:0.0
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    this.loadGoods();
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },

  loadGoods:function(){
    var goods = app.globalData.ordercart
    var totalPrice=0;
    for(var i=0;i<goods.length;i++){
      var good = goods[i];
      totalPrice += parseFloat(good.goodsPrice);
    }
    this.setData({goods: goods, totalPrice: totalPrice});
  },
  checkboxChange:function(e){
    console.log(e.detail.value)
     var ids = e.detail.value;
     if(ids.length==0){
       this.setData({selectedAll:false,totalPrice:0});
     }else{
       var totalPrice = 0;
       for (var i = 0; i < this.data.goods.length; i++) {
         var good = this.data.goods[i];
         for (var j = 0; j < ids.length; j++) {
           if (good.goodsID == ids[j]) {
             totalPrice += parseFloat(good.goodsPrice);
           }
         }
       }
       if(this.data.goods.length == ids.length)
       {
          this.setData({ selectedAll: true, totalPrice: totalPrice });
       }
       else{
          this.setData({ selectedAll: false, totalPrice: totalPrice });
       }
       
     } 
  },
  checkAll:function(e){
     var selected = this.data.selected;
     var result = selected==true?false:true;
     this.setData({selected:result});
     if (result==false){
        
     }else{
       this.loadGoods();
     }
  },
  addGoods:function(e){
    var id = e.currentTarget.id;
    var goods = wx.getStorageSync("goods");
    var addGoods = new Array();
    for(var i=0;i<goods.length;i++){
      var good = goods[i];
      if(good.id == id){
        good.count = good.count + 1;
      }
      addGoods.push(good);
    }
    wx.setStorageSync("goods", addGoods);
    this.loadGoods();
  },
  minusGoods:function(e){
    var id = e.currentTarget.id;
    var goods = wx.getStorageSync("goods");
    var addGoods = new Array();
    for (var i = 0; i < goods.length; i++) {
      var good = goods[i];
      if (good.id == id) {
        var count = good.count;
        if(count >= 2){
          good.count = good.count - 1;
        }
      }
      addGoods.push(good);
    }
    wx.setStorageSync("goods", addGoods);
    this.loadGoods();
  }
})