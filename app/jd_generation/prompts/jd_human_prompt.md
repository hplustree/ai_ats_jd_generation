Create a comprehensive, ATS-optimized job description using the following details:

## INPUT FIELDS:

- Designation: {designation}
- Industry/Domain: {domain}
- Minimum Experience: {min_experience} years
- Maximum Experience: {max_experience} years
- Number of Positions: {number_of_positions}
- Location: {job_location}
- Work Preference: {work_preference}
- Employment Type: {availability}
- Required Qualification: {qualification}
- Sector: {sector}
- Big 4 Experience Required: {big4_experience}
- Travel Requirement: {travel_required}
- Technical Skills: {key_skills}
- Software Tools: {software_tools}
- Additional Information: {additional_info}


## SPECIFIC INSTRUCTIONS FOR EACH OUTPUT COMPONENT:

### 1. `job_title` Field Instructions:
- **Rule:** Present the job title exactly as provided in `designation` input with proper title case formatting.
- **Format:** "[Title] – [Domain]"
- **Example:** If designation is "Director" and domain is "Tax and Compliance", output "Director – Tax and Compliance"

### 2. `location` Field Instructions:
- **Rule:** Present the job location exactly as provided in the `location` input.
- **Example Constraint:** If input is "New York, NY", output "New York, NY". If input is "Remote", output "Remote". Do not add or remove any location details.

### 3. `availability` Field Instructions:
- **Rule:** 
    - Present the `availability` field in the following format:
        - Always include both availability and work_preference:  
          **Format:** "[employment_type], [work_mode]"
- **Work Mode Conversions:**
  - WFO → Work-from-Office
  - Remote → Remote
  - Hybrid → Hybrid
- **Example:** 
    - Single Values
        - Single availability with single work_preference: If availability is "Full-Time" and work_preference is "WFO", output: "Full-Time, Work-from-Office"
        - Single availability with single work_preference: If availability is "Part-Time" and work_preference is "Remote", output: "Part-Time, Remote"
        - Single availability with single work_preference: If availability is "Contractual" and work_preference is "Hybrid", output: "Contractual, Hybrid"
    - Multiple Values
        - Multiple availability with single work_preference: If availability is ["Full-Time", "Part-Time"] and work_preference is "Remote", output: "Full-Time, Part-Time, Remote"
        - Multiple availability with single work_preference: If availability is ["Contractual", "Temporary"] and work_preference is "WFO", output: "Contractual, Temporary, Work-from-Office"
        - Single availability with multiple work_preference: If availability is "Full-Time" and work_preference is ["Remote", "Hybrid"], output: "Full-Time, Remote, Hybrid"
        - Single availability with multiple work_preference: If availability is "Part-Time" and work_preference is ["WFO", "Hybrid"], output: "Part-Time, Work-from-Office, Hybrid"
        - Multiple availability with multiple work_preference: If availability is ["Full-Time", "Part-Time"] and work_preference is ["Remote", "WFO"], output: "Full-Time, Part-Time, Remote, Work-from-Office"
        - Multiple availability with multiple work_preference: If availability is ["Contractual", "Seasonal"] and work_preference is ["Hybrid", "Remote"], output: "Contractual, Seasonal, Hybrid, Remote"


### 4. `summary` Field Instructions:
- **Rule:** Strictly ensure that must be generate a concise, strategic, and designation-specific summary as a single short paragraph (max 2–3 lines), highlighting the role’s core value within the organization.
- **Dynamic Elements to Integrate:**
    * Strictly ensure that must be begin with the opening statement:
    - "We are seeking a [Adjective] [designation] to join our team in the [Industry/Domain] sector"
    - Clearly state the core mission and impact of *this specific role* within the given `Industry/Domain` and `Sector`. Explain *how* the role contributes to the organization's goals.
    - Mention the opportunity to work with specific client types, contribute to business growth, or engage in meaningful work within the organization.
    - Highlight the unique value propositions, growth opportunities, and challenges *relevant to this designation*. What makes this role particularly appealing or demanding?
    - End with emphasis on the candidate's role in ensuring quality, compliance, accuracy, or other key outcomes specific to the position.
- **Sector Rules:**
    - If Sector is "Public": "public sector"
    - If Sector is "Private": "private sector"
    - If Sector is "Both": "public and private sectors"
- **Dynamic Adjective Selection Based on Designation Level:**
    * Senior/Executive Level (CEO, CTO, VP, Director, Senior Manager, Principal, etc.):
        - "highly experienced and strategic"
        - "highly accomplished"
    * Mid-Level/Professional (Manager, Team Lead, Analyst, Consultant, Specialist, etc.):
        - "highly skilled and detail-oriented"
        - "experienced and results-driven"
        - "talented and motivated"
        - "skilled"
    * Entry-Level/Junior (Associate, Junior, Trainee, Graduate, Assistant, etc.):
        - "motivated and eager-to-learn"
        - "detail-oriented and enthusiastic"
        - "dedicated and ambitious"
    * Basic/Support Level (Clerk, Peon, Helper, Attendant, etc.):
        - Use no adjective - directly state: "We are seeking [designation] to join our team"
        - Alternative: "reliable" or "dedicated" (only if appropriate for the role context)
- **Content Guidelines:** 
    - Each item should be concise and specific
    - Use clear, professional language
    - Ensure grammatical correctness
    - Focus on qualifications that truly add value to the role
    - Avoid repetition of required skills
    - **Adjective Selection Logic:** Analyze the `designation` to determine its hierarchical level before selecting the appropriate adjective category
- **Constraint:** Absolutely avoid generic phrases or boilerplate openings that could apply to any job. Every sentence must directly relate to the provided `Designation`, `Industry/Domain`, and other input parameters. Adjectives must align with the seniority and nature of the designation.


### 5. `roles_responsibilities` Field Instructions:
- **Rule:** Generate a comprehensive numbered python list of responsibilities that are *strictly and directly derived from the `Designation`, `Industry/Domain`, and `Experience` level*. Each point must be a distinct, action-oriented statement.
- **Dynamic Elements to:**
    - Start each point with a strong, varied action verb (e.g., "Design," "Lead," "Implement," "Coordinate," "Analyze," "Develop," "Manage," "Collaborate," "Optimize," "Strategize," "Mentor," "Ensure").
    - Include a balanced mix of:    
        - **Core Technical/Functional Duties:** Directly related to the `key_skills` and the functional aspects of the `designation`.
        - **Collaborative & Communication Duties:** Emphasize teamwork, stakeholder engagement, and clear reporting relevant to the role's level, if highly applicable and integral to the `designation` and `key_skills`.
        - **Strategic & Analytical Tasks:** For mid to senior roles, include responsibilities like problem-solving, decision-making, and contributing to strategy. For entry-level, focus on supporting analysis.
        - **Process Improvement & Innovation Activities:** How the role contributes to efficiency or new approaches.
    - If `Travel Requirement` is "Occasional" or "Frequent", integrate it naturally into a relevant responsibility (e.g., "Travel occasionally to client sites/conferences..." for Occasional, "Travel frequently to client sites/conferences..." for Frequent). If Travel Requirement is "No", do not mention travel in the responsibilities.
- **Content Guidelines:** 
    - Each item must be a short, single sentence (max 13–16 words) that is clear, direct and action-oriented.
    - Use clear, professional language
    - Ensure grammatical correctness
    - Avoid repetition of required skills
- **Formatting Rules:** 
    - Stictly ensure that must be use numbered list format (1., 2., 3., etc.)
    - Present each sentence as a complete, grammatically correct sentence
    - Maintain consistent structure throughout
- **Constraints:**
    - Each responsibility must be concise, clearly articulated, and easy to understand.
    - Avoid using more than one comma per sentence; break down compound thoughts into separate responsibilities if needed.
    - **Crucially, avoid mentioning specific tools/technologies in this section; save them exclusively for `required_skills`**.
    - Ensure every point is specific to the role's context and not a generic responsibility that could fit any job.
    - Vary sentence structure and avoid repetition of action verbs in consecutive points.
    - **Output Format:** Strictly ensure that must be present all `roles_responsibilities` as a numbered list (1., 2., 3., etc.) in the python list rather than bullet points.
- **Example format:**
    [
        "1. ...,
        "2. ...
    ]


### 6. `required_skills` Field Instructions:
- **Rule:** Create a numbered list of essential skills that are directly mandated by the `Designation`, `Industry/Domain`, specifically the `key_skills` and `software_tools` provided in the input.
- **Dynamic Elements to Integrate:**
    - Concise Format: Each skill should be a brief, direct statement without lengthy descriptive qualifiers
    - Smart Grouping: When multiple related tools, forms, or technologies are present, intelligently group them under umbrella categories
    - Prioritization: Order logically - core technical skills first, then methodologies, then analytical capabilities
  - **Smart Grouping:** When multiple related tools, forms, or technologies are present, intelligently group them under umbrella categories where logical (e.g., "Strong working knowledge of [Tool A], [Tool B], and [Tool C]" or "Expertise in international reporting, including:").
- **Technical Skills Structure:**
  - **Primary Technical Skills:** Include specific programming languages, software, platforms, tools, and databases exactly as mentioned in `key_skills` and `software_tools`.  
  - **Related Tool Grouping:** When 2+ similar tools/software are present, group them under a single numbered item with descriptive category (e.g., "Strong working knowledge of [category]: [Tool 1], [Tool 2], and [Tool 3]").
  - **Form/Document Grouping:** When multiple related forms or documents are present, create a parent category with sub-items using format:
        X. Expertise in [category name], including:
        • [Form/Document 1] – [Brief description]
        • [Form/Document 2] – [Brief description]
  - **Tool Grouping:** When 2+ similar tools/software are present, group them as: "Strong working knowledge of [Tool 1], [Tool 2], and [Tool 3]"
- **Methodologies/Frameworks:** If relevant to the `Designation` and `Industry/Domain` (e.g., Agile, Scrum, ITIL, DevOps).
- **Analytical/Problem-Solving:** Include skills like "Strong analytical and problem-solving capabilities" or "Data interpretation and statistical analysis" if applicable for the given `Designation` `Industry/Domain`, or `key_skills`.
- **Communication/Interpersonal:** Only include if truly *required* for the role (e.g., "Excellent verbal and written communication skills," "Ability to collaborate effectively with cross-functional teams") and only if relevant to the `Designation`, `Industry/Domain`, or `key_skills`.
- **Industry-Specific Knowledge:** If the `Industry/Domain` implies specific regulatory or market knowledge, include it.
- **Content Guidelines:** 
    - Each item must be a short, single sentence (max 10–12 words) that is clear, direct and action-oriented.
    - Use clear, professional language
    - Ensure grammatical correctness
    - Avoid repetition of required skills
- **Formatting Rules:**
  - Stictly ensure that must be use numbered list format (1., 2., 3., etc.)
  - For grouped sub-items under any main point, use bullet points (`•`) with **5 spaces indentation** before each bullet (e.g., `"     • Sub-item"`)
  - Do not begin bullet lines with numbers or tabs.
  - Keep each main item to one concise line when possible
  - Ensure consistent formatting throughout
- **Constraints:**
    - Only include skills directly provided or unequivocally implied by the `key_skills` input and the `Designation` context
    - Avoid generic or assumed skills
    - Prioritize clarity and brevity over lengthy descriptions
    - Group similar items intelligently to avoid redundancy
    - **Output Format:**  Strictly ensure that must be present all `required_skills` as a numbered list (1., 2., 3., etc.) in the python list rather than bullet points.
- **Example format:**
    [
        "1. ...,
        "2. ...
    ]

### 7. `preferred_qualifications` Field Instructions:
- **Rule:** Generate a numbered list of "nice-to-have" qualifications that would enhance a candidate's profile but are not strictly mandatory. These must be *directly relevant to the *`Designation`*, *`Industry/Domain`*, and *`Experience`* level*.
- **Dynamic Elements to Integrate:**
    - "Always include all relevant fields in the format: 'Bachelor's degree in [Field1], [Field2], ... or a related field.' If the `qualification` specifies a 'Master's degree' or 'PhD', output it as-is without adding any additional qualifications or preferences unless explicitly stated in the input."
    - If the input contains only professional certifications (e.g., CA, CPA, ACCA), output them as-is, without inserting a bachelor's or master's degree unless explicitly mentioned.

    **Examples**:
        Input: "qualification": "PhD in Accounting, Finance, or a related field"
        Output: "PhD in Accounting, Finance, or a related field."
        
        Input: "qualification": "Bachelor’s degree in Computer Science or a related field"
        Output: "Bachelor’s degree in Computer Science or a related field."

        Input: "qualification": "Master’s degree in Business Administration required"
        Output: "Master’s degree in Business Administration required."

        Input: "qualification": "Bachelor’s degree in Marketing, Communications, or a related field; Master’s degree preferred"
        Output: "Bachelor’s degree in Marketing, Communications, or a related field; Master’s degree preferred."

        Input: "qualification": "CA, CPA, ACCA"
        Output: "CA, CPA, ACCA, or a related professional qualification."

    - Always include a sentence about additional relevant experience aligned with the provided experience input:
        - If both `min_experience` and `max_experience` are 0 (or not provided), include the phrase:
            "Freshers or entry-level candidates with strong academic backgrounds may also apply"
        - If both `min_experience` and `max_experience` are the same value (and greater than 0), include:
            "Minimum {min_experience} years of experience in [relevant field]"
        - Otherwise, if either `min_experience` or `max_experience` is greater than 0, include a sentence like:
            "{min_experience} to {max_experience} years of experience in [relevant field]"
    - Include industry certifications (e.g., "PMP certification," "AWS Certified Solutions Architect") if applicable.
    - Mention preferred but not mandatory technical competencies (e.g., "Familiarity with [specific niche tool]").
    - Add leadership, mentoring, or project management experience if applicable and must not already covered in `required_skills` or `roles_responsibilities`.
    - If `Big 4 Experience Required` is yes in provided input, but not necessarily mandatory for *all* candidates, it could be listed here as a strong preference.
- **Content Guidelines:** 
    - Each item must be a short, single sentence that is clear, direct and action-oriented.
    - Use clear, professional language
    - Ensure grammatical correctness
    - Focus on qualifications that truly add value to the role
    - Avoid repetition of required skills
- **Formatting Rules:** 
    - Stictly ensure that must be use numbered list format (1., 2., 3., etc.)
    - Present each qualification as a complete, grammatically correct sentence
    - Maintain consistent structure throughout
    - Order from most important to least important qualifications
- **Constraints:**
    - **Strictly ensure each point is a 'preferred' qualification and not a 'required' one.**
    - Each point must be directly related to the `Job Title` and `Industry/Domain` and avoid adding irrelevant or generic qualifications.
    - If the role is typically entry-level, emphasize relevant academic projects, internships, or certifications.
    - **Output Format:** Strictly ensure that must be present all `preferred_qualifications` as a numbered list (1., 2., 3., etc.) in the python list rather than bullet points.
- **Example format:**
    [
        "1. ...,
        "2. ...
    ]

## GENERATE THE FOLLOWING OUTPUT IN JSON FORMAT:

{{
  "job_title": "...",
  "location": "...",
  "availability": "...",
  "summary": "...",
  "roles_responsibilities": "...",
  "required_skills": "...",
  "preferred_qualifications": "..."
}}

### QUALITY ASSURANCE CHECKLIST (Self-Correction/Verification):
- Professional, formal tone throughout.
- Active voice and varied sentence structure used consistently.
- No redundancy or overlapping information between sections (`roles_responsibilities`, `required_skills`, `preferred_qualifications`).
- ATS-friendly formatting and strategic keyword placement.
- Industry-appropriate terminology used correctly and contextually.
- Inclusive and legally compliant language maintained.
- Clear value proposition articulated for candidates.
- Comprehensive coverage of role expectations based *only* on provided inputs.
- Ready for immediate publication on global job platforms.

Generate the complete job description following this exact structure in proper JSON format and quality standards.