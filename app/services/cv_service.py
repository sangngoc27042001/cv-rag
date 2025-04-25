from ..shared.pdf_parse_service import extract_text_from_pdf
from ..shared.llm_service import get_response, get_parsed_response
from ..config import prompts, ai_output_schema
from ..shared.database import db

def upload_cv(pdf_file_content):
    # extract text from the PDF file
    text = extract_text_from_pdf(pdf_file_content)

    # send the text to the LLM and get the response
    cv_object = get_parsed_response(
        text,
        prompts.sys_prompt_cv_extraction,
        ai_output_schema.CVExtraction
    )
    cv_object.update({"cv_raw_content": text})

    # store to the database
    db['candidates'].insert_one(cv_object)

    return cv_object

def get_cv_by_id(cv_id):
    cv_object = db['candidates'].find_one({"_id": cv_id})
    return cv_object

def get_cv_by_general_search(
    name: str = None,
    yoe_lower_bound: int = None,
    yoe_upper_bound: int = None,
    skills: list[str] = [],
    english_level: str = None,
    roles: list[str] = [],
):
    # Build the query filter based on provided parameters
    query = {}
    
    # Add name filter (using case-insensitive regex for partial matching)
    # This will match if the input name is contained within record.name
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    
    # Add year of experience range filter
    if yoe_lower_bound is not None or yoe_upper_bound is not None:
        yoe_query = {}
        if yoe_lower_bound is not None:
            yoe_query["$gte"] = yoe_lower_bound
        if yoe_upper_bound is not None:
            yoe_query["$lte"] = yoe_upper_bound
        if yoe_query:
            query["year_of_experience"] = yoe_query
    
    # Add skills filter (using $all to match all specified skills)
    # This ensures that the record's skills include all the skills in the query
    if skills and len(skills) > 0:
        query["skills"] = {"$all": skills}
    
    # Add english level filter (exact match)
    if english_level:
        query["english_level"] = english_level
    
    # Add roles filter (using $all to match all specified roles)
    # This ensures that the record's roles include all the roles in the query
    if roles and len(roles) > 0:
        query["roles"] = {"$all": roles}
    
    # Execute the query and return the results
    results = list(db['candidates'].find(query))
    return results

def get_cv_by_user_input(user_input: str):
    # send the user input to the LLM and get the response
    cv_object: ai_output_schema.ParsedUserInput = get_parsed_response(
        user_input,
        prompts.sys_prompt_cv_extraction,
        ai_output_schema.ParsedUserInput,
        json_dump=False
    )

    cvs = get_cv_by_general_search(
        name=cv_object.name,
        yoe_lower_bound=cv_object.yoe_lower_bound,
        yoe_upper_bound=cv_object.yoe_upper_bound,
        skills=cv_object.skills,
        english_level=cv_object.english_level,
        roles=cv_object.roles
    )

    return cvs