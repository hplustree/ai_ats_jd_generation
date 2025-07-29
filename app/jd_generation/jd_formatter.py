from app.schemas.jd_input import JobDescriptionInput
from typing import Dict, Any

AVAILABILITY_MAP = {
    1: "Full-Time",
    2: "Part-Time",
    3: "Contractual",
    4: "Temporary",
    5: "Seasonal"
}

WORK_PREFERENCE_MAP = {
    1: "Remote",
    2: "WFO",
    3: "Hybrid"
}

SECTOR_MAP = {
    1: "Public",
    2: "Private",
    3: "Both"
}

BIG4_MAP = {
    1: "Yes",
    2: "No"
}

TRAVEL_REQUIRED_MAP = {
    1: "No",
    2: "Occasional",
    3: "Frequent"
}


def convert_experience(value: float | None) -> float | int | None:
    if value is None:
        return None
    return int(value) if value == int(value) else value


async def format_job_input_data(data: JobDescriptionInput) -> Dict[str, Any]:
    try:
        min_exp = convert_experience(data.min_experience)
        max_exp = convert_experience(data.max_experience)

        key_skills = ", ".join(data.technical_skills)
        software_tools = ", ".join(data.software) if data.software else None

        availability_options = [AVAILABILITY_MAP.get(val, "Not provided") for val in data.availability]
        work_preferences = [WORK_PREFERENCE_MAP.get(val, "Not provided") for val in data.work_preference]

        return {
            "job_id": data.job_id,
            "user_id": data.user_id,
            "designation": data.designation,
            "domain": data.domain,
            "min_experience": min_exp,
            "max_experience": max_exp,
            "number_of_positions": data.number_of_positions,
            "job_location": data.location,
            "work_preference": work_preferences,
            "availability": availability_options,
            "qualification": data.qualification,
            "sector": SECTOR_MAP.get(data.sector, "Not provided"),
            "big4_experience": BIG4_MAP.get(data.big4_experience, "Not provided"),
            "travel_required": TRAVEL_REQUIRED_MAP.get(data.travel_required, "Not provided"),
            "key_skills": key_skills,
            "software_tools": software_tools
        }

    except Exception as e:
        raise RuntimeError(f"Error while formatting job input: {e}") from e
