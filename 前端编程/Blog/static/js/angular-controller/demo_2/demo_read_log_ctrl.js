app.controller('demo_read_log_ctrl',function($scope, $http){
    $scope.read_flag = false;
    $scope.execute_read = function() {
        $scope.ansible_log = '';
        $scope.read_flag = true;
        // console.log($scope.read_flag);
        $scope.state = 'PENDING';
        data = {'yml_file': $scope.yml_file};
        // console.log(data);
        // $http.post('/demo2_api/execute_long_ansible/', data)
        $http({
            // url: '/demo2_api/execute_long_ansible/',
            url: '/execute_long_ansible/',
            method: "POST",
            data: data,
            // data: $httpParamSerializer({
            //     yml_file: $scope.yml_file
            // }),
            contentType: 'application/json',
            dataType:'json'
        })
        .success(function(result){
            $scope.task_id = result['task_id'];
            read_log({'seek': 0 , 'task_id': result['task_id'], 'log_file': result['log_file']});
            // console.log(result['log_file']);
            $scope.ansible_log += '\nstart read\n';
        }).error(function(err){
            console.log(err)
        });
    };

    function read_log(data){
        // $http.post('/demo2_api/read_long_ansible/', data)
        $http.post('/read_long_ansible/', data)
        .success(function(result){
            // console.log(result);
            data = result;
            $scope.ansible_log += result['logs'];            // add logs to model(ansible_log)
            if($scope.state == 'REVOKED'){
                 $scope.ansible_log += '\nend read\n';
            	$scope.read_flag = false;
                 return;
            }
            $scope.state = data['state'];
            $scope.read_flag = data['read_flag']     
            if($scope.read_flag == false){
                alert('task ' + result['task_id'] + ' is over')
                document.getElementById("textscroll").scrollTop=document.getElementById("textscroll").scrollHeight;
                $scope.ansible_log += '\nend read\n';
            }else{
                if($scope.read_flag == false){
                    alert('task ' + result['task_id'] + ' is over')
                    document.getElementById("textscroll").scrollTop=document.getElementById("textscroll").scrollHeight;
                    $scope.ansible_log += '\nend read\n';
                }else{
                    setTimeout(function() { read_log(data)}, 5000);  // wait every 5 second to read log
                    if(document.getElementById("textscroll").scrollTop + 1000>=document.getElementById("textscroll").scrollHeight || document.getElementById("textscroll").scrollTop == 0){
                        setTimeout(function(){
                            document.getElementById("textscroll").scrollTop=document.getElementById("textscroll").scrollHeight;
                        },100);
                    }
                }
            }
        }).error(function(err){
            console.log('err')
        });
    }

    $scope.revoke_task = function(task_id){
        data = {'task_id': task_id}
        console.log('from revoke' + data)
        // $http.post('/demo2_api/long_ansible_revoke/', data)
        // $http.post('/long_ansible_revoke/', data)
        $http({
            url: '/long_ansible_revoke/',
            method: "POST",
            data: data,
            contentType: 'application/json',
            dataType:'json'
        })
        .success(function(result){
            alert('任务已经停止')
            $scope.task_id = '';
            $scope.state = 'REVOKED';
        }).error(function(err){
            console.log('err')
        });
    };

});
