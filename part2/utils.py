import json


# конвертирование текста json из файла
def load_candidates_from_json(path):
    with open(path, encoding='UTF-8') as f:
        text = json.load(f)
    return text


# вывод всех кандидатов с конкретным именем
def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json('candidates.json')
    candidates_by_name = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            candidates_by_name.append(candidate)
    return candidates_by_name


# возвращается кандидат по номеру
def get_candidate(candidate_id):
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    else:
        return f"Не существует кандидата с номером {candidate_id}"


# выводит кандидатов по конкретному навыку
def get_candidates_by_skill(skill_name):
    candidates = load_candidates_from_json('candidates.json')
    candidates_skill = []
    for candidate in candidates:
        candidate_skill = [i.lower() for i in candidate['skills'].split(', ')]
        if skill_name in candidate_skill:
            candidates_skill.append(candidate)
    return candidates_skill
