app.controller('demo_server_add_ctrl',function($scope, $http){
    get_all_data = function() {
        $http.get('/demo2/ansible_host_api/')
        .success(function(response, status, headers, config){
            $scope.servers_list_all = '111'+ response;
            console.log('111'+ response)
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

    $scope.create_tag = function(tag){
        $scope.operate_type = tag;
    }

    $scope.generate_ansible_host_func = function() {
        $scope.save_wait = true;
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
                if(res['flag'] == true) {
                    alert('生成hosts成功')
                    get_all_data()
                }else{
                    alert('生成hosts失败')
                }
                $scope.save_wait = '';
            }).error(function (res) {
            alert('生成hosts失败')
            $scope.save_wait = '';
        })
    }

});