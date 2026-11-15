
from flask import Flask, jsonify, request

app = Flask(__name__)

# Student Data
students = [
    {"id": 1, "name": "Rahul", "age": 21, "course": "BCA"},
    {"id": 2, "name": "Priya", "age": 22, "course": "MCA"}
]


# Home API
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Student Management API",
        "status": "Success"
    })


# GET All Students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify({
        "status": "Success",
        "students": students
    })


# POST Add Student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Valid JSON data is required"}), 400

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Valid name is required"}), 400

    if not isinstance(course, str) or not course.strip():
        return jsonify({"error": "Valid course is required"}), 400

    if isinstance(age, bool) or not isinstance(age, int) or age <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400

    new_student = {
        "id": max([s["id"] for s in students], default=0) + 1,
        "name": name.strip(),
        "age": age,
        "course": course.strip()
    }

    students.append(new_student)

    return jsonify({
        "message": "Student added successfully",
        "student": new_student
    }), 201


# PUT Update Student
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = next(
        (s for s in students if s["id"] == student_id), None
    )

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Valid JSON data is required"}), 400

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Valid name is required"}), 400

    if isinstance(age, bool) or not isinstance(age, int) or age <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400

    if not isinstance(course, str) or not course.strip():
        return jsonify({"error": "Valid course is required"}), 400

    student["name"] = name.strip()
    student["age"] = age
    student["course"] = course.strip()

    return jsonify({
        "message": "Student updated successfully",
        "student": student
    }), 200


# DELETE Student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = next(
        (s for s in students if s["id"] == student_id), None
    )

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    students.remove(student)

    return jsonify({
        "message": "Student deleted successfully",
        "student": student
    }), 200


# Run Application
if __name__ == "__main__":
    app.run(debug=True)
