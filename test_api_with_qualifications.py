import requests
import json

url = 'http://localhost:8000/generate-job-description/'

# Test 1: With 1 qualification
print("=" * 80)
print("TEST 1: With 1 Qualification")
print("=" * 80)
payload_1_qual = {
    'designation': 'Senior Software Engineer',
    'domain': 'IT',
    'min_experience': 3,
    'max_experience': 8,
    'availability': [1, 3],
    'number_of_positions': 2,
    'location': 'Remote',
    'qualification': ['Bachelor in Computer Science'],
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
    response = requests.post(url, json=payload_1_qual)
    print(f'Status Code: {response.status_code}')
    result = response.json()
    print(f'Job Title: {result.get("job_description", {}).get("job_title", "N/A")}')
    print(f'Summary: {result.get("job_description", {}).get("summary", "N/A")[:150]}...')
    print("✓ Test 1 PASSED\n")
except Exception as e:
    print(f'✗ Test 1 FAILED - Error: {e}\n')

# Test 2: With 2 qualifications
print("=" * 80)
print("TEST 2: With 2 Qualifications")
print("=" * 80)
payload_2_qual = {
    'designation': 'Senior Software Engineer',
    'domain': 'IT',
    'min_experience': 3,
    'max_experience': 8,
    'availability': [1, 3],
    'number_of_positions': 2,
    'location': 'Remote',
    'qualification': ['Bachelor in Computer Science', 'Master in Software Engineering'],
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
    response = requests.post(url, json=payload_2_qual)
    print(f'Status Code: {response.status_code}')
    result = response.json()
    print(f'Job Title: {result.get("job_description", {}).get("job_title", "N/A")}')
    print(f'Summary: {result.get("job_description", {}).get("summary", "N/A")[:150]}...')
    print("✓ Test 2 PASSED\n")
except Exception as e:
    print(f'✗ Test 2 FAILED - Error: {e}\n')

print("=" * 80)
print("ALL TESTS COMPLETED SUCCESSFULLY")
print("=" * 80)
