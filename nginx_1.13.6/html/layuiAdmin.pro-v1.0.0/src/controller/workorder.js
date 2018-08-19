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
      ,{field: 'all_value', width: 100, title: '总费用',align: 'center'}
      ,{field: 'lay_value', width: 100, title: '延时费用',align: 'center'}
      ,{field: 'free_value', width: 100, title: '优惠费用',align: 'center'}
      ,{field: 'progress', title: '进度', width: 200, align: 'center', templet: '#progressTpl'}
      ,{field: 'notes', width: 160, title: '备注',align: 'center'}
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
        ,area: ['750px', '660px']
        ,success: function(layero, index){
          //console.log(data);
          view(this.id).render('app/workorder/listform').done(function(){

            $.ajax({
              //url: './json/workorder/dddetail.js'
              url: setter.http+'orderDetail/'
              ,type: 'get'
              ,data: {'order_serial_number':data['order_serial_number']}
              ,error:function(data){
                  layer.msg("获取订单详情失败",{icon:2});
              }
              ,success: function(res){
                //console.log(res);
                 form.render(null, 'layuiadmin-form-workorder');
                  $("#orderid").val(res['order_serial_number']);
                  $("#attr").val(res['name']);
                  $("#type").val(res['type']);
                  if(res['state']==0){
                     $("#status").val('待结账');
                  }else if(res['state']==1){
                     $("#status").val('已结账');
                  }else{
                     $("#status").val('故障');
                  }
                  $("#time").val(res['start_time']);
                  $("#end_time").val(res['end_time']);

                  $("#money").val(res['money']);
                  $("#jf").val(res['integration']);
                  var server = res.server
                  var good = res.good
                  //console.log(result);
                  var my_str='<table  class="layui-table" lay-size="sm"><th>服务名</th><th>单价</th><th>数量';
                  var my_str2 ='<table  class="layui-table" lay-size="sm"><th>商品名</th><th>单价</th><th>数量';

                  for (var i=0;i<server.length;i++){
                    my_str += '<tr><td>'+server[i].name+'</td><td>'+server[i].price+'</td><td>'+server[i].server_count+'</td></tr>'
                  }
                  my_str += '</table>'
                   for (var i=0;i<good.length;i++){
                      my_str2 += '<tr><td>'+good[i].name+'</td><td>'+good[i].price+'</td><td>'+good[i].good_count+'</td></tr>'
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

      layer.prompt({
          formType: 1
          ,title: '敏感操作，请验证口令'
          }, function(value, index){
            if(value =='111111'){
          layer.close(index);
          layer.confirm('确定结账吗？', function(index) {

           $.ajax({
              //url: './json/workorder/ddje.js'
              url: setter.http+'endOrder/'
              ,type: 'get'
              ,data: {'order_serial_number':data['order_serial_number']}
              ,error:function(data){
                  layer.msg("订单结算失败",{icon:2});
              }
              ,success: function(res){
                   layer.close(index);

              }
          });


          });
        }else{
          layer.close(index);
          layer.alert('密码错误',{icon:2})
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
            form.render(null,'layuiadmin-form-new-dd');
             $('#vip_id').val(data.person_id);
             $('#vip_name').val(data.name);
             $('#vip_phone').val (data.phone);
            //获取服务列表接口
             $.ajax({
               url: setter.http+'listServer/',
               type: 'GET',
               error:function(data){
                  layer.msg("获取服务列表失败");
               },
               success:function(data){
                  //console.log(data);
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

        }
      });

    }
  });

  exports('workorder', {})
});