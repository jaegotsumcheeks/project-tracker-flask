"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")

    # def get_grades_by_github(github):
    #     """Get a list of all grades for a student by their github username"""

    #     QUERY = """
    #         SELECT project_title, grade
    #         FROM grades
    #         WHERE student_github = :github
    #         """

    #     db_cursor = db.session.execute(QUERY, {'github': github})

    #     rows = db_cursor.fetchall()

    #     for row in rows:
    #         print(f"Student {github} received grade of {row[1]} for {row[0]}")

    #     return rows


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    project_title, grade = hackbright.get_grades_by_github(github)

    print(project_title, grade)

    

    return render_template("student_info.html", 
                            first= first,
                            last= last,
                            github= github,
                            project_title = project_title,
                            grade = grade)

   

@app.route("/create-student")
def create_student():

    return render_template("new_student.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    
    hackbright.make_new_student(first, last, github)
    
    return render_template("successfully_added_student.html", first=first,
                                                                last= last,
                                                                github= github)


    




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
