from flask import Blueprint
from manage import jsonrpc
from app.models import User, Project, ProjectSchema, ProjectDeploy, ProjectDeploySchema, ProjectConfig, \
    ProjectConfigSchema
from app.ansible2.api import ansible_playbook
from app import db

mod = Blueprint('knowledge', __name__)

jsonrpc.register_blueprint(mod)


@jsonrpc.method('project.get', authenticated=User.check_auth)
def project_get():
    projects = []
    project_schema = ProjectSchema()
    p = Project.query.all()
    for i in p:
        projects.append(project_schema.dump(i).data)
    return {'status': 0, 'message': u'获取成功', 'data': projects}


@jsonrpc.method('project.config.save(id=int,content=str)', authenticated=User.check_auth)
def project_config_save(id, content):
    return {'status': 0, 'message': u'保存成功'}


@jsonrpc.method('project.config.list(projectid=int)', authenticated=User.check_auth)
def project_config_list(projectid):
    configs = []
    config_schema = ProjectConfigSchema()
    c = ProjectConfig.query.filter_by(project_id=projectid).all()
    for i in c:
        configs.append(config_schema.dump(i).data)
    return {'status': 0, 'message': u'获取成功', 'data': configs}


@jsonrpc.method('project.deploy.list(projectid=int)', authenticated=User.check_auth)
def project_deploy_list(projectid):
    deploys = []
    deploy_schema = ProjectDeploySchema()
    d = ProjectDeploy.query.filter_by(project_id=projectid).all()
    for i in d:
        deploys.append(deploy_schema.dump(i).data)
    return {'status': 0, 'message': u'获取成功', 'data': deploys}


@jsonrpc.method('project.deploy.save(id=int,content=str)', authenticated=User.check_auth)
def project_deploy_save(id, content):
    d = ProjectDeploy.query.filter_by(name='python_deploy').first()
    with open('%s/deploy/%s.yaml' % (d.project.path, 'python_deploy'), 'w+') as f:
        f.write(content)
    return {'status': 0, 'message': u'保存成功'}


@jsonrpc.method('project.deploy.get(id=int)', authenticated=User.check_auth)
def project_deploy_get(id):
    d = ProjectDeploy.query.filter_by(id=id).first()
    with open('%s/deploy/%s.yaml' % (d.project.path, d.name)) as f:
        return {'status': 0, 'message': u'获取成功', 'data': f.read()}


@jsonrpc.method('project.run(id=int)', authenticated=User.check_auth)
def proejct_run(id):
    d = ProjectDeploy.query.filter_by(name='python_deploy').first()
    return {'status': 0, 'message': u'执行成功',
            'data': ansible_playbook('', '%s/deploy/%s.yaml' % (d.project.path, 'python_deploy'))}
