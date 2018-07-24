/**

 @Name：layuiAdmin 订单系统
 @Author：star1029
 @Site：http://www.layui.com/admin/
 @License：GPL-2

 */


layui.define(['table', 'form', 'element'], function(exports){
  var $ = layui.$
  ,admin = layui.admin
  ,view = layui.view
  ,table = layui.table
  ,form = layui.form
  ,element = layui.element;

  table.render({
     elem: '#LAY-app-workorder'
    ,url: './json/workorder/demo.js' //模拟接口
    ,cols: [[
      {type: 'numbers', fixed: 'left'}
      ,{field: 'orderid', width: 150, title: '订单号', sort: true,align: 'center'}
      ,{field: 'attr', width: 100, title: '订单人',align: 'center'}
      ,{field: 'type', width: 100, title: '订单类型',align: 'center'}
      ,{field: 'progress', title: '进度', width: 200, align: 'center', templet: '#progressTpl'}
      ,{field: 'state', title: '订单状态', templet: '#buttonTpl', minWidth: 80, align: 'center'}
      ,{title: '操作', align: 'center', fixed: 'right', toolbar: '#table-system-order'}
    ]]
    ,page: true
    ,limit: 10
    ,limits: [10, 15, 20, 25, 30]
    ,text: '对不起，加载出现异常！'
    ,done: function(){
      element.render('progress');
    }
  });

  //监听工具条
  table.on('tool(LAY-app-workorder)', function(obj){
    var data = obj.data;
    if(obj.event === 'view'){
      admin.popup({
        title: '订单信息'
        ,id: 'LAY-popup-workorder-add'
        ,area: ['800px', '600px']
        ,success: function(layero, index){
          // console.log(data);
          view(this.id).render('app/workorder/listform').done(function(){
            form.render(null, 'layuiadmin-form-workorder');
            $("#orderid").val(data['orderid']);
            $("#attr").val(data['attr']);
            $("#type").val(data['type']);
            $("#status").val(data['state']);
            $("#time").val('2018-07-25 01:01:11');
            $("#money").val('100');
            $("#jf").val('10');
            form.on('submit(LAY-app-workorder-submit)', function(data){
              layer.close(index)
            });
          });
        }
      });
    }else if(obj.event === 'complete'){
      admin.req({
      url: './json/workorder/ddje.js'
      ,type: 'get'
      ,data: {}
      ,done: function(res){
        layer.open( {
        title: '订单结算完成',
        content: res['name']+"订单共消费"+res['money']+",共积分"+res['integration']+"分",
        btn: ['确定'],
        yes: function(index, layero){
            layui.table.reload('LAY-app-workorder'); //重载表格
            layer.close(index);
          }
        });
      }
    });



    }
  });

  exports('workorder', {})
});