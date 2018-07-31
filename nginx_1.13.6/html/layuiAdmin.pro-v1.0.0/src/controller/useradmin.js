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
    ,limit: 10
    ,height: 'full-320'
    ,text: '对不起，加载出现异常！'
  });

  //监听工具条
  table.on('tool(LAY-user-manage)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      layer.prompt({
        formType: 1
        ,title: '敏感操作，请验证口令'
      }, function(value, index){
        if(value ==='111') {
          layer.close(index);
          layer.confirm('真的删除行么', function(index){
          obj.del();
          table.reload('LAY-user-manage');
          layer.close(index);
        });
        }
        else{

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
            $('#desc').val(data.vip_notes);
            console.log(data);
            //监听提交
            form.on('submit(LAY-user-front-submit)', function(data){
              var field = data.field; //获取提交的字段

              //提交 Ajax 成功后，关闭当前弹层并重载表格
              //$.ajax({});
              layui.table.reload('LAY-user-manage'); //重载表格
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

  //管理员管理
  table.render({
    elem: '#LAY-user-back-manage'
    ,url: './json/useradmin/mangadmin.js' //模拟接口
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 80, title: 'ID', sort: true}
      ,{field: 'loginname', title: '登录名'}
      ,{field: 'telphone', title: '手机'}
      ,{field: 'email', title: '邮箱'}
      ,{field: 'role', title: '角色'}
      ,{field: 'jointime', title: '加入时间', sort: true}
      ,{field: 'check', title:'审核状态', templet: '#buttonTpl', minWidth: 80, align: 'center'}
      ,{title: '操作', width: 150, align: 'center', fixed: 'right', toolbar: '#table-useradmin-admin'}
    ]]
    ,text: '对不起，加载出现异常！'
  });

  //监听工具条
  table.on('tool(LAY-user-back-manage)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      layer.prompt({
        formType: 1
        ,title: '敏感操作，请验证口令'
      }, function(value, index){
        layer.close(index);
        layer.confirm('确定删除此管理员？', function(index){
          console.log(obj)
          obj.del();
          layer.close(index);
        });
      });
    }else if(obj.event === 'edit'){
      admin.popup({
        title: '编辑管理员'
        ,area: ['420px', '450px']
        ,id: 'LAY-popup-user-add'
        ,success: function(layero, index){
          view(this.id).render('user/administrators/adminform', data).done(function(){
            form.render(null, 'layuiadmin-form-admin');

            //监听提交
            form.on('submit(LAY-user-back-submit)', function(data){
              var field = data.field; //获取提交的字段

              //提交 Ajax 成功后，关闭当前弹层并重载表格
              //$.ajax({});
              layui.table.reload('LAY-user-back-manage'); //重载表格
              layer.close(index); //执行关闭
            });
          });
        }
      });
    }
  });

  //角色管理
  table.render({
    elem: '#LAY-user-back-role'
    ,url: './json/useradmin/role.js' //模拟接口
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 80, title: 'ID', sort: true}
      ,{field: 'rolename', title: '角色名'}
      ,{field: 'limits', title: '拥有权限'}
      ,{field: 'descr', title: '具体描述'}
      ,{title: '操作', width: 150, align: 'center', fixed: 'right', toolbar: '#table-useradmin-admin'}
    ]]
    ,text: '对不起，加载出现异常！'
  });

  //监听工具条
  table.on('tool(LAY-user-back-role)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      layer.confirm('确定删除此角色？', function(index){
        obj.del();
        layer.close(index);
      });
    }else if(obj.event === 'edit'){
      admin.popup({
        title: '添加新角色'
        ,area: ['500px', '480px']
        ,id: 'LAY-popup-user-add'
        ,success: function(layero, index){
          view(this.id).render('user/administrators/roleform', data).done(function(){
            form.render(null, 'layuiadmin-form-role');

            //监听提交
            form.on('submit(LAY-user-role-submit)', function(data){
              var field = data.field; //获取提交的字段

              //提交 Ajax 成功后，关闭当前弹层并重载表格
              //$.ajax({});
              layui.table.reload('LAY-user-back-role'); //重载表格
              layer.close(index); //执行关闭
            });
          });
        }
      });
    }
  });

  exports('useradmin', {})
});

