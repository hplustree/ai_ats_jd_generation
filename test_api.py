import requests
import json

url = 'http://localhost:8000/generate-job-description/'

payload = {
    'designation': 'Senior Software Engineer',
    'domain': 'IT',
    'min_experience': 3,
    'max_experience': 8,
    'availability': [1, 3],
    'number_of_positions': 2,
    'location': 'Remote',
    'qualification': None,
    'technical_skills': ['Python', 'FastAPI', 'PostgreSQL', 'Docker'],
    'work_preference': [1, 3],
    'sector': 2,
    'software': ['VSCode', 'Git'],
    'big4_experience': 2,
    'travel_required': 1,
    'additional_info': 'Looking for a senior engineer with strong backend skills',
    'store_db': False
}

try:
    response = requests.post(url, json=payload)
    print(f'Status Code: {response.status_code}')
    print(f'Response:\n{json.dumps(response.json(), indent=2)}')
except Exception as e:
    print(f'Error: {e}')
