/**

 @Name：layuiAdmin 营销
 @Site：http://www.layui.com/admin/
 @License：LPPL

 */


layui.define(['table', 'form','laydate'], function(exports){
  var $ = layui.$
  ,admin = layui.admin
  ,setter = layui.setter
  ,view = layui.view
  ,table = layui.table
  ,laydate = layui.laydate
  ,layer = layui.layer
  ,form = layui.form;





  //商品管理
  table.render({
    elem: '#LAY-app-content-list'
    ,url: setter.http+'listGood/'
    //,url: './json/content/good.js' //模拟接口
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 100, title: '商品ID', sort: true, align: 'center'}
      ,{field: 'name', title: '商品名称', minWidth: 100, align: 'center'}
      ,{field: 'price', title: '商品价格(元)', minWidth: 100, align: 'center'}
      ,{field: 'type', title: '商品分类', align: 'center'}
      ,{field: 'uploadtime',width:170, title: '最近一次上货时间', sort: true, align: 'center'}
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
          return layer.msg('请选择数据',{icon:5});
        }
        var l= []
        for (var i =0;i<checkData.length; i++) {
            l.push(checkData[i]['id'])
        };
        var mycars=checkData[0]['id']

        var dic ={};
     //    for (var i=0;i<checkData.length;i++)
        // {
        //  mycars.push(checkData[i]['id'])
        // }
        dic['checkData'] = l.toString()


        layer.confirm('确定删除吗？', function(index) {
          $.ajax({
             url: setter.http+'delGood/',
             type: 'POST',
             data: dic ,
             error:function(request){
                layer.alert("商品删除失败",{icon: 2});
             },
             success:function(data){
                if(data['code'] == 0){
                  layer.msg('商品删除成功', {icon: 1});
                  table.reload('LAY-app-content-list', {
                                page: {
                                    curr: deleteDulJumpPage(checkStatus)
                                }
                  });

                }else {
                  layer.alert("商品删除失败!",{icon: 2});
                }
              }
            });

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
                  url: setter.http+'addGood/',
                  type: 'POST',
                  data:field,
                  error:function(request){//请求失败之后的操作
                      layer.alert("添加失败",{icon: 2});
                  },
                  success:function(data){//请求成功之后的操作
                      if(data['code'] == 0){
                        layer.msg('添加成功', {icon: 1});
                        table.reload('LAY-app-content-list'); //重载表格
                      }else if(data['code'] == 2){
                        layer.alert("商品已存在,添加失败!",{icon: 2});
                      }else {
                        layer.alert("添加失败!",{icon: 2});
                      }
                  }

                });

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



  //监听工具条 --删除和编辑
  table.on('tool(LAY-app-content-list)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      var dic ={};
      dic['checkData'] =data['id']
      layer.confirm('确定删除此商品？', function(index){
            $.ajax({
             url: setter.http+'delGood/',
             type: 'POST',
             data: dic ,
             error:function(request){
                layer.alert("商品删除失败",{icon: 2});
             },
             success:function(data){
                if(data['code'] == 0){

                  layer.msg('商品删除成功', {icon: 1});
                  table.reload('LAY-app-content-list', {
                                page: {
                                    curr: deleteJumpPage(obj)
                                }
                             });
                }else {
                  layer.alert("商品删除失败!",{icon: 2});
                }
              }
          });
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

            //监听提交
            form.on('submit(layuiadmin-app-form-submit)', function(data){
              var field = data.field; //获取提交的字段a
              //layer.alert(JSON.stringify(field));
              //提交 Ajax 成功后，关闭当前弹层并重载表格
              if(parseInt(field['add_count'])<0){
                layer.msg("失败！上货数量不能为负数",{icon: 2});
              }else{
                $.ajax({
                url: setter.http+'editGood/',
                type: 'POST',
                data:field,
                error:function(request){//请求失败之后的操作
                    layer.alert("更新失败",{icon: 2});
                },
                success:function(data){//请求成功之后的操作
                    if(data['code'] == 0){
                      table.reload('LAY-app-content-list'); //重载表格
                      layer.msg('更新成功', {icon: 1});
                    }else if(data['code'] == 2){
                      layer.alert("商品已存在,更新失败!",{icon: 2});
                    }else {
                      layer.alert("更新失败!",{icon: 2});
                    }
                }
              });

              }

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
    ,url: setter.http+'listServer/'
    //,url: './json/content/server.js' //模拟接口
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
    ,done:function(res){
      data_len = res.data.length;
      if(data_len == 0){
        var s = $('.layui-none').html('无服务数据')
      }
    }
    ,text: '对不起，加载出现异常！'
  });

  //监听工具条
  table.on('tool(LAY-app-content-comm)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      var dic ={};
      dic['checkData'] =data['id']
      layer.confirm('确定删除此服务？', function(index){
        $.ajax({
             url: setter.http+'delServer/',
             type: 'POST',
             data: dic ,
             error:function(request){
                layer.alert("商品删除失败",{icon: 2});
             },
             success:function(data){
                if(data['code'] == 0){

                  layer.msg('商品删除成功', {icon: 1});
                  table.reload('LAY-app-content-comm', {
                                page: {
                                    curr: deleteJumpPage(obj)
                                }
                             });
                }else {
                  layer.alert("商品删除失败!",{icon: 2});
                }
              }
          });
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
//监听搜索
  form.on('submit(LAY-app-contcomm-search)', function(data){
    var field = data.field;

    //执行重载
    table.reload('LAY-app-content-comm', {
      where: field
    });
  });

  //点击事件
  var active2 = {
    batchdel2: function(){
      var checkStatus = table.checkStatus('LAY-app-content-comm')
      ,checkData = checkStatus.data; //得到选中的数据

      if(checkData.length === 0){
        return layer.msg('请选择数据');
      }
        var l= []
        for (var i =0;i<checkData.length; i++) {
            l.push(checkData[i]['id'])
        };
        var mycars=checkData[0]['id']

        var dic ={};

        dic['checkData'] = l.toString()

      layer.confirm('确定删除吗？', function(index) {

         $.ajax({
             url: setter.http+'delServer/',
             type: 'POST',
             data: dic ,
             error:function(request){
                layer.alert("服务删除失败",{icon: 2});
             },
             success:function(data){
                if(data['code'] == 0){
                  layer.msg('服务删除成功', {icon: 1});
                  table.reload('LAY-app-content-comm', {
                                page: {
                                    curr: deleteDulJumpPage(checkStatus)
                                }
                  });

                }else {
                  layer.alert("服务删除失败!",{icon: 2});
                }
              }
            });
      });
    },add2: function(othis){
        admin.popup({
          title: '添加服务'
          ,area: ['550px', '430px']
          ,id: 'LAY-popup-content-add'
          ,success: function(layero, index){
            view(this.id).render('app/content/serverform').done(function(){
              form.render(null, 'layuiadmin-form-comment');

              //监听提交
              form.on('submit(layuiadmin-app-com-submit)', function(data){
                var field = data.field; //获取提交的字段
                //layer.alert(JSON.stringify(field));
                $.ajax({
                  url: setter.http+'addServer/',
                  type: 'POST',
                  data:field,
                  error:function(request){//请求失败之后的操作
                      layer.alert("添加失败",{icon: 2});
                  },
                  success:function(data){//请求成功之后的操作
                      if(data['code'] == 0){
                        layer.msg('添加成功', {icon: 1});
                        table.reload('LAY-app-content-comm'); //重载表格
                      }else if(data['code'] == 2){
                        layer.alert("服务已存在,添加失败!",{icon: 2});
                      }else {
                        layer.alert("添加失败!",{icon: 2});
                      }
                  }

                });
                layer.close(index); //执行关闭
              });
            });
          }
        });
      }

  };

  $('.layui-btn.layuiadmin-btn-comm').on('click', function(){
    var type = $(this).data('type');
    active2[type] ? active2[type].call(this) : '';
  });

 function deleteJumpPage(obj){
        // 获取当前页码   console.log(obj.tr[0]);// 获取行数据内容
        var curr = $('.layui-laypage-curr em:eq(1)').text();
        //console.log(curr);
        // 获取tr的data-index属性的值验证是否是当前页的第一条
        var s = $('.layui-table tbody tr').length;
        console.log(s);
        var dataIndex = $(obj.tr[0]).attr("data-index");
        // 如是当前页的第一条数据,curr-1
        if (dataIndex == 0 && s == 3 ) {
            curr = curr == 1 ? curr : curr - 1
        }
        //console.log(curr);
        return curr;
  }
   // 批量删除返回跳转
    function deleteDulJumpPage(checkStatus) {
    var curr = $('.layui-laypage-curr em:eq(1)').text(); // 获取当前页码
    //console.log(curr);// 获取行数据内容
    //console.log(checkStatus);
    //console.log(checkStatus.isAll)
    if (checkStatus.isAll) {
        curr = curr == 1 ? curr : curr - 1
    }
    return curr; // 返回curr
}

  exports('contlist', {})
});