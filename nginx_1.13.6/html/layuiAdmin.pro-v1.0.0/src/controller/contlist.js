/**

 @Name：layuiAdmin 营销
 @Site：http://www.layui.com/admin/
 @License：LPPL

 */


layui.define(['table', 'form','laydate'], function(exports){
  var $ = layui.$
  ,admin = layui.admin
  ,view = layui.view
  ,table = layui.table
  ,laydate = layui.laydate
  ,layer = layui.layer
  ,form = layui.form;





  //商品管理
  table.render({
    elem: '#LAY-app-content-list'
    ,url: './json/content/good.js' //模拟接口
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 100, title: '商品ID', sort: true}
      ,{field: 'name', title: '商品名称', minWidth: 100}
      ,{field: 'price', title: '商品价格(元)', minWidth: 100}
      ,{field: 'type', title: '商品分类'}
      ,{field: 'uploadtime', title: '上货时间', sort: true}
      ,{field: 'status', title: '库存', templet: '#buttonTpl', minWidth: 80, align: 'center'}
      ,{title: '操作', minWidth: 150, align: 'center', fixed: 'right', toolbar: '#table-content-list'}
    ]]
    ,page: true
    ,limit: 10
    ,limits: [10, 15, 20, 25, 30]
    ,text: '对不起，加载出现异常！'
  });

  //监听工具条
  table.on('tool(LAY-app-content-list)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      layer.confirm('确定删除此商品？', function(index){
        obj.del();
        layer.close(index);
      });
    } else if(obj.event === 'edit'){
      admin.popup({
        title: '编辑商品'
        ,area: ['550px', '550px']
        ,id: 'LAY-popup-content-edit'
        ,success: function(layero, index){
          view(this.id).render('app/content/listform', data).done(function(){
            //console.log(data);
            form.render(null, 'layuiadmin-app-form-list');

              //上货日期
              laydate.render({
                elem: '#date'
                ,type: 'datetime'
                ,value: new Date()

              });
            //监听提交
            form.on('submit(layuiadmin-app-form-submit)', function(data){
              var field = data.field; //获取提交的字段
             layer.alert(JSON.stringify(field));
              //提交 Ajax 成功后，关闭当前弹层并重载表格
              //$.ajax({});
              layui.table.reload('LAY-app-content-list'); //重载表格
              layer.close(index); //执行关闭
            });
          });
        }
      });
    }
  });

  //服务列表
  table.render({
    elem: '#LAY-app-content-comm'
    ,url: './json/content/server.js' //模拟接口
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 100, title: '服务ID', sort: true}
      ,{field: 'name', title: '服务名称', minWidth: 100}
      ,{field: 'price',title: '服务价格(元)'}
      ,{field: 'type', title: '服务分类'}
      ,{title: '操作', minWidth: 150, align: 'center', fixed: 'right', toolbar: '#table-content-com'}
    ]]
    ,page: true
    ,limit: 10
    ,limits: [10, 15, 20, 25, 30]
    ,text: '对不起，加载出现异常！'
  });

  //监听工具条
  table.on('tool(LAY-app-content-comm)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      layer.confirm('确定删除此服务？', function(index){
        obj.del();
        layer.close(index);
      });
    } else if(obj.event === 'edit'){
      admin.popup({
        title: '编辑服务'
        ,area: ['550px', '550px']
        ,id: 'LAY-popup-content-edit'
        ,success: function(layero, index){
          view(this.id).render('app/content/serverform', data).done(function(){
            console.log(data);
            form.render(null, 'layuiadmin-form-comment');


            //监听提交
            form.on('submit(layuiadmin-app-com-submit)', function(data){
              var field = data.field; //获取提交的字段
             layer.alert(JSON.stringify(field));
              //提交 Ajax 成功后，关闭当前弹层并重载表格
              //$.ajax({});
              layui.table.reload('LAY-app-content-comm'); //重载表格
              layer.close(index); //执行关闭
            });
          });
        }
      });
    }
  });

  exports('contlist', {})
});