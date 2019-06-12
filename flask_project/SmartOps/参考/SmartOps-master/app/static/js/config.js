/**
 * INSPINIA - Responsive Admin Theme
 *
 * Inspinia theme use AngularUI Router to manage routing and views
 * Each view are defined as state.
 * Initial there are written state for all view in theme.
 *
 */
function config($stateProvider, $urlRouterProvider, $ocLazyLoadProvider) {
    $urlRouterProvider.otherwise("/index/404");

    $ocLazyLoadProvider.config({
        // Set to true if you want to see what and when is dynamically loaded
        debug: false
    });


    $stateProvider

        .state('index', {
            abstract: true,
            url: "/index",
            templateUrl: "static/views/common/content.html",

        })
        .state('index.main', {
            url: "/main",
            templateUrl: "static/views/main.html",
            data: {pageTitle: 'Example view'},
            access: {restricted: true}
        })
        .state('index.minor', {
            url: "/minor",
            templateUrl: "static/views/minor.html",
            data: {pageTitle: 'Example view'},
            access: {restricted: true}
        })
        .state('login', {
                url: '/login',
                access: {restricted: false},
                templateUrl: "static/views/login.html",
                controller: 'LoginCtrl',
            }
        )
        .state('index.error404', {
            url: '/404',
            access: {restricted: false},
            templateUrl: "static/views/errorOne.html"
        })
        .state('host', {
            abstract: true,
            url: "/host",
            templateUrl: "static/views/common/content.html",

        })
        .state('host.add', {
            url: '/add',
            access: {restricted: false},
            templateUrl: "static/views/host/create.html"
        })
        .state('host.list', {
            url: '/list',
            access: {restricted: true},
            templateUrl: "static/views/host/list.html",
            data: {pageTitle: '主机列表'},
            resolve: {
                loadPlugin: function ($ocLazyLoad) {
                    return $ocLazyLoad.load([
                        {
                            serie: true,
                            files: ['/static/js/plugins/dataTables/datatables.min.js', '/static/css/plugins/dataTables/datatables.min.css']
                        },
                        {
                            serie: true,
                            name: 'datatables',
                            files: ['/static/js/plugins/dataTables/angular-datatables.min.js']
                        },
                        {
                            serie: true,
                            name: 'datatables.buttons',
                            files: ['/static/js/plugins/dataTables/angular-datatables.buttons.min.js']
                        }
                    ]);
                }
            }
        })
        .state('knowledge', {
            abstract: true,
            url: "/knowledge",
            templateUrl: "static/views/common/content.html",
        })
        .state('knowledge.list', {
            url: "/list",
            data: {pageTitle: '知识库列表'},
            access: {restricted: true},
            templateUrl: "static/views/knowledge/list.html",
        })
        .state('knowledge.add', {
            url: "/add",
            data: {pageTitle: '添加知识库'},
            access: {restricted: true},
            templateUrl: "static/views/knowledge/add.html",
            resolve: {
                loadPlugin: function ($ocLazyLoad) {
                    return $ocLazyLoad.load([
                        {
                            serie: true,
                            files: ['/static/em/css/editormd.css', '/static/em/js/zepto.min.js', "/static/em/js/editormd.js"]
                        }
                    ]);
                }
            }
        })
        .state('project', {
            abstract: true,
            url: "/project",
            templateUrl: "static/views/common/content.html"
        })
        .state('project.list', {
            url: "/list",
            data: {pageTitle: '项目列表'},
            access: {restricted: true},
            templateUrl: "static/views/project/list.html",
        })
        .state('project.add', {
            url: "/add",
            data: {pageTitle: '添加项目'},
            access: {restricted: true},
            templateUrl: "static/views/project/add.html",
        })
        .state('project.config', {
            url: "/config",
            data: {pageTitle: '项目配置'},
            access: {restricted: true},
            templateUrl: "static/views/project/config.html",
            resolve: {
                loadPlugin: function ($ocLazyLoad) {
                    return $ocLazyLoad.load([
                        {
                            serie: true,
                            files: ['/static/em/css/editormd.css', '/static/em/js/zepto.min.js', "/static/em/js/editormd.js"]
                        },
                        {
                            name: 'ui.select',
                            files: ['/static/css/plugins/ui-select/select.min.css', '/static/js/plugins/ui-select/select.min.js']

                        }
                    ]);
                }
            }
        })
        .state('project.deploy', {
            url: "/deploy",
            data: {pageTitle: '项目部署'},
            access: {restricted: true},
            templateUrl: "static/views/project/deploy.html",
            resolve: {
                loadPlugin: function ($ocLazyLoad) {
                    return $ocLazyLoad.load([
                        {
                            serie: true,
                            files: ['/static/em/css/editormd.css', '/static/em/js/zepto.min.js', "/static/em/js/editormd.js"]
                        },
                        {
                            name: 'ui.select',
                            files: ['/static/css/plugins/ui-select/select.min.css', '/static/js/plugins/ui-select/select.min.js']

                        }
                    ]);
                }
            }


        })
        .state('project.run', {
            url: "/run",
            data: {pageTitle: ''},
            access: {restricted: true},
            templateUrl: "static/views/project/run.html",

        })
        .state('blog', {
            abstract: true,
            url: "/blog",
            templateUrl: "static/views/blog/content_top_navigation.html",
        })
        .state('blog.index', {
            url: "/index",
            templateUrl: "static/views/blog/index.html",
            access: {restricted: true},
        })
}

angular
    .module('inspinia')
    .config(config)
    .run(function ($rootScope, $state, AuthService) {
        $rootScope.$state = $state
        $rootScope.$on('$stateChangeStart',
            function (event, toState, toParams, fromState, fromParams) {
                AuthService.getUserStatus().then(function () {
                    if (toState.access.restricted && !AuthService.isLoggedIn()) {
                        AuthService.next = toState.name
                        $state.go('login')
                    }
                })
            })
    })
