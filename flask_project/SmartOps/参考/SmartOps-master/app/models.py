from itsdangerous import BadSignature, SignatureExpired, TimedJSONWebSignatureSerializer as Serializer
import werkzeug
from functools import wraps
from flask_jsonrpc import InvalidCredentialsError, InvalidParamsError
from app import db, ma
from config import USER_SECRET_KEY, VERIFY_DEBUG


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(164))

    def password(self, password):
        """
        设置密码hash值
        """
        self.password_hash = werkzeug.security.generate_password_hash(password)

    def verify_password(self, password):
        """
        将用户输入的密码明文与数据库比对
        """

        if self.password_hash:
            return werkzeug.security.check_password_hash(self.password_hash, password)
        return None

    def generate_auth_token(self, expiration=6000):
        s = Serializer(USER_SECRET_KEY, expires_in=expiration)
        return bytes.decode(s.dumps({'id': self.id}))

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(USER_SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

    @staticmethod
    def authenticate(f, f_check_auth):
        @wraps(f)
        def _f(*args, **kwargs):
            is_auth = False
            try:
                creds = args[:2]
                is_auth = f_check_auth(creds[0], creds[1])
                if is_auth:
                    args = args[2:]
            except IndexError:
                if 'token' in kwargs:
                    is_auth = f_check_auth(kwargs['token'])
                    if is_auth:
                        kwargs.pop('token')
                else:
                    raise InvalidParamsError('Authenticated methods require at least '
                                             '[token] or {token: } arguments')
            if not is_auth:
                raise InvalidCredentialsError()
            return f(*args, **kwargs)

        return _f

    @staticmethod
    def check_auth(token):
        # 启用debug模式不需要进行token认证
        if VERIFY_DEBUG:
            return True
        user = User.verify_auth_token(token)
        if user:
            return True
        return False

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(80))
    hostname = db.Column(db.String(80))
    port = db.Column(db.String(80))
    is_active = db.Column(db.String(80))
    public_ip = db.Column(db.String(80))
    number = db.Column(db.String(80))
    # Collect
    vendor = db.Column(db.String(80))
    model = db.Column(db.String(80))
    sn = db.Column(db.String(80))
    cpu_model = db.Column(db.String(80))
    cpu_count = db.Column(db.String(80))
    cpu_cores = db.Column(db.String(80))
    memory = db.Column(db.String(80))
    disk_total = db.Column(db.String(80))
    disk_info = db.Column(db.String(80))
    platform = db.Column(db.String(80))
    os = db.Column(db.String(80))
    os_version = db.Column(db.String(80))
    os_arch = db.Column(db.String(80))
    hostname_raw = db.Column(db.String(80))
    labels = db.Column(db.String(80))
    created_by = db.Column(db.String(80))
    date_created = db.Column(db.String(80))
    comment = db.Column(db.String(80))


class Knowledge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    tag = db.Column(db.String(80))
    description = db.Column(db.String(80))
    content = db.Column(db.UnicodeText())


class AssetSchema(ma.ModelSchema):
    class Meta:
        model = Asset


class KnowledgeSchema(ma.ModelSchema):
    class Meta:
        model = Knowledge


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    path = db.Column(db.String(100))


class ProjectSchema(ma.ModelSchema):
    class Meta:
        model = Project


class ProjectDeploy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    script = db.Column(db.String(50))
    args = db.Column(db.String(50))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship('Project', backref=db.backref('projects'))


class ProjectDeploySchema(ma.ModelSchema):
    class Meta:
        model = ProjectDeploy


class ProjectConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    path = db.Column(db.String(50))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))


class ProjectConfigSchema(ma.ModelSchema):
    class Meta:
        model = ProjectConfig


class ProjectRun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    command = db.Column(db.String(50))
    autostart = db.Column(db.Boolean)
    autorestart = db.Column(db.Boolean)
    startsecs = db.Column(db.String(50))
    startretries = db.Column(db.Integer)
    user = db.Column(db.String(50))
    priority = db.Column(db.Integer)
    redirect_stderr = db.Column(db.Boolean)
    stdout_logfile_maxbytes = db.Column(db.String(50))
    stdout_logfile_backups = db.Column(db.String(50))
    stdout_logfile = db.Column(db.String(50))
    stopasgroup = db.Column(db.Boolean)
    killasgroup = db.Column(db.Boolean)


class ProjectRunSchema(ma.ModelSchema):
    class Meta:
        model = ProjectRun
