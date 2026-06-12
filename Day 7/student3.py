from flakk import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.get_json()

    student = {
        "name": data["name"],
        "age": data["age"],
        "college": data["college"],
        "branch": data["branch"]
    }

    students.append(student)

    return jsonify({
        "message": "Student Added Successfully",
        "student": student
    })

if __name__ == '__main__':
    app.run(debug=True)