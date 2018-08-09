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
    ,url: 'http://127.0.0.1:8888/listGood/'
    //,url: './json/content/good.js' //模拟接口
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 100, title: '商品ID', sort: true}
      ,{field: 'name', title: '商品名称', minWidth: 100}
      ,{field: 'price', title: '商品价格(元)', minWidth: 100}
      ,{field: 'type', title: '商品分类'}
      ,{field: 'uploadtime',width:170, title: '上货时间', sort: true}
      ,{field: 'status', title: '库存', templet: '#buttonTpl', minWidth: 80, align: 'center'}
      ,{title: '操作', minWidth: 150, align: 'center', fixed: 'right', toolbar: '#table-content-list'}
    ]]
    ,page: true
    ,limit: 10
    ,limits: [10, 15, 20, 25, 30]
    ,done:function(res){
      data_len = res.data.length;
      if(data_len == 0){
        var s = $('.layui-none').html('无商品数据')
      }
    }
    ,text: '对不起，加载出现异常！'
  });

 //监听搜索
    form.on('submit(LAY-app-contlist-search)', function(data){
      var field = data.field;

      //执行重载
      table.reload('LAY-app-content-list', {
        where: field
      });
    });

    var active = {
      batchdel: function(){
        var checkStatus = table.checkStatus('LAY-app-content-list')
        ,checkData = checkStatus.data; //得到选中的数据

        if(checkData.length === 0){
          return layer.msg('请选择数据');
        }

        layer.confirm('确定删除吗？', function(index) {

          //执行 Ajax 后重载
          /*
          admin.req({
            url: 'xxx'
            //,……
          });
          */
          table.reload('LAY-app-content-list');
          layer.msg('已删除');
        });
      }

      //添加
      ,add: function(othis){
        admin.popup({
          title: '添加商品'
          ,area: ['550px', '450px']
          ,id: 'LAY-popup-content-add'
          ,success: function(layero, index){
            view(this.id).render('app/content/listform').done(function(){
              form.render(null, 'layuiadmin-app-form-list');

              //监听提交
              form.on('submit(layuiadmin-app-form-submit)', function(data){
                var field = data.field; //获取提交的字段
                //layer.alert(JSON.stringify(field));
                //提交 Ajax 成功后，关闭当前弹层并重载表格
                $.ajax({
                  url: 'http://127.0.0.1:8888/addGood/',
                  type: 'POST',
                  data:field,
                  error:function(request){//请求失败之后的操作
                      layer.alert("添加失败",{icon: 2});
                  },
                  success:function(data){//请求成功之后的操作
                      if(data['code'] == 0){
                        layer.msg('添加成功', {icon: 1});
                        table.reload('LAY-user-manage'); //重载表格
                      }else if(data['code'] == 2){
                        layer.alert("手机号已存在,添加失败!",{icon: 2});
                      }else {
                        layer.alert("添加失败!",{icon: 2});
                      }
                  }

                });
                layui.table.reload('LAY-app-content-list'); //重载表格
                layer.close(index); //执行关闭
              });
            });
          }
        });
      }
    };

    $('.layui-btn.layuiadmin-btn-list').on('click', function(){
      var type = $(this).data('type');
      active[type] ? active[type].call(this) : '';
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