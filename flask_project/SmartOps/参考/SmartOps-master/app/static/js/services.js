angular.module('inspinia').factory('AuthService',
    ['$q', '$timeout', 'jsonrpc', '$cookies',
        function ($q, $timeout, jsonrpc, $cookies) {

            // create user variable
            var user = null;

            var token = $cookies.get('token');
            var next = 'index.main';

            // return available functions for use in controllers
            return ({
                isLoggedIn: isLoggedIn,
                login: login,
                logout: logout,
                register: register,
                getUserStatus: getUserStatus
            });

            function isLoggedIn() {
                if (user) {
                    return true;
                } else {
                    return false;
                }
            }

            function login(email, password) {

                // create a new instance of deferred
                var deferred = $q.defer();

                // send a post request to the server

                jsonrpc.request('user.verify', {
                    username: email,
                    password: password
                })
                    .then(function (result) {
                        if (result.status == 0) {
                            var expireDate = new Date();
                            expireDate.setDate(expireDate.getDate() + 1);
                            token = result.token;
                            $cookies.put("token",token,{'expires': expireDate});
                            user = true;
                            deferred.resolve();
                        }
                        else {
                            user = false
                            deferred.reject();
                        }
                    })
                    .catch(function (error) {
                        user = false;
                        deferred.reject();
                    })

                // return promise object
                return deferred.promise;

            }

            function logout() {

                // create a new instance of deferred
                var deferred = $q.defer();

                $cookies.remove('token')
                // return promise object
                return deferred.promise;

            }

            function register(email, password) {
                return
                // create a new instance of deferred
                var deferred = $q.defer();

                // send a post request to the server
                $http.post('/api/register', {email: email, password: password})
                // handle success
                    .success(function (data, status) {
                        if (status === 200 && data.result) {
                            deferred.resolve();
                        } else {
                            deferred.reject();
                        }
                    })
                    // handle error
                    .error(function (data) {
                        deferred.reject();
                    });

                // return promise object
                return deferred.promise;

            }

            function getUserStatus() {

                return jsonrpc.request('user.status', {token: token}).then(function (result) {
                    if (result.status == 0) {
                        user = true
                    }
                    else {
                        user = false

                    }
                }).catch(function (reason) {
                    user = false
                })
            }
        }]);