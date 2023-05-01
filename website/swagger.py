"""Definition of the Swagger UI Blueprint."""

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = "/openapi.json"

# Call factory function to create our blueprint
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Notizen API | Modul 4-WI-113-WWI21B"
    }
)