from flask_swagger_ui import get_swaggerui_blueprint

swagger = get_swaggerui_blueprint(
    '/swagger',
    '/static/swagger.yaml',
    config={'app_name': "Todo Review 1.1.0"}
)