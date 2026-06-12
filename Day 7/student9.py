from flakk import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add-student', methods=['POST'])
def add_student():
    data = request.get_json()

    student = {
        "name": data.get("name"),
        "age": data.get("age"),
        "college": data.get("college"),
        "branch": data.get("branch")
    }

    return jsonify({
        "message": "Student Added Successfully",
        "student": student
    })

if __name__ == '__main__':
    app.run(debug=True)
