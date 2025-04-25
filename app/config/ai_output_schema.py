from pydantic import BaseModel
from typing import List, Optional, Literal

class CVExtraction(BaseModel):
    """
    A class representing the schema for CV extraction results.
    """
    name: str
    email: str
    phone: str
    year_of_birth: int
    year_of_experience: int
    roles: List[Literal["Software Engineer", "Data Scientist", "Product Manager", "Data Analyst", "Data Engineer", "Frontend Developer", "Backend Developer", "Full Stack Developer", "DevOps Engineer", "Machine Learning Engineer", "AI Engineer", "Cloud Engineer", "QA Engineer", "Security Engineer"]]
    english_level: Literal["Beginner", "Intermediate", "Advanced", "Native"]
    skills: List[Literal["Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go", "Swift", "Kotlin", "R", "SQL", "NoSQL", "HTML", "CSS", "React", "Angular", "Vue.js", "Django", "Flask", "Spring Boot", "Node.js", "Express.js", "TensorFlow", "PyTorch", "Keras"]]
    companies: List[str]

class ParsedUserInput(BaseModel):
    """
    A class representing the schema for parsed user input.
    """
    name: Optional[str]
    yoe_lower_bound: Optional[int]
    yoe_upper_bound: Optional[int]
    skills: List[Literal["Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go", "Swift", "Kotlin", "R", "SQL", "NoSQL", "HTML", "CSS", "React", "Angular", "Vue.js", "Django", "Flask", "Spring Boot", "Node.js", "Express.js", "TensorFlow", "PyTorch", "Keras"]]
    english_level: Optional[Literal["Beginner", "Intermediate", "Advanced", "Native"]]
    roles: List[Literal["Software Engineer", "Data Scientist", "Product Manager", "Data Analyst", "Data Engineer", "Frontend Developer", "Backend Developer", "Full Stack Developer", "DevOps Engineer", "Machine Learning Engineer", "AI Engineer", "Cloud Engineer", "QA Engineer", "Security Engineer"]]