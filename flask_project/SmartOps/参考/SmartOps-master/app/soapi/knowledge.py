from flask import Blueprint
from manage import jsonrpc
from app.models import Knowledge, User, KnowledgeSchema
from app import db

mod = Blueprint('knowledge', __name__)

jsonrpc.register_blueprint(mod)


@jsonrpc.method('knowledge.put(knowledges=dict)->Object', authenticated=User.check_auth)
def knowledge_put(knowledges):
    try:
        i = knowledges
        _k = Knowledge.query.filter_by(title=i['title']).first()
        message = u"添加成功"
        if not _k:
            k = Knowledge(title=i['title'], tag=i['tag'], description=i['description'], content=i['content'])

            db.session.add(k)
        else:
            _k.tag = i['tag']
            _k.content = i['content']
            _k.description = i['description']
            message = u"修改成功"
        db.session.commit()
        return {"static": 0, "message": message}

    except Exception as e:
        return {"static": 1, "messsage": e}


@jsonrpc.method('knowledge.get(type=str)', authenticated=User.check_auth)
def knowledge_get(type):
    try:
        if type == 'all':
            knowledge_schema = KnowledgeSchema()
            knowledges = Knowledge.query.all()
            data = []
            for i in knowledges:
                data.append(knowledge_schema.dump(i).data)
            return {"status": 0, "message": "获取全部成功", "data": data}
    except Exception as e:
        return {"status": 1, "message": e}
