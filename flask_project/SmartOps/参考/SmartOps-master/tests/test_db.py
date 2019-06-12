from app.models import ProjectDeploy


def deploy_get():
    q = ProjectDeploy.query.filter(name='python_deploy')
    print(q)


if __name__ == '__main__':
    deploy_get()
