from flask import Flask, request, jsonify
import docker

app = Flask(__name__)

@app.route('/', methods=['get'])
def default_page():
    return """
    <h1>For run the container use below URL and modify the values </h1>
    <h2>localhost:8000/run?image=mysql&version=8&hport=1234&cport=3306&cport=&db_user=admin&db_pass=mypass</h2>
    <h1>For delete the container use below URL and use correct containerid</h1>
    <h2>localhost:8000/delete?id=ContainerID</h2>
    """



@app.route('/run', methods=['get'])
def run():
    client = docker.from_env()
    USER = request.args.get('db_user', None) # use default value repalce 'None'
    PASS = request.args.get('db_pass', None)
    IMAGE = request.args.get('image', None)
    CONT = request.args.get('cport', None)
    HOST = request.args.get('hport', None)
    VERSION = request.args.get('version', None)
    target_ports = { HOST : CONT}
    test = (IMAGE, VERSION)
    name = (":".join(test))
    auth = { 'MYSQL_ROOT_PASSWORD' : PASS, 'USER' : USER}
    container = client.containers.run(name, detach=True, ports=target_ports, environment=auth).id
    # do something, eg. return json response
    return jsonify({'DB_USER': USER, 'DB_PASS': PASS, 'CONTAINER_PORT': CONT, 'HOST_PORT' : HOST, 'Container_ID' : container})

@app.route('/delete', methods=['get'])
def delete():
    client = docker.from_env()
    ID = request.args.get('id', None)
    delete = client.containers.get(ID)
    delete.kill()
    delete.remove()
    return """<h1>Container ID is deleted!</h1>"""


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 8000, debug=True)
