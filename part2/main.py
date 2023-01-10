from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
@app.route("/main/")
def main():
    return render_template('main.html', candidates=load_candidates_from_json("candidates.json"))


@app.route("/candidate/<int:x>/")
def all_of_candidates(x):
    if type(get_candidate(int(x))) is dict:
        return render_template('candidate.html', candidate=get_candidate(int(x)))
    else:
        return render_template('none.html')


@app.route("/search/<candidate_name>/")
def search_by_name(candidate_name):
    return render_template('search.html', candidates=get_candidates_by_name(candidate_name), length=len(get_candidates_by_name(candidate_name)))


@app.route("/skill/<skill_name>/")
def search_by_skill(skill_name):
    return render_template('skills.html', candidates=get_candidates_by_skill(skill_name), length=len(get_candidates_by_skill(skill_name)))


if __name__ == "__main__":
    app.run(debug=True)
