# This file has search functions - finding a specific record in a list.

def linear_search_by_name(records, search_name):
    for record in records:
        if record["name"].lower() == search_name.lower():
            return record
    return None  # wala nahanap

def linear_search_by_id(records_dict, search_id):
    return records_dict.get(search_id)

def search_courses_by_keyword(courses_dict, keyword):
    results = []
    for course_code, info in courses_dict.items():
        if keyword.lower() in info["name"].lower():
            results.append((course_code, info))
    return results