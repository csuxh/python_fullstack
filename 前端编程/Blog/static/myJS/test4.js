var app = angular.module('app', ['angularFileUpload']);
app.controller('uploadController',['$scope', 'FileUploader', function($scope, FileUploader) {
    $scope.uploadStatus = $scope.uploadStatus1 = false; //定义两个上传后返回的状态，成功获失败
    var uploader = $scope.uploader = new FileUploader({
        url: 'upload.php',
        queueLimit: 1,     //文件个数
        removeAfterUpload: true   //上传后删除文件
    });
    var uploader1 = $scope.uploader1 = new FileUploader({
        url: 'upload.php',
        queueLimit: 1,
        removeAfterUpload: true
    });
    $scope.clearItems = function(){    //重新选择文件时，清空队列，达到覆盖文件的效果
        uploader.clearQueue();
    }
    $scope.clearItems1 = function(){
        uploader1.clearQueue();
    }
    uploader.onAfterAddingFile = function(fileItem) {
        $scope.fileItem = fileItem._file;    //添加文件之后，把文件信息赋给scope
    };
    uploader1.onAfterAddingFile = function(fileItem) {
        $scope.fileItem1 = fileItem._file;    //添加文件之后，把文件信息赋给scope
        //能够在这里判断添加的文件名后缀和文件大小是否满足需求。
    };
    uploader.onSuccessItem = function(fileItem, response, status, headers) {
        $scope.uploadStatus = true;   //上传成功则把状态改为true
    };
    uploader1.onSuccessItem = function(fileItem,response, status, headers){
        $scope.uploadStatus1 = true;
    }
    $scope.UploadFile = function(){
        uploader.uploadAll();
        uploader1.uploadAll();
        if(status){
            if(status1){
                alert('上传成功！');
            }else{
                alert('证书成功！私钥失败！');
            }
       }else{
            if(status1){
               alert('私钥成功！证书失败！');
            }else{
               alert('上传失败！');
            }
       }
    }
}])