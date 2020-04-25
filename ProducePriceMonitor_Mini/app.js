//app.js
App({
  onLaunch: function () {
    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
        if (res.code) {
          var sessionID = wx.getStorageSync('SessionID');//获取本地缓存中session
          var header = {
            'content-type': 'application/json',
            'cookie': "my_session_id=" + sessionID,
          };
          //发起网络请求
          wx.request({
            url: 'http://49.233.195.95:8000/login',
            method: 'GET',
            header: header,
            data: {
              code: res.code
            },
            success:function(res){
              console.log(res.data)
              wx.setStorageSync('SessionID', res.data.data.my_session_id)
            },
            fail:function(errMsg){
             
            }
          })
        }
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
    try{
      var val =  wx.getStorageSync('ordercart');
      if(val){
        this.globalData.ordercart = val;
      }
    }catch(e){

    }
    
  },
  GetRequestHeader:function(){
    var sessionID = wx.getStorageSync('SessionID');//获取本地缓存中session
    var header = {
        'content-type': 'application/json',
        'cookie': "my_session_id=" + sessionID,
    };
    return header;
  },
  SaveOrderCartToStorage:function(){
    wx.setStorageSync('ordercart', this.globalData.ordercart)
  },
  globalData: {
    userInfo: null,
    ordercart: [],
  },
  
})