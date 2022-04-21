import json
import os


def load_candidates_from_json(data_folder, data_filename):

    """Загружает данные (список всех кандидатов) из файла Json и возвращает в виде словаря"""
    data_file_path = os.path.join(data_folder, data_filename)
    with open(data_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id, candidates):

    """возвращает одного кандидата по его id"""
    try:
        candidate = next(filter(lambda _: _['id'] == candidate_id, candidates))
    except StopIteration:
        return 1
    return candidate


def get_candidates_by_name(candidate_name, candidates):

    """Возвращает кандидатов по имени"""
    selected_candidates = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            selected_candidates.append(candidate)
    return selected_candidates


def get_candidates_by_skill(skill_name, candidates):

    """Возвращает кандидатов по имени"""
    selected_candidates = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower():
            selected_candidates.append(candidate)
    return selected_candidates
