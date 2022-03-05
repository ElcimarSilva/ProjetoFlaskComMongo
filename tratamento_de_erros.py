from flask import app, jsonify, request


#@app.errorhandler(404) # deu problema, não sei porque não posso utilizado quando estou em um arquivo externo como este
def not_found():
    response = jsonify({
        'message': 'Recurso não encontrado!' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response
