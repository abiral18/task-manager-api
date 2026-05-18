from flask import Flask, jsonify

app = Flask(__name__)

# Temporary storage (just a list for now)
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)
from flask import Flask, jsonify, request

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'done': False
    }
    tasks.append(task)
    return jsonify(task), 201
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task['done'] = True
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    tasks.remove(task)
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)