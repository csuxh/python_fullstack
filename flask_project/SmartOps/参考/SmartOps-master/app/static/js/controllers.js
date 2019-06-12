/**
 * INSPINIA - Responsive Admin Theme
 *
 */

/**
 * MainCtrl - controller
 */
function MainCtrl() {

    this.userName = '';
    this.helloText = '';
    this.descriptionText = '';

};

function HostListCtrl($scope, DTOptionsBuilder, jsonrpc, $cookies) {

    $scope.dtOptions = DTOptionsBuilder.newOptions()
        .withDOM('<"html5buttons"B>lTfgitp')
        .withButtons([
            {extend: 'copy'},
            {extend: 'csv'},
            {extend: 'excel', title: 'ExampleFile'},
            {extend: 'pdf', title: 'ExampleFile'},

            {
                extend: 'print',
                customize: function (win) {
                    $(win.document.body).addClass('white-bg');
                    $(win.document.body).css('font-size', '10px');

                    $(win.document.body).find('table')
                        .addClass('compact')
                        .css('font-size', 'inherit');
                }
            }
        ]);
    jsonrpc.request('asset.get', {'token': $cookies.get('token')}).then(function (data) {
        $scope.hosts = data['data']
    }).catch(function (reason) {
        console.log(reason)
    })
}

function LoginCtrl($scope, $state, AuthService) {
    $scope.login = function () {
        AuthService.login($scope.loginForm.email,
            $scope.loginForm.password
        ).then(function () {
                if (AuthService.next == undefined) {
                    AuthService.next = 'index.main'
                }
                $state.go(AuthService.next)
            }
        ).catch(function (reason) {
            $scope.errorMessage = reason;
        })
    }
}

function HostAddCtrl($scope, jsonrpc, $cookies) {
    $scope.ip2 = '192.168.1.121'
    $scope.username = 'shuaibo'
    $scope.password = '123456'
    $scope.port = '22'
    $scope.get = function () {
        jsonrpc.request('ansible.run', {
            hosts: [{
                "hostname": $scope.ip2,
                "username": $scope.username,
                "ip": $scope.ip2,
                "port": $scope.port,
                "password": $scope.password
            }],
            tasks: [{"action": {"module": "setup", "args": ""}, "name": "asset_info"}],
            token: $cookies.get('token')
        })
            .then(function (result) {
                t = result['ok'][$scope.ip2]['asset_info']['ansible_facts']
                $scope.vendor = t['ansible_system_vendor']
                $scope.model = t['ansible_system']
                $scope.cpu_model = t['ansible_processor'][2]
                $scope.cpu_count = t['ansible_processor_count']
                $scope.cpu_cores = t['ansible_processor_cores']
                $scope.memory = t['ansible_memtotal_mb']
                $scope.platform = t['ansible_os_family']
                $scope.os = t['ansible_distribution']
                $scope.os_version = t['ansible_distribution_version']
                $scope.os_arch = t['ansible_machine']
                $scope.hostname_raw = t['ansible_hostname']
                // console.log(assetinfo)

            }).catch(function (reason) {
        })

    }
    $scope.add = function () {
        jsonrpc.request('asset.add', {
            token: $cookies.get('token'),
            assetinfo: [{
                hostname_raw: $scope.hostname_raw,
                ip: $scope.ip2,
                hostname: $scope.hostname,
                port: $scope.port,
                vendor: $scope.vendor,
                model: $scope.model,
                sn: $scope.sn,
                cpu_model: $scope.cpu_model,
                cpu_count: $scope.cpu_count,
                cpu_cores: $scope.cpu_cores,
                memory: $scope.memory,
                platform: $scope.platform,
                os: $scope.os,
                os_version: $scope.os_version,
                os_arch: $scope.os_arch
            }]
        }).then(function () {

        }).catch(function (reason) {
        })
    }
}

function KnowledgeAddCtrl($scope, $stateParams, jsonrpc, $cookies) {
    var testEditor;
    var jQuery = Zepto;
    $scope.option = {
        width: "80%",
        autoHeight: true,
        path: '/static/lib/',
        markdown: "# 新文档",
        codeFold: true,
        //syncScrolling : false,
        saveHTMLToTextarea: true,    // 保存 HTML 到 Textarea
        searchReplace: true,
        //watch : false,                // 关闭实时预览
        htmlDecode: "style,script,iframe|on*",            // 开启 HTML 标签解析，为了安全性，默认不开启
        //toolbar  : false,             //关闭工具栏
        //previewCodeHighlight : false, // 关闭预览 HTML 的代码块高亮，默认开启
        emoji: false,
        taskList: true,
        tocm: true,         // Using [TOCM]
        tocTitle: "目录",
        tex: true,                   // 开启科学公式TeX语言支持，默认关闭
        flowChart: true,             // 开启流程图支持，默认关闭
        sequenceDiagram: false,       // 开启时序/序列图支持，默认关闭,
        //dialogLockScreen : false,   // 设置弹出层对话框不锁屏，全局通用，默认为true
        //dialogShowMask : false,     // 设置弹出层对话框显示透明遮罩层，全局通用，默认为true
        //dialogDraggable : false,    // 设置弹出层对话框不可拖动，全局通用，默认为true
        //dialogMaskOpacity : 0.4,    // 设置透明遮罩层的透明度，全局通用，默认值为0.1
        //dialogMaskBgColor : "#000", // 设置透明遮罩层的背景颜色，全局通用，默认为#fff
        imageUpload: true,
        imageFormats: ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
        imageUploadURL: "/blog/upload",
        onload: function () {
            this.fullscreen();

            var keyMap = {
                "Ctrl-S": function (cm) {
                    p = window.location.pathname.split('/')
                    if (p.length != 3) {

                        data = {}
                        data.name = p[p.length - 1]
                        data.content = testEditor.getMarkdown()
                        $.post('/blog/put', data, function (data) {
                            if (data != 0) {
                                testEditor.blogsaveDialog();
                            }

                        })

                    }
                    else {
                        testEditor.blogsaveDialog();
                    }
                }
            }
            this.addKeyMap(keyMap)

        },
    }
    KEditor = editormd("knowledge-editormd", $scope.option);
    $scope.putKnowledge = function () {
        jsonrpc.request('knowledge.put', {
            token: $cookies.get('token'),
            knowledges: {
                'title': $scope.Ktitle,
                'tag': $scope.Ktag,
                'description': $scope.Kdescription,
                'content': KEditor.getMarkdown()
            }
        })
    }
}

function KnowlegeGetCtrl($scope, jsonrpc, $cookies) {
    jsonrpc.request('knowledge.get', {token: $cookies.get('token'), type: 'all'}).then(function (data) {
        $scope.knowledges = data['data']
    })
}

function ProjectListCtrl($scope, jsonrpc, $cookies) {
    jsonrpc.request('project.get', {token: $cookies.get('token')}).then(function (data) {
        $scope.projects = data['data']
    }).catch(function (error) {
        console.log(error)
    })

}

function ProjectDeployCtrl($scope, jsonrpc, $cookies) {

    jsonrpc.request('project.get', {token: $cookies.get('token')}).then(function (data) {
        $scope.projects = data['data']
    }).catch(function (error) {
        console.log(error)
    });
    jsonrpc.request('project.deploy.list', {token: $cookies.get('token'), projectid: 1}).then(function (data) {
        $scope.deploys = data['data']
    }).catch(function (error) {
        console.log(error)
    })
    $scope.option = {
        width: "80%",
        autoHeight: true,
        path: '/static/lib/',
        codeFold: true,
        toolbar: true,
        //syncScrolling : false,
        saveHTMLToTextarea: true,    // 保存 HTML 到 Textarea
        searchReplace: true,
        watch: false,
        htmlDecode: "style,script,iframe|on*",
        toolbarIcons: function () {
            return ["undo", "redo", "|", "template", "run", "save"]
        },
        toolbarIconTexts: {
            template: "模板",
            run: "运行",
            save: "保存"

        },
        toolbarHandlers: {
            template: function (cm, icon, cursor, selection) {
                cm.replaceSelection("---\n" +
                    "- hosts: webservers\n" +
                    "  vars:\n" +
                    "    http_port: 80\n" +
                    "    max_clients: 200\n" +
                    "  remote_user: root\n" +
                    "  tasks:\n" +
                    "  - name: ensure apache is at the latest version\n" +
                    "    yum: pkg=httpd state=latest\n" +
                    "  - name: write the apache config file\n" +
                    "    template: src=/srv/httpd.j2 dest=/etc/httpd.conf\n" +
                    "    notify:\n" +
                    "    - restart apache\n" +
                    "  - name: ensure apache is running\n" +
                    "    service: name=httpd state=started\n" +
                    "  handlers:\n" +
                    "    - name: restart apache\n" +
                    "      service: name=httpd state=restarted");
            },
            save: function () {

            },
            run: function () {

            }
        },
        onload: function () {
            this.fullscreen();
            this.setToolbarAutoFixed(true);

        },

    }
    KEditor = editormd("PEdit", $scope.option);
    $scope.getDeploy=function (id) {
        jsonrpc.request('project.deploy.get',{token:$cookies.get('token'),id:id}).then(function (data) {
            KEditor.setMarkdown(data['data'])
        }).catch(function (error) {
            console.log(error)
        })
    }

}

function ProjectRunCtrl($scope, jsonrpc, $cookies) {
    jsonrpc.request('project.get', {token: $cookies.get('token')}).then(function (data) {
        $scope.projects = data['data']
    }).catch(function (error) {
        console.log(error)
    })


}

function ProjectConfigCtrl($scope, jsonrpc, $cookies) {
    jsonrpc.request('project.get', {token: $cookies.get('token')}).then(function (data) {
        $scope.projects = data['data']
    }).catch(function (error) {
        console.log(error)
    })
    $scope.option = {
        width: "80%",
        autoHeight: true,
        path: '/static/lib/',
        codeFold: true,
        toolbar: true,
        //syncScrolling : false,
        saveHTMLToTextarea: true,    // 保存 HTML 到 Textarea
        searchReplace: true,
        watch: false,
        htmlDecode: "style,script,iframe|on*",
        toolbarIcons: function () {
            return ["undo", "redo", "|", "template"]
        },
        toolbarIconTexts: {
            template: "模板",
            run: "运行"

        },
        toolbarHandlers: {
            template: function (cm, icon, cursor, selection) {
                cm.replaceSelection("---\n" +
                    "- hosts: webservers\n" +
                    "  vars:\n" +
                    "    http_port: 80\n" +
                    "    max_clients: 200\n" +
                    "  remote_user: root\n" +
                    "  tasks:\n" +
                    "  - name: ensure apache is at the latest version\n" +
                    "    yum: pkg=httpd state=latest\n" +
                    "  - name: write the apache config file\n" +
                    "    template: src=/srv/httpd.j2 dest=/etc/httpd.conf\n" +
                    "    notify:\n" +
                    "    - restart apache\n" +
                    "  - name: ensure apache is running\n" +
                    "    service: name=httpd state=started\n" +
                    "  handlers:\n" +
                    "    - name: restart apache\n" +
                    "      service: name=httpd state=restarted");
            }
        },
        onload: function () {
            this.fullscreen();
            this.setToolbarAutoFixed(true);

        },

    }
    KEditor = editormd("PEdit", $scope.option);

}

angular
    .module('inspinia')
    .config(function (jsonrpcConfigProvider) {
        jsonrpcConfigProvider.set({
            url: '/api',
            returnHttpPromise: false
        });
    })
    .controller('MainCtrl', MainCtrl)
    .controller('LoginCtrl', ['$scope', '$state', 'AuthService', LoginCtrl])
    .controller('datatablesCtrl', HostListCtrl)
    .controller('HostAddCtrl', ['$scope', 'jsonrpc', '$cookies', HostAddCtrl])
    .controller('KnowledgeAddCtrl', KnowledgeAddCtrl)
    .controller('KnowlegeGetCtrl', KnowlegeGetCtrl)
    .controller('ProjectListCtrl', ProjectListCtrl)
    .controller('ProjectRunCtrl', ProjectRunCtrl)
    .controller('ProjectConfigCtrl', ProjectConfigCtrl)
    .controller('ProjectDeployCtrl', ProjectDeployCtrl)