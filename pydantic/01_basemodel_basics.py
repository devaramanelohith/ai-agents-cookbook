"""
WHAT: Pydantic BaseModel basics — define, create, convert to/from dict & JSON.
WHEN: Any time you need validated, typed data structures (agent inputs/outputs, API payloads).
RUN:  python pydantic/01_basemodel_basics.py
"""

from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: int = Field(gt=0, description="Age in years, must be positive")
    email: str | None = None          # optional field
    skills: list[str] = []            # default empty list


if __name__ == "__main__":
    # Create — keyword args, validated at creation time
    u = User(name="Lohith", age=28, skills=["python", "langchain"])
    print(u)

    # Model → dict / JSON
    print(u.model_dump())        # {'name': 'Lohith', 'age': 28, ...}
    print(u.model_dump_json())   # '{"name":"Lohith","age":28,...}'

    # Dict / JSON → model (validates!)
    u2 = User.model_validate({"name": "Asha", "age": 30})
    u3 = User.model_validate_json('{"name": "Ravi", "age": 25}')
    print(u2, u3)

    # Validation failure — this raises ValidationError
    try:
        User(name="Bad", age=-5)
    except Exception as e:
        print("Validation caught:", e)
