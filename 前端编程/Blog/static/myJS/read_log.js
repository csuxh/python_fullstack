$("#refresh_host").on("click", function () {
            $.ajax({
                    url:"/demo2/ansible_host_api/",
                    type:"GET",
                    data:JSON.stringify({}),
                    contentType: 'application/json', //默认: "application/x-www-form-urlencoded"
                    dataType:'json',
                    success:function(ret){
                        var ss = '';
                        for(var i=0; i < ret.length; i +=1){
                            // console.log(ret[i]);
                            ss += '<tr><th>' + ret[i].name + '</th>' +
                                '<th>' + ret[i].group + '</th>' +
                                '<th>' + ret[i].ssh_host + '</th>' +
                                '<th>' + ret[i].ssh_user + '</th>' +
                                '<th>' + ret[i].ssh_port + '</th>' +
                                '<th>' + ret[i].server_type + '</th>' +
                                '<th class="col-md-3 text-muted"><button class="btn btn-primary btn-offset" data-toggle="modal" data-target="#servers_operate" ng-click="create_tag("modify", ret[i]);">修改和查看</button><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><button class="btn btn-primary btn-offset"  data-toggle="modal" data-target="#servers_operate" ng-click="create_tag("remove", ret[i])">删除</button></th>;' +
                                '</tr>'
                        }
                        // console.log(ss)
                        $('#host_info').html(ss);
                    }
                }
            )
        })