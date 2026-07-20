"""
WHAT: Custom validation with @field_validator and @model_validator.
WHEN: When built-in Field constraints (gt, max_length...) aren't enough —
      e.g. cleaning strings, cross-field checks.
RUN:  python pydantic/02_validators.py
"""

from pydantic import BaseModel, Field, field_validator, model_validator


class Booking(BaseModel):
    guest_name: str
    nights: int = Field(gt=0)
    check_in_day: int = Field(ge=1, le=31)
    check_out_day: int = Field(ge=1, le=31)

    # Runs on ONE field
    @field_validator("guest_name")
    @classmethod
    def clean_name(cls, v: str) -> str:
        v = v.strip().title()
        if not v:
            raise ValueError("guest_name cannot be blank")
        return v

    # Runs on the WHOLE model — use for cross-field logic
    @model_validator(mode="after")
    def check_dates(self):
        if self.check_out_day <= self.check_in_day:
            raise ValueError("check_out_day must be after check_in_day")
        return self


if __name__ == "__main__":
    b = Booking(guest_name="  lohith d  ", nights=3, check_in_day=10, check_out_day=13)
    print(b)   # guest_name cleaned to 'Lohith D'

    try:
        Booking(guest_name="X", nights=2, check_in_day=20, check_out_day=18)
    except Exception as e:
        print("Cross-field validation caught:", e)
