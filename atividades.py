from bson import json_util, ObjectId
from flask import request, Response, jsonify
from app import mongo
from tratamento_de_erros import not_found


def create_atividade():
    #Recebendo dados
    atividade = request.json['atividade'] #
    descricao = request.json['descricao']

    if atividade and descricao :
        id = mongo.db.atividades.insert(
            {'atividade': atividade, 'descricao': descricao, }
        )                            #INSERÇÃO DE ATIVIDADE
        response = {
            'id': str(id),
            'atividade': atividade,
            'descricao': descricao
        }
        return response
    else:
        return not_found()

    #print (request.json)
    return {'mensagem': 'recebido'}


def get_atividades():
    atividades = mongo.db.atividades.find()
    response = json_util.dumps(atividades)
    return Response(response, mimetype='application/json')


def get_atividade(id):
    atividade = mongo.db.atividades.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(atividade)
    return Response (response, mimetype="application/json")