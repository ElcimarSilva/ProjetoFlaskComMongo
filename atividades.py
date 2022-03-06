from bson import json_util, ObjectId
from flask import request, Response, jsonify, flash, redirect, render_template
from app import mongo
from forms import atvdd
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


def create_atividade_form():
    field = atvdd(request.form)

    if request.method == 'POST' and field.validate():
        atividade = request.form['atividade']
        descricao = request.form['descricao']
        json = {'atividade': atividade, 'descricao': descricao}

        mongo.db.atividades.insert_one(json)
        flash('Cadastro efetuado!')
        return redirect('/painel')
    return render_template('cadAtividade.html', field=field)


def get_atividades():
    atividades = mongo.db.atividades.find()
    response = json_util.dumps(atividades)
    return Response(response, mimetype='application/json')


def get_atividade(id):
    atividade = mongo.db.atividades.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(atividade)
    return Response (response, mimetype="application/json")


def detele_atividade(id):
    mongo.db.atividades.delete_one({'_id': ObjectId(id)})
    response = jsonify({'mensagem': 'Atividade: ' + id + 'foi deletada com sucesso!'})
    return response


def update_atividade(id):
    atividade = request.json['atividade']
    descricao = request.json['descricao']

    if atividade and descricao:
        mongo.db.atividades.update_one({'_id': ObjectId(id)}, {'$set': {
            'atividade': atividade,
            'descricao': descricao

        }})
        response = jsonify({'mensagem': 'Atividade: ' + id + 'foi atualizada com sucesso!'})
        return response