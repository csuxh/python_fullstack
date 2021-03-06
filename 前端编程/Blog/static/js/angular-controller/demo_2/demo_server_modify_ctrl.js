app.controller('demo_server_modify_ctrl',function($scope, $http){
    get_all_data = function() {
        $http.get('/AnsibleHostApi/')
        .success(function (res) {
            $scope.servers_list_all = res;
            console.log(res)
        })
    }

    get_all_data()

    $scope.generate_new_ansible_host_func = function() {
        $http.get('/demo2/create_ansible_hosts/')
            .success(function (res) {
               if(res['flag'] == true) {
                    alert('生成hosts成功')
               }else{
                   alert('生成hosts失败')
               }
            }).error(function (res) {
            alert('生成hosts失败')
        })
    }

    $scope.create_tag = function(tag, ins){
        $scope.operate_type = tag;
        if(tag == 'remove'|| tag == 'modify'){
            $scope.id = ins.id;
            $scope.group = ins.group,
            $scope.name = ins.name,
            $scope.ssh_host = ins.ssh_host,
            $scope.ssh_user = ins.ssh_user,
            $scope.ssh_port = ins.ssh_user,
            $scope.server_type = ins.server_type,
            $scope.comment = ins.comment
            console.log("from create_tag" + ins)
        }
    }

    $scope.generate_ansible_host_func = function() {
        $scope.save_wait = true;
        if($scope.operate_type == 'create') {
            data = {'group': $scope.group,
                'name': $scope.name,
                'ssh_host': $scope.ssh_host,
                'ssh_user': $scope.ssh_user,
                'ssh_port': $scope.ssh_port,
                'server_type': $scope.server_type,
                'comment': $scope.comment
            }
            $http.post('/demo2/create_ansible_hosts_add/', data)
                .success(function (res) {
                    if (res['flag'] == true) {
                        alert('生成hosts成功')
                        get_all_data()
                    } else {
                        alert('生成hosts失败')
                    }
                    $scope.save_wait = '';
                }).error(function (res) {
                alert('生成hosts失败')
                $scope.save_wait = '';
            })
        }
        if($scope.operate_type == 'remove') {
            data = {'remove_id': $scope.id};
            $http.post('/demo2/create_ansible_hosts_delete/', data)
                .success(function (res) {
                    if (res['flag'] == true) {
                        alert('生成hosts成功')
                        get_all_data()
                    } else {
                        alert('生成hosts失败')
                    }
                    $scope.save_wait = '';
                }).error(function (res) {
                alert('生成hosts失败')
                $scope.save_wait = '';
            })
        }
        if($scope.operate_type == 'modify') {
            data = {'id': $scope.id,
                'group': $scope.group,
                'name': $scope.name,
                'ssh_host': $scope.ssh_host,
                'ssh_user': $scope.ssh_user,
                'ssh_port': $scope.ssh_port,
                'server_type': $scope.server_type,
                'comment': $scope.comment
            }
            $http.post('/demo2/create_ansible_hosts_modify/', data)
                .success(function (res) {
                    console.log(res)
                    if (res['flag'] == true) {
                        alert('生成hosts成功')
                        get_all_data()
                    } else {
                        alert('生成hosts失败')
                    }
                    $scope.save_wait = '';
                }).error(function (res) {
                alert('生成hosts失败')
                $scope.save_wait = '';
            })
        }
    }

});