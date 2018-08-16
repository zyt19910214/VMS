/**

 @Name：layuiAdmin 订单系统
 @Site：http://www.layui.com/admin/
 @License：GPL-2

 */


layui.define(['table', 'form', 'element'], function(exports){
  var $ = layui.$
  ,admin = layui.admin
  ,setter = layui.setter
  ,laytpl = layui.laytpl
  ,setter = layui.setter
  ,view = layui.view
  ,table = layui.table
  ,form = layui.form
  ,element = layui.element;

  table.render({
     elem: '#LAY-app-workorder'
     ,url: setter.http+'listOrder/'
    //,url: './json/workorder/demo.js' //模拟接口
    ,cols: [[
      {type: 'numbers', fixed: 'left'}
      ,{field: 'order_serial_number', width: 150, title: '订单号', sort: true,align: 'center'}
      ,{field: 'name', width: 100, title: '订单人',align: 'center'}
      ,{field: 'phone', width: 150, title: '手机号',align: 'center'}
      ,{field: 'type', width: 100, title: '订单类型',align: 'center'}
      ,{field: 'free_value', width: 100, title: '优惠费用',align: 'center'}
      ,{field: 'lay_value', width: 100, title: '延时费用',align: 'center'}
      ,{field: 'progress', title: '进度', width: 200, align: 'center', templet: '#progressTpl'}
      ,{field: 'notes', width: 200, title: '备注',align: 'center'}
      ,{field: 'state', width: 120,title: '订单状态', templet: '#buttonTpl', align: 'center'}
      ,{title: '操作', align: 'center', minWidth:250,fixed: 'right', toolbar: '#table-system-order'}
    ]]
    ,page: true
    ,limit: 10
    ,limits: [10, 15, 20, 25, 30]
    ,text: '对不起，加载出现异常！'
    ,done: function(res){
      element.render('progress');
      data_len = res.data.length;
      if(data_len == 0){
        var s = $('.layui-none').html('无订单数据')
      }
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

            admin.req({
              url: './json/workorder/dddetail.js'
              ,type: 'get'
              ,data: {}
              ,done: function(res){
                console.log(res);
                 form.render(null, 'layuiadmin-form-workorder');
                  $("#orderid").val(data['orderid']);
                  $("#attr").val(data['attr']);
                  $("#type").val(data['type']);
                  $("#status").val(data['state']);
                  if(res['end_time']){
                    $("#time").val(res['end_time']);
                  }else{
                     $("#time").val(res['start_time']);
                  }
                  $("#money").val(res['money']);
                  $("#jf").val(res['integration']);
                  var server = res.server
                  var good = res.good
                  //console.log(result);
                  var my_str='';
                  var my_str2 ='';
                  for (var i=0;i<server.length;i++){
                      my_str += server[i].name+' x '+server[i].count+'</br>'
                  }
                   for (var i=0;i<good.length;i++){
                      my_str2 += good[i].name+' x '+good[i].count+'</br>'
                  }
                  $("#serverlist").html(my_str)
                  $("#goodlist").html(my_str2)

              }
            });
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



    }else if(obj.event == 'new_add'){
         admin.popup({
        title:  '已有未结算订单时新增订单'
        ,area: ['800px', '600px']
        ,id: 'LAY-popup-user-add'
        ,success: function(layero, index){

          view(this.id).render('template/new_dd', data).done(function(){
            //console.log(data);
            form.render(null,'layuiadmin-form-new_dd');
             $('#vip_name').val(data.vip_name);
             $('#vip_phone').val(data.vip_phone);

            //获取服务列表接口
             $.ajax({
               url: setter.http+'listServer/',
               type: 'GET',
               error:function(data){
                  layer.msg("获取服务列表失败");
               },
               success:function(data){
                  console.log(data);
                  var getTpl = demo.innerHTML
                  ,view = document.getElementById('server');
                  laytpl(getTpl).render(data, function(html){
                    view.innerHTML = html;
                  });
                  form.render('checkbox');
                }
            });

            //获取饮料列表接口
            $.ajax({
              url: setter.http+'listGood/',
              type: 'GET',
              data:{"title":"","label":"1"}
              ,error:function(data){
                layer.msg("获取饮料列表失败");
              },
              success:function(data){
                //console.log(data);
                var getTpl = demo2.innerHTML
                ,view = document.getElementById('drink');
                laytpl(getTpl).render(data, function(html){
                  view.innerHTML = html;
                });
              }
            });

            //获取酒水列表接口
            $.ajax({
              url: setter.http+'listGood/',
              type: 'GET',
              data:{"title":"","label":"2"}
              ,error:function(data){
                layer.msg("获取酒水列表失败");
              },
              success:function(data){
                //console.log(data);
                var getTpl = demo2.innerHTML
                ,view = document.getElementById('wine');
                laytpl(getTpl).render(data, function(html){
                  view.innerHTML = html;
                });
              }
            });

            //获取简餐列表接口
            $.ajax({
              url: setter.http+'listGood/',
              type: 'GET',
              data:{"title":"","label":"3"}
              ,error:function(data){
                layer.msg("获取简餐列表失败");
              },
              success:function(data){
                //console.log(data);
                var getTpl = demo2.innerHTML
                ,view = document.getElementById('snack');
                laytpl(getTpl).render(data, function(html){
                  view.innerHTML = html;
                });
              }
            });

            //获取火锅列表接口
            $.ajax({
              url: setter.http+'listGood/',
              type: 'GET',
              data:{"title":"","label":"4"}
              ,error:function(data){
                layer.msg("获取火锅列表失败");
              },
              success:function(data){
                //console.log(data);
                var getTpl = demo2.innerHTML
                ,view = document.getElementById('hot_pot');
                laytpl(getTpl).render(data, function(html){
                  view.innerHTML = html;
                });
              }
            });




          });
          //监听提交
  form.on('submit(LAY_new_dd_submit)', function(data){
    //layer.alert(JSON.stringify(data.field), { title: '最终的提交信息' })
    var field = data.field; //获取提交的字段
    console.log(field);
    //提交 Ajax 成功后，关闭当前弹层并重载表格
    $.ajax({
      url: setter.http+'addOrder/',
      type: 'POST',
      data:field,
      error:function(request){//请求失败之后的操作
          layer.alert("订单生成失败",{icon: 2});
      },
      success:function(data){//请求成功之后的操作
          if(data['code'] == 0){
            layer.open( {
            title: '订单生成',
            content: '订单生成成功',
            btn: ['确定'],
            yes: function(index, layero){
              layer.close(index);
            }
            });
              //window.location.href='#/app/workorder/list';
            return false;
          }else if(data['code'] == 2){
            layer.alert("该用户存在未结算订单,生成失败!",{icon: 2});
          }else {
            layer.alert("订单生成失败!",{icon: 2});
          }

      }

     });
 });

        }
      });

    }
  });

  exports('workorder', {})
});