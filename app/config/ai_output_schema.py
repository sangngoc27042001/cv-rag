from pydantic import BaseModel
from typing import List, Optional, Literal, Union, get_args

# Create type aliases using Union of Literals
RoleType = Literal["Software Engineer", "Data Scientist", "Product Manager", "Data Analyst", "Data Engineer", "Frontend Developer", "Backend Developer", "Full Stack Developer", "DevOps Engineer", "Machine Learning Engineer", "AI Engineer", "Cloud Engineer", "QA Engineer", "Security Engineer"]
TechSkillType = Literal["Python", "Java", "C++", "JavaScript", "C#", "PHP", "Ruby", "Swift", "Kotlin", "Go", "Rust", "TypeScript", "Scala", "Haskell", "SQL", "NoSQL", "HTML", "CSS", "React", "Angular", "Vue", "Node.js", "Express", "Django", "Flask", "Spring", "Hibernate", "TensorFlow", "PyTorch", "Scikit-learn", "Keras", "OpenCV", "NumPy", "Pandas", "Matplotlib", "Seaborn", "SciPy", "NLTK", "spaCy", "BeautifulSoup", "Requests", "Selenium", "Scrapy", "BeautifulSoup", "Tailwind CSS", "Bootstrap", "MongoDB", "MySQL", "PostgreSQL", "Oracle"]
OtherSkillType = Literal["Leadership", "Communication", "Teamwork", "Problem Solving", "Time Management", "Adaptability", "Creativity", "Critical Thinking", "Project Management", "Agile Methodologies", "Scrum", "Kanban", "Lean", "Media Relations"]
EnglishLevelType = Literal["Beginner", "Intermediate", "Advanced", "Native"]

class CVExtraction(BaseModel):
    """
    A class representing the schema for CV extraction results.
    """
    name: str
    email: str
    phone: str
    year_of_birth: int
    year_of_experience: int
    roles: List[RoleType]
    english_level: Optional[EnglishLevelType]
    tech_skills: List[TechSkillType]
    other_skills: List[OtherSkillType]
    companies: List[str]

class ParsedUserInput(BaseModel):
    """
    A class representing the schema for parsed user input.
    """
    name: Optional[str]
    yoe_lower_bound: Optional[int]
    yoe_upper_bound: Optional[int]
    tech_skills: List[TechSkillType]
    other_skills: List[OtherSkillType]
    english_level: Optional[EnglishLevelType]
    roles: List[RoleType]
