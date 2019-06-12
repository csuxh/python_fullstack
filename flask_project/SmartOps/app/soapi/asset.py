from flask import Blueprint
from manage import jsonrpc
from app.models import User, Asset, AssetSchema
from app import db

mod = Blueprint('user', __name__)

jsonrpc.register_blueprint(mod)


@jsonrpc.method('asset.add(assetinfo=list)->Object', authenticated=User.check_auth)
def asset_add(assetinfo):
    try:
        for i in assetinfo:
            _asset = Asset(hostname_raw=i['hostname_raw'], ip=i['ip'], port=i['ip'], vendor=i['vendor'],
                           model=i['model'], cpu_model=i['cpu_model'], cpu_count=i['cpu_count'],
                           cpu_cores=i['cpu_cores'], memory=i['memory'], platform=i['platform'], os=i['os'],
                           os_version=i['os_version'], os_arch=i['os_arch']
                           )
            db.session.add(_asset)
        db.session.commit()
        return {"static": 0, "message": u"添加成功"}
    except Exception as e:
        return {"static": 1, "messsage": e}


@jsonrpc.method('asset.get', authenticated=User.check_auth)
def asset_get():
    try:
        asset_schema = AssetSchema()
        ret = Asset.query.all()
        ret_data = []
        for i in ret:
            ret_data.append(asset_schema.dump(i).data)
        return {"static": 0, "message": u"添加成功", "data": ret_data}

    except Exception as e:
        return {"static": 1, "messsage": e}
