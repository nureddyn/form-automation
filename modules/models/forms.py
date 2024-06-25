FORMS = { 
    "health-department": {
        "url": "https://www.alleghenycounty.us/files/assets/county/v/1/government/health/documents/food-safety/",
        "forms": {
            "permanent-food-facility": "perm-food-facility-application_fillable.pdf",
            "mobile-food-facility": "mobile-food-facility-application-final-230131.pdf",
            "change-ownership": "change-of-ownership-app-fillable.pdf",
            "temporary-food-facility": "temporary-checklist-2024.pdf",
            "shared-kitchen": "shared-kitchen-user-app-fillable.pdf",
            "class-1-food-facility": "class-1-registration-application-fillable.pdf"
        }
    }
}

DEPARTMENTS = [department for department in FORMS.keys()]
FORM_NAMES = [form_name for details in FORMS.values() for form_name in details["forms"]]
