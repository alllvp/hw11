import utils
from flask import Flask, render_template

app = Flask(__name__)


def handle_bad_request(e):
    return 'такой страницы не существует', 400


app.register_error_handler(404, handle_bad_request)

candidates = utils.load_candidates_from_json('data', 'candidates.json')


@app.route("/")
def page_index():
    """Выводит список всех кандидатов"""
    return render_template('list.html', candidates_list=candidates)


@app.route("/candidate/<int:number>/")
def page_candidate(number):
    """Выводит данные про кандидата"""
    candidate = utils.get_candidate(number, candidates)
    if candidate != 1:
        return render_template('single.html', single_candidate=candidate)
    else:
        return f"кандидата {number} не существует"


@app.route("/search/<candidate_name>/")
def page_candidates_by_name(candidate_name):
    """Выводит тех кандидатов, в имени у которых содержится candidate_name"""
    selected_candidates = utils.get_candidates_by_name(candidate_name, candidates)
    return render_template('search.html', amount=len(selected_candidates), candidates_list=selected_candidates)


@app.route("/skill/<skill_name>/")
def page_candidates_by_skill(skill_name):
    """Выводит тех кандидатов, в списке навыков у которых содержится skill"""
    selected_candidates = utils.get_candidates_by_skill(skill_name, candidates)
    return render_template('skill.html', skill_name=skill_name,
                           amount=len(selected_candidates), candidates_list=selected_candidates)


app.run()
