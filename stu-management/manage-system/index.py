from flask import Flask, render_template
import dao


system = Flask(__name__)


@system.route("/")
def index():
    stu_list = dao.load_student_list()
    return render_template('index.html', student_list = stu_list)


if __name__ == '__main__':
    system.run(debug=True)