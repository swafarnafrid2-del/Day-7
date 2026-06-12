from flakk import Flask, jsonify

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
        "name": "John",
        "age": 21,
        "college": "XYZ College",
        "branch": "Mechanical Engineering"
    },
    {
        "id": 3,
        "name": "Sara",
        "age": 19,
        "college": "PQR College",
        "branch": "Electronics"
    }
]

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)