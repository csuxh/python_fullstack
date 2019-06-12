app.controller('demo_test2_ctrl',function($scope, $http){
    $scope.touch_file = function(filename) {
        $scope.ansible_log = '';
        if(_.isEmpty(filename)){
            alert('输入不能为空')
            return;
        }
        $scope.main_msg = '开始创建文件,请耐心等待';
        data = {'filename': filename}
        // $scope.main_msg = data;
        $http.post('/ansible_demo/touchFile3/', data)
        .success(function(result){
            alert(result['msg']);
            console.log(result)
            $scope.ansible_log = result['output'];
            $scope.main_msg = '';
        }).error(function(err){
            console.log(err)
        });
    };
});