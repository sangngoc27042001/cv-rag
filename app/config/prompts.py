sys_prompt_cv_extraction = """
Extract the relevant information from the CV and return it in JSON format:
Name: the name of the person
Year of Birth: the year of birth
Year of Experience lower bound: the lower bound of the year of experience
Year of Experience upper bound: the upper bound of the year of experience
Roles: the roles of the person
English Level: the English level of the person
Skills: the skills of the person in technology
Companies: the companies where the person worked

Exmaple:
6+ yoe => Year of Experience lower bound: 6; Year of Experience upper bound: null
6-10 yoe => Year of Experience lower bound: 6; Year of Experience upper bound: 10
"""