app.controller('demo_test1_ctrl',function($scope, $http){
    $scope.touch_file = function() {
        alert('开始创建文件');
        $http.get('/ansible_demo/touchFile/')
        .success(function(result){
            alert('创建文件成功');
            console.log(result)
        }).error(function(err){
            alert('创建文件失败');
            console.log(err)
        });
    };
});