from flakk import Flask, jsonify, request

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
        "name": "James",
        "age": 22,
        "college": "PQR College",
        "branch": "Mechanical"
    }
]

@app.route('/search-student/<name>', methods=['GET'])
def search_student(name):
    result = []

    for student in students:
        if student["name"].lower() == name.lower():
            result.append(student)

    if result:
        return jsonify(result)

    return jsonify({"message": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)