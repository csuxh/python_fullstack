'use strict';


angular
    .module('app', ['angularFileUpload'])
    .controller('AppController', ['$scope','$http','FileUploader', function($scope,$http,FileUploader) {
        var uploader = $scope.uploader = new FileUploader({
            url: './upload/'
        });

        // FILTERS

        uploader.filters.push({
            name: 'customFilter',
            fn: function(item /*{File|FileLikeObject}*/, options) {
                return this.queue.length < 10;
            }
        });

        // CALLBACKS
        $scope.filename = '';

        uploader.onWhenAddingFileFailed = function(item /*{File|FileLikeObject}*/, filter, options) {
            // console.info('onWhenAddingFileFailed', item, filter, options);
        };
        uploader.onAfterAddingFile = function(fileItem) {

            // console.info('onAfterAddingFile', fileItem);
        };
        uploader.onAfterAddingAll = function(addedFileItems) {
            // console.info('onAfterAddingAll', addedFileItems);
        };
        uploader.onBeforeUploadItem = function(item) {
            // console.info('onBeforeUploadItem', item);
        };
        uploader.onProgressItem = function(fileItem, progress) {
            // console.info('onProgressItem', fileItem, progress);
        };
        uploader.onProgressAll = function(progress) {
            // console.info('onProgressAll', progress);
        };
        uploader.onSuccessItem = function(fileItem, response, status, headers) {
            // console.info('onSuccessItem', fileItem, response, status, headers);
            if($scope.filename==''){$scope.filename = fileItem._file.name;}
            else{$scope.filename += ',' + fileItem._file.name};
        };
        uploader.onErrorItem = function(fileItem, response, status, headers) {
            // console.info('onErrorItem', fileItem, response, status, headers);
        };
        uploader.onCancelItem = function(fileItem, response, status, headers) {
            // console.info('onCancelItem', fileItem, response, status, headers);
        };
        uploader.onCompleteItem = function(fileItem, response, status, headers) {
            // console.info('onCompleteItem', fileItem, response, status, headers);
        };
        uploader.onCompleteAll = function() {
            // console.info('onCompleteAll');
            // $scope.filename = fileItem._file.name;
        };
        console.log("from uploader");
        console.info('uploader', uploader);


        $scope.delever_file = function()
        {
            $http({
                // url: '/demo2_api/execute_long_ansible/',
                url: '/deploy_files/',
                method: "POST",
                data: {'name':$scope.filename},
                contentType: 'application/json',
                dataType: 'json'
            })
                .success(function (result) {
                    console.log("after sucessed")
                    console.log(uploader)
                    console.log("sucessed")
                })
                .error(function (err) {
                console.log(err)
            });
        };
    }]);
