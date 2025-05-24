from exceptions.exceptions import InvalidAgeError , InvalidGenderError,InvalidDateError
# Validation Functions
def validate_doctor_age(age: int):
    """
    Validates the age for a doctor.
    Raises:
        InvalidAgeError: if age is not in valid range for doctors.
    """
    if not (25 <= age <= 70):
        raise InvalidAgeError("Doctor's age must be between 25 and 70.")

def validate_patient_age(age: int):
    """
    Validates the age for a patient.
    Raises:
        InvalidAgeError: if age is negative or unrealistic.
    """
    if not (0 < age <= 120):
        raise InvalidAgeError("Patient age must be between 1 and 120.")

def validate_gender(gender: str):
    """
    Validates gender input.
    Raises:
        InvalidGenderError: if gender is not Male/Female/Other.
    """
    allowed_genders = {"male", "female", "other"}
    if gender.lower() not in allowed_genders:
        raise InvalidGenderError(gender)

def validate_date(date: str):
    """
    Validates date input.
    Raises:
        InvalidDateError: if date is not in valid format.
    """
    try:
        import datetime
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise InvalidDateError("Date format must be YYYY-MM-DD.")
    
