/**

 @Name：layuiAdmin 用户管理 管理员管理 角色管理
 @Site：http://www.layui.com/admin/
 @License：LPPL

 */


layui.define(['table', 'form'], function(exports){
  var $ = layui.$
  ,admin = layui.admin
  ,view = layui.view
  ,table = layui.table
  ,form = layui.form
  ,laytpl = layui.laytpl;

  //用户管理
  table.render({
    elem: '#LAY-user-manage'
   ,url: 'http://127.0.0.1:8888/listVipPerson/'
   //,url: './json/useradmin/webuser.js' //模拟接口
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: '8%', title: 'ID', sort: true, align:'center'}
      ,{field: 'vip_name',width:'10%', title: '用户名', align:'center'}
      ,{field: 'vip_sex', width: '8%', title: '性别' ,sort: true, align:'center'}
      ,{field: 'vip_phone', width: '12%',title: '手机', align:'center'}
       ,{field: 'vip_person_point',width: '10%', title: '积分', sort: true, align:'center'}
      ,{field: 'vip_notes', width: '20%', title: '备注', align:'center'}
      ,{title: '操作', width: '28%', align:'center', fixed: 'right', toolbar: '#table-useradmin-webuser'}
    ]]
    ,page: true
    ,done:function (res) {
        if(res.data.length == 0){
          layer.confirm('暂无会员信息')
        }

    }
    //,height: 'full-320'
    ,text: '对不起，加载出现异常！'
  });

  //监听工具条
  table.on('tool(LAY-user-manage)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      var dic ={};
      dic['checkData'] =data['id']
      layer.prompt({
        formType: 1
        ,title: '敏感操作，请验证口令'
      }, function(value, index){
        if(value =='693582'){
          layer.close(index);
          layer.confirm('确定删除吗？', function(index) {

          //执行 Ajax 后重载
          $.ajax({
             url: 'http://127.0.0.1:8888/delVipPerson/',
             type: 'POST',
             data: dic ,
             error:function(request){
                layer.alert("会员删除失败",{icon: 2});
             },
             success:function(data){
                if(data['code'] == 0){

                  layer.msg('会员删除成功', {icon: 1});
                  table.reload('LAY-user-manage', {
                                page: {
                                    curr: deleteJumpPage(obj)
                                }
                                ,where: {
                                    id:data.id
                                }
                             });
                }else {
                  layer.alert("删除失败!",{icon: 2});
                }
              }
          });



          });
        }else{
          layer.close(index);
          layer.alert('密码错误',{icon:2})
        }

      });
    } else if(obj.event === 'edit'){
      admin.popup({
        title: '编辑用户'
        ,area: ['500px', '450px']
        ,id: 'LAY-popup-user-edit'
        ,success: function(layero, index){
          view(this.id).render('user/user/userform', data).done(function(){
            form.render(null, 'layuiadmin-form-useradmin');

            $('#id').val(data.id);
            $('#desc').val(data.vip_notes);
            //console.log(data);
            //监听提交
            form.on('submit(LAY-user-front-submit)', function(data){
              var field = data.field; //获取提交的字段

              //提交 Ajax 成功后，关闭当前弹层并重载表格
              $.ajax({
                url: 'http://127.0.0.1:8888/editVipPerson/',
                type: 'POST',
                data:field,
                error:function(request){//请求失败之后的操作
                    layer.alert("更新失败",{icon: 2});
                },
                success:function(data){//请求成功之后的操作
                    if(data['code'] == 0){
                      layer.msg('更新成功', {icon: 1});
                      table.reload('LAY-user-manage'); //重载表格
                    }else if(data['code'] == 2){
                      layer.alert("手机号已存在,更新失败!",{icon: 2});
                    }else {
                      layer.alert("更新失败!",{icon: 2});
                    }
                }
              });
              layer.close(index); //执行关闭
            });
          });
        }
      });

    }else if(obj.event === 'add'){
      admin.popup({
        title:  '生成订单'
        ,area: ['800px', '600px']
        ,id: 'LAY-popup-user-add'
        ,success: function(layero, index){

          view(this.id).render('template/dd', data).done(function(){
            //console.log(data);
            form.render(null,'layuiadmin-form-dd');
             $('#vip_name').val(data.vip_name);
             $('#vip_phone').val(data.vip_phone);
             //获取服务接口
             admin.req({
             url: './json/content/server.js'
             ,type: 'get'
             ,data: {}
             ,done: function(res){ //这里要说明一下：done 是只有 response 的 code 正常才会执行。而 succese 则是只要 http 为 200 就会执行
              //console.log(res);
              var getTpl = demo.innerHTML
              ,view = document.getElementById('server');
              laytpl(getTpl).render(res, function(html){
                view.innerHTML = html;
              });
              form.render('checkbox');
              }
            });
             //获取商品接口
             admin.req({
             url: './json/content/good.js'
             ,type: 'get'
             ,data: {}
             ,done: function(res){
              //console.log(res);
               var getTpl = demo2.innerHTML
              ,view = document.getElementById('good');
              laytpl(getTpl).render(res, function(html){
                view.innerHTML = html;
              });

              }
            });

          });
        }
      });
    }
  });

 function deleteJumpPage(obj){
        // 获取当前页码   console.log(obj.tr[0]);// 获取行数据内容
        var curr = $('.layui-laypage-curr em:eq(1)').text();
        // console.log(curr);
        // 获取tr的data-index属性的值验证是否是当前页的第一条
        var s = $('.layui-table table tr');
        console.log(s);
        var dataIndex = $(obj.tr[0]).attr("data-index");
        // 如是当前页的第一条数据,curr-1
        if (dataIndex == 0) {
            curr = curr == 1 ? curr : curr - 1
        }
        //console.log(curr);
        return curr;
  }

  exports('useradmin', {})
});

