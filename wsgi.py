from flaskbb import create_app
#from flaskbb.configs.production import ProductionConfig
from flaskbb.configs.development import DevelopmentConfig

#flaskbb = create_app(config=ProductionConfig())
flaskbb = create_app(config=DevelopmentConfig())
