{
  "code": 0
  ,"msg": ""
  ,"data": [{
    "title": "控制台"
    ,"icon": "layui-icon-home"
      ,"jump": "/"

  }, {
    "name": "user"
    ,"title": "会员"
    ,"icon": "layui-icon-user"
    ,"list": [{
      "name": "user"
      ,"title": "会员用户"
      ,"jump": "user/user/list"
    }]
  },{
    "name": "template"
    ,"title": "独立页面"
    ,"icon": "layui-icon-template"
    ,"list": [{
      "name": "addresslist"
      ,"title": "通讯录"
      ,"jump": "template/addresslist"
    },{
      "name": "reg"
      ,"title": "注册"
      ,"jump": "user/reg"
    },{
      "name": "login"
      ,"title": "登入"
      ,"jump": "user/login"
    }]
  }, {
    "name": "app"
    ,"title": "营销"
    ,"icon": "layui-icon-app"
    ,"list": [{
      "name": "workorder"
      ,"title": "订单系统"
      ,"jump": "app/workorder/list"
    },{
      "name": "content"
      ,"title": "商城管理"
      ,"spread": true
      ,"list": [{
        "name": "list"
        ,"title": "商品列表"
      },{
        "name": "comment"
        ,"title": "服务列表"
      }]

    }]
  }, {
    "name": "senior"
    ,"title": "高级"
    ,"icon": "layui-icon-senior"
    ,"list": [{
      "name": "echarts"
      ,"title": "Echarts集成"
      ,"list": [{
        "name": "line"
        ,"title": "折线图"
      },{
        "name": "bar"
        ,"title": "柱状图"
      },{
        "name": "map"
        ,"title": "地图"
      }]
    }]
  }, {
    "name": "set"
    ,"title": "设置"
    ,"icon": "layui-icon-set"
    ,"list": [{
      "name": "system"
      ,"title": "系统设置"
      ,"spread": true
      ,"list": [{
        "name": "email"
        ,"title": "邮件服务"
      }]
    },{
      "name": "user"
      ,"title": "我的设置"
      ,"spread": true
      ,"list": [{
        "name": "info"
        ,"title": "基本资料"
      },{
        "name": "password"
        ,"title": "修改密码"
      }]
    }]
  }]
}