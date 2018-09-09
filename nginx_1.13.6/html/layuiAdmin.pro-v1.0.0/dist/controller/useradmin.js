/** layuiAdmin.pro-v1.0.0 LPPL License By http://www.layui.com/admin/ */
 ;layui.define(["table","form"],function(e){function a(e){var a=n(".layui-laypage-curr em:eq(1)").text(),t=n(".layui-table tbody tr").length;console.log(t);var i=n(e.tr[0]).attr("data-index");return 0==i&&3==t&&(a=1==a?a:a-1),a}function t(e){var a=n(".layui-laypage-curr em:eq(1)").text();return e.isAll&&(a=1==a?a:a-1),a}var n=layui.$,i=layui.admin,r=layui.setter,l=layui.view,o=layui.table,c=layui.form,d=layui.laytpl;o.render({elem:"#LAY-user-manage",url:r.http+"listVipPerson/",where:{access_token:layui.data("layuiAdmin").access_token},cols:[[{type:"checkbox",fixed:"left"},{field:"id",width:"8%",title:"会员ID",sort:!0,align:"center"},{field:"vip_name",width:"10%",title:"用户名",align:"center"},{field:"vip_sex",width:"8%",title:"性别",sort:!0,align:"center"},{field:"vip_phone",width:"12%",title:"手机",align:"center"},{field:"vip_person_point",width:"10%",title:"积分",sort:!0,align:"center"},{field:"vip_notes",width:"20%",title:"备注",align:"center"},{title:"操作",width:"28%",minWidth:250,align:"center",fixed:"right",toolbar:"#table-useradmin-webuser"}]],page:!0,done:function(e){if("1001"==e.code&&i.exit(),data_len=e.data.length,0==data_len){n(".layui-none").html("无会员数据")}},text:"对不起，加载出现异常！"}),c.render(null,"layadmin-userfront-formlist"),c.on("submit(LAY-user-front-search)",function(e){var a=e.field;console.log(a),o.reload("LAY-user-manage",{where:a,page:1,done:function(e,a,t){if(data_len=e.data.length,0==data_len){n(".layui-none").html("未查询到会员数据")}}})}),o.on("tool(LAY-user-manage)",function(e){var t=e.data;if("del"===e.event){var s={};s.checkData=t.id,s.access_token=layui.data("layuiAdmin").access_token,layer.prompt({formType:1,title:"敏感操作，请验证口令"},function(t,l){"111111"==t?(layer.close(l),layer.confirm("确定删除吗？",function(t){n.ajax({url:r.http+"delVipPerson/",type:"POST",data:s,error:function(e){layer.alert("删除失败",{icon:2})},success:function(t){0==t.code?(layer.msg("删除成功",{icon:1}),o.reload("LAY-user-manage",{page:{curr:a(e)}})):2==t.code?layer.alert("会员存在未结算订单，无法删除!",{icon:2}):"1001"==t.code?i.exit():layer.alert("删除失败!",{icon:2})}})})):(layer.close(l),layer.alert("密码错误",{icon:2}))})}else"edit"===e.event?i.popup({title:"编辑用户",area:["500px","450px"],id:"LAY-popup-user-edit",success:function(e,a){l(this.id).render("user/user/userform",t).done(function(){c.render(null,"layuiadmin-form-useradmin"),n("#id").val(t.id),n("#desc").val(t.vip_notes),c.on("submit(LAY-user-front-submit)",function(e){var t=e.field;t.access_token=layui.data("layuiAdmin").access_token,n.ajax({url:r.http+"editVipPerson/",type:"POST",data:t,error:function(e){layer.alert("更新失败",{icon:2})},success:function(e){0==e.code?(layer.msg("更新成功",{icon:1}),o.reload("LAY-user-manage")):2==e.code?layer.alert("手机号已存在,更新失败!",{icon:2}):"1001"==e.code?(layer.close(a),i.exit()):layer.alert("更新失败!",{icon:2})}}),layer.close(a)})})}}):"add"===e.event&&i.popup({title:"生成订单",area:["800px","550px"],id:"LAY-popup-user-add",success:function(e,a){l(this.id).render("app/workorder/dd",t).done(function(){console.log(t),c.render(null,"layuiadmin-form-dd"),n("#vip_id").val(t.id),n("#vip_name").val(t.vip_name),n("#vip_phone").val(t.vip_phone),n.ajax({url:r.http+"listServer/",type:"GET",data:{access_token:layui.data("layuiAdmin").access_token},error:function(e){layer.msg("获取服务列表失败")},success:function(e){if(0==e.code){var t=demo.innerHTML,n=document.getElementById("server");d(t).render(e,function(e){n.innerHTML=e}),c.render("checkbox")}else"1001"==e.code&&(layer.close(a),i.exit())}}),n.ajax({url:r.http+"listGood/",type:"GET",data:{title:"",label:"1",access_token:layui.data("layuiAdmin").access_token},error:function(e){layer.msg("获取饮料列表失败")},success:function(e){if(0==e.code){var t=demo2.innerHTML,n=document.getElementById("drink");d(t).render(e,function(e){n.innerHTML=e})}else"1001"==e.code&&(layer.close(a),i.exit())}}),n.ajax({url:r.http+"listGood/",type:"GET",data:{title:"",label:"2",access_token:layui.data("layuiAdmin").access_token},error:function(e){layer.msg("获取酒水列表失败")},success:function(e){if(0==e.code){var t=demo2.innerHTML,n=document.getElementById("wine");d(t).render(e,function(e){n.innerHTML=e})}else"1001"==e.code&&(layer.close(a),i.exit())}}),n.ajax({url:r.http+"listGood/",type:"GET",data:{title:"",label:"3",access_token:layui.data("layuiAdmin").access_token},error:function(e){layer.msg("获取简餐列表失败")},success:function(e){if(0==e.code){var t=demo2.innerHTML,n=document.getElementById("snack");d(t).render(e,function(e){n.innerHTML=e})}else"1001"==e.code&&(layer.close(a),i.exit())}}),n.ajax({url:r.http+"listGood/",type:"GET",data:{title:"",label:"4",access_token:layui.data("layuiAdmin").access_token},error:function(e){layer.msg("获取火锅列表失败")},success:function(e){if(0==e.code){var t=demo2.innerHTML,n=document.getElementById("hot_pot");d(t).render(e,function(e){n.innerHTML=e})}else"1001"==e.code&&(layer.close(a),i.exit())}})})}})});var s={batchdel:function(){var e=o.checkStatus("LAY-user-manage"),a=e.data;if(0===a.length)return layer.msg("请选择数据",{icon:5});for(var l=[],c=0;c<a.length;c++)l.push(a[c].id);var d=(a[0].id,{});d.checkData=l.toString(),d.access_token=layui.data("layuiAdmin").access_token,layer.prompt({formType:1,title:"敏感操作，请验证口令"},function(a,l){"111111"==a?(layer.close(l),layer.confirm("确定删除吗？",function(a){n.ajax({url:r.http+"delVipPerson/",type:"POST",data:d,error:function(e){layer.alert("删除失败",{icon:2})},success:function(a){0==a.code?(layer.msg("删除成功",{icon:1}),o.reload("LAY-user-manage",{page:{curr:t(e)}})):2==a.code?layer.alert("会员存在未结算订单，无法删除!",{icon:2}):"1001"==a.code?i.exit():layer.alert("删除失败!",{icon:2})}})})):(layer.close(l),layer.alert("密码错误",{icon:2}))})},add:function(){i.popup({title:"添加用户",area:["500px","450px"],id:"LAY-popup-user-add",success:function(e,a){l(this.id).render("user/user/userform").done(function(){c.render(null,"layuiadmin-form-useradmin"),c.on("submit(LAY-user-front-submit)",function(e){var t=e.field;t.access_token=layui.data("layuiAdmin").access_token,n.ajax({url:r.http+"addVipPerson/",type:"POST",data:t,error:function(e){layer.alert("添加失败",{icon:2})},success:function(e){0==e.code?(layer.msg("添加成功",{icon:1}),o.reload("LAY-user-manage")):2==e.code?layer.alert("手机号已存在,添加失败!",{icon:2}):"1001"==e.code?i.exit():layer.alert("添加失败!",{icon:2})}}),layer.close(a)})})}})}};n(".layui-btn.layuiadmin-btn-useradmin").on("click",function(){var e=n(this).data("type");s[e]?s[e].call(this):""}),e("useradmin",{})});