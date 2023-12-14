from fastapi import FastAPI, HTTPException, Query, APIRouter, Body, Path

from pydantic import BaseModel


app = FastAPI(
    title="Todo List API",
    summary="Doc example for 75",
    version="0.1"
)
root_router = APIRouter()
router = APIRouter(
    prefix="/todos",
    responses={404: {
            "content": {
                    "application/json": {
                        "example": {
                            "detail": "Not found the TODO item",
                        }
                    }
                },
        },
},
)


class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool
    
    class Config:
        schema_extra = {
            "example": {
                "id": 0,
                "task": "do something",
                "completed": False
            }
        }

'''
----------------------------------------------------------------
Routers
----------------------------------------------------------------
'''

@router.get("/{todo_id}",
    summary="Get TODO item by ID",
    response_model=TodoItem,
)
def get_todo_by_id(
    todo_id: int = Path(..., description="This is description about TODO ID ..."),
):
    """
    Get TODO item by ID
    
    - `todo_id`: ID of the TODO item to fetch.
    
    Example:
    - `123`
    - `456`
    - `789`
    """

    pass

@router.get("/",
    summary="Get TODOs",
    response_model=TodoItem,
)
def get_todos(
    tags: str = Query(..., description="This is description about tags ..."),
    limit: int = Query(..., description="This is description about limit ..."),
    skip: int = Query(..., description="This is description about skip ..."),
):
    """
    Get TODOs
    
    Fetches a list of TODO items with optional filtering and pagination.
    
    - `tags`: Filter TODOs by tags.
    - `limit`: Limit the number of results.
    - `skip`: Skip number of results.
    
    Example:
    - `123`
    - `456`
    - `789`
    """
    
    pass
    

@router.post("/",
    summary="Create a TODO item",
    response_model=TodoItem
)
def create_todo(todo: TodoItem):
    """
    Create a new TODO item.
    
    Example:
    - `123`
    - `456`
    - `789`
    """
    pass

@router.put("/{todo_id}",
    summary="Update a TODO item",
    response_model=TodoItem
)
def update_todo(
    todo_id: int = Path(..., description="This is description about TODO ID ..."),
    updated_todo: TodoItem = Body(..., description="This is description about updated_todo...")
):
    """
    Update a TODO item by ID.
    
    - `todo_id`: ID of the TODO item to update.
    
    Example:
    - `123`
    - `456`
    - `789`
    """
    pass


@router.delete(
    "/{todo_id}",
    summary="Delete a TODO item",
    response_model=TodoItem
)
def delete_todo(
    todo_id: int = Path(..., description="This is description about TODO ID ..."),
):
    """
    Delete a TODO item by ID.
    
    - `todo_id`: ID of the TODO item to delete.
    
    Example:
    - `123`
    - `456`
    - `789`
    """
    pass


root_router.include_router(router, tags=["TODOs"])
app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8080)