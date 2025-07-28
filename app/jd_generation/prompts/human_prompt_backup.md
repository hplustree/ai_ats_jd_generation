


Create a comprehensive, ATS-optimized job description using the following details:

## INPUT FIELDS:

- Designation: {designation}
- Industry/Domain: {domain}
- Minimum Experience: {min_experience} years
- Maximum Experience: {max_experience} years
- Number of Positions: {number_of_positions}
- Location: {job_location}
- Work Arrangement: {work_preference}
- Employment Type: {availability}
- Required Qualification: {qualification}
- Sector: {sector}
- Big 4 Experience Required: {big4_experience}
- Travel Requirement: {travel_required}
- Technical Skills: {key_skills}
- Software Tools: {software_tools}


## SPECIFIC INSTRUCTIONS FOR EACH OUTPUT COMPONENT:

### 1. `job_title` Field Instructions:
- **Rule:** Present the job title exactly as provided in `designation` input or make minimal, highly professional adjustments for capitalization (title case) and standard corporate nomenclature.
- **Example Constraint:** If input is "software engineer", output "Software Engineer". If input is "Sr. Data Scientist", output "Senior Data Scientist". Do not invent titles.

### 2. `location` Field Instructions:
- **Rule:** Present the job location exactly as provided in the `location` input.
- **Example Constraint:** If input is "New York, NY", output "New York, NY". If input is "Remote", output "Remote". Do not add or remove any location details.

### 3. `availability` Field Instructions:
- **Rule:** Present the job type exactly as provided in the `availability` input. Make minor grammatical corrections if necessary 
- **Example Constraint:** f input is "Full-Time", output "Full-Time". If input is "contract", output "Contract". Do not expand or modify the job type beyond minor grammatical fixes.

### 4. `summary` Field Instructions:
- **Rule:** Craft a dynamic, engaging, and unique summary (paragraph format, no bullets) that *immediately* captivates candidates and clearly articulates the role's essence, impact, and value proposition *specific to this job*.
- **Dynamic Elements to Integrate:**
    - Clearly state the core mission and impact of *this specific role* within the given `Industry/Domain` and `Sector`. Explain *how* the role contributes to the organization's goals.
    - Highlight the unique value propositions, growth opportunities, and challenges *relevant to this designation*. What makes this role particularly appealing or demanding?
    - If `Big 4 Experience Required` is true, subtly weave in the relevance of a fast-paced, high-performance consultancy background. Emphasize how this experience will be leveraged in the role.
    - Mention the `Work Arrangement` (e.g., "This role supports our [Work Arrangement] model...") and `job_location` as appropriate.

- **Constraint:** Absolutely avoid generic phrases or boilerplate openings that could apply to any job. Every sentence must directly relate to the provided `Designation`, `Job Title`, `Industry/Domain`, and other input parameters.

### 5. `roles_responsibilities` Field Instructions:
- **Rule:** Generate a comprehensive list of responsibilities that are *strictly and directly derived from the `Job Title`, `Designation`, `Industry/Domain`, and `Experience` level*. Each point must be a distinct, action-oriented statement.
- **Dynamic Elements to     :**
    - Start each point with a strong, varied action verb (e.g., "Design," "Lead," "Implement," "Coordinate," "Analyze," "Develop," "Manage," "Collaborate," "Optimize," "Strategize," "Mentor," "Ensure").
    - Include a balanced mix of:
        - **Core Technical/Functional Duties:** Directly related to the `key_skills` and the functional aspects of the `Job Title`.
        - **Collaborative & Communication Duties:** Emphasize teamwork, stakeholder engagement, and clear reporting relevant to the role's level, if highly applicable and integral to the `Job Title` and `key_skills`.
        - **Strategic & Analytical Tasks:** For mid to senior roles, include responsibilities like problem-solving, decision-making, and contributing to strategy. For entry-level, focus on supporting analysis.
        - **Process Improvement & Innovation Activities:** How the role contributes to efficiency or new approaches.
    - If `Travel Requirement` is specified, integrate it naturally into a relevant responsibility (e.g., "Travel as required to client sites/conferences...").
    - If `Big 4 Experience Required` is true, responsibilities might lean towards project management, client-facing, and fast-paced delivery.
- **Constraints:**
    - Each responsibility must be concise, clearly articulated, and easy to understand.
    - **Crucially, avoid mentioning specific tools/technologies in this section; save them exclusively for `required_skills`**.
    - Ensure every point is specific to the role's context and not a generic responsibility that could fit any job.
    - Vary sentence structure and avoid repetition of action verbs in consecutive points.

### 6. `required_skills` Field Instructions:
- **Rule:** Create a flat bullet-point list of essential skills that are *directly mandated by the `Designation`, `Job Title`, `Industry/Domain`, and specifically the `key_skills` provided in the input*.
- **Dynamic Elements to Integrate:**
    - Begin each skill with a descriptive qualifier (e.g., "Proficiency in," "Extensive experience with," "Expertise in," "Solid understanding of," "Hands-on experience with," "Demonstrated ability in").
    - Organize logically within the flat list, prioritizing core technical skills first, then methodologies, then soft skills.
    - **Technical skills:** Include specific programming languages, software, platforms, tools, and databases *exactly as mentioned in `key_skills`*. Use standard abbreviations (e.g., SQL, MS Excel, AWS, Azure, Python, Java, Salesforce).
    - **Methodologies/Frameworks:** If relevant to the `Job Title` and `Industry/Domain` (e.g., Agile, Scrum, ITIL, DevOps).
    - **Analytical/Problem-Solving:** Include skills like "Strong analytical and problem-solving capabilities" or "Data interpretation and statistical analysis if applicable for the given `Job Title`, `Industry/Domain`, or `key_skills`."
    - **Communication/Interpersonal:** Only include if truly *required* for the role (e.g., "Excellent verbal and written communication skills," "Ability to collaborate effectively with cross-functional teams") and only if relevant to the `Job Title`, `Industry/Domain`, or `key_skills`.
    - **Industry-Specific Knowledge:** If the `Industry/Domain` implies specific regulatory or market knowledge, include it.
- **Constraints:**
    - **Only include skills directly provided or unequivocally implied by the `key_skills` input and the `Job Title` context.** Do not add generic or assumed skills.
    - Ensure keywords are present for ATS optimization.


### 7. `preferred_qualifications` Field Instructions:
- **Rule:** Generate a flat bullet-point list of "nice-to-have" qualifications that would enhance a candidate's profile but are not strictly mandatory. These must be *directly relevant to the `Job Title`, `Designation`, `Industry/Domain`, and `Experience` level*.
- **Dynamic Elements to Integrate:**
    - Always include a bachelor’s degree/master’s degree relevant to the role (e.g., "Bachelor's/ Master'sdegree in [related field]").
    - Always include a sentence about additional relevant experience aligned with the provided experience input:
        - If both `min_experience` and `max_experience` are 0 (or not provided), include the phrase:
            "Freshers or entry-level candidates with strong academic backgrounds may also apply"
        - Otherwise, if either `min_experience` or `max_experience` is greater than 0, include a sentence like:
            "{min_experience} to {max_experience} years of experience in [relevant field]"
    - Include industry certifications (e.g., "PMP certification," "AWS Certified Solutions Architect") if applicale.
    - Mention preferred but not mandatory technical competencies (e.g., "Familiarity with [specific niche tool]").
    - Add leadership, mentoring, or project management experience if applicable and not already covered in `required_skills` or `roles_responsibilities`.
    - If `Big 4 Experience Required` is provided as an input, but not necessarily mandatory for *all* candidates, it could be listed here as a strong preference.
- **Constraints:**
    - **Strictly ensure each point is a 'preferred' qualification and not a 'required' one.**
    - Each point must be directly related to the `Job Title` and `Industry/Domain` and avoid adding irrelevant or generic qualifications.
    - If the role is typically entry-level, emphasize relevant academic projects, internships, or certifications.

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





### 4. `summary` Field Instructions:
- **Rule:** Craft a concise, professional, and targeted summary (paragraph format, no bullets) that opens with "We are seeking a [qualified/skilled/experienced] [job title]" and clearly defines the role's core requirements and purpose specific to this job.
- **Dynamic Elements to Integrate:**
    - Begin with "We are seeking a [relevant qualifier] [job title] with [key requirement/experience]" to immediately establish what you're looking for.
    - Clearly state the primary function and mission of this specific role within the given Industry/Domain and Sector. Explain the main responsibilities and contributions expected.
    - Mention the opportunity to work with specific client types, contribute to business growth, or engage in meaningful work within the organization.
    - Highlight the essential qualifications, experience, and skills relevant to this designation. Focus on what makes the ideal candidate stand out.
    - If `Big 4 Experience Required` is true, subtly weave in the relevance of a fast-paced, high-performance consultancy background. Emphasize how this experience will be leveraged in the role.
    - Subtly reference the `Work Arrangement` and `job_location` when relevant to the role's context.
    - End with emphasis on the candidate's role in ensuring quality, compliance, accuracy, or other key outcomes specific to the position.
- **Content Guidelines:** 
    - Each item should be concise and specific
    - Use clear, professional language
    - Ensure grammatical correctness
    - Focus on qualifications that truly add value to the role
    - Avoid repetition of required skills
- **Constraint:** Absolutely avoid generic phrases or boilerplate openings that could apply to any job. Every sentence must directly relate to the provided `Designation`, `Industry/Domain`, and other input parameters.