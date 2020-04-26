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
    totalPrice:0.0,
    monitorPrice:1.0
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
      for (var i = 0; i < this.data.goods.length; i++) {
        this.data.goods[i].isSelect = false;
        this.setData({selectedAll:false,totalPrice:0,goods:this.data.goods});  
      }
     }else{
       var totalPrice = 0;
       for (var i = 0; i < this.data.goods.length; i++) {
         var good = this.data.goods[i];
         this.data.goods[i].isSelect = false
         for (var j = 0; j < ids.length; j++) {
           if (good.goodsID == ids[j]) {
             totalPrice += parseFloat(good.goodsPrice);
             this.data.goods[i].isSelect = true
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
     var selected = this.data.selectedAll;
     console.log(selected)
     var result = selected==true?false:true;
     for (var i = 0; i < this.data.goods.length; i++) {
      this.data.goods[i].isSelect = result;
     }
     this.setData({selected:result,selectedAll:result,goods: this.data.goods});
     if (result==false){
        
     }else{
       this.loadGoods();
     }
  },
  deleteGoods:function(e){
    console.log("delete")
    for(var i = this.data.goods.length-1; i >= 0;i--)
    {
      if(this.data.goods[i].isSelect == true)
      {
        this.data.goods.splice(i,1)
        this.data.totalPrice = 0.0
        this.data.monitorPrice = 0.0
      }
      app.globalData.ordercart = this.data.goods
      app.SaveOrderCartToStorage()
    }
    this.setData({goods:this.data.goods,totalPrice:this.data.totalPrice,monitorPrice:this.data.monitorPrice})
  }
})