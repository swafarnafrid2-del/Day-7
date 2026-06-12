from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "James",
        "age": 20,
        "college": "ABC College",
        "branch": "Computer Science"
    },
    {
        "id": 2,
        "name": "Sarah",
        "age": 21,
        "college": "XYZ College",
        "branch": "Electronics"
    },
    {
        "id": 3,
        "name": "John",
        "age": 22,
        "college": "PQR College",
        "branch": "Mechanical"
    }
]

@app.route('/delete-student/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students

    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({
                "message": "Student deleted successfully"
            })

    return jsonify({
        "message": "Student not found"
    }), 404

if __name__ == '__main__':
    app.run(debug=True)