from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Body
from fastapi.responses import JSONResponse
from typing import List, Dict, Any

from ..services.cv_service import upload_cv, get_cv_by_user_input
from ..shared.utils import serialize_mongo_doc

router = APIRouter(
    prefix="/cv",
    tags=["cv"],
    responses={404: {"description": "Not found"}},
)

@router.post("/upload")
async def upload_cv_endpoint(file: UploadFile = File(...)):
    """
    Upload a CV in PDF format.
    
    This endpoint accepts a PDF file, extracts information from it,
    and stores the extracted data in the database.
    
    Returns the extracted CV data.
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    try:
        # Read the file content
        file_content = await file.read()
        
        # Process the CV
        cv_data = upload_cv(file_content)
        # Serialize the MongoDB document to a JSON-serializable format
        cv_data = serialize_mongo_doc(cv_data)
        
        
        return JSONResponse(
            status_code=200,
            content={"message": "CV uploaded successfully", "data": cv_data}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing CV: {str(e)}")

@router.post("/search")
async def search_cv_endpoint(user_input: str = Body(..., embed=True)):
    """
    Search for CVs based on user input.
    
    This endpoint accepts a string input from the user,
    parses it to extract search criteria, and returns matching CVs.
    
    Returns a list of matching CVs.
    """
    try:
        # Process the user input and get matching CVs
        matching_cvs = get_cv_by_user_input(user_input)
        # Serialize the MongoDB documents to a JSON-serializable format
        matching_cvs = serialize_mongo_doc(matching_cvs)
        
        return JSONResponse(
            status_code=200,
            content={"message": "Search completed", "data": matching_cvs}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching CVs: {str(e)}")
