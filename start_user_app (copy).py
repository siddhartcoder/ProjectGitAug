# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from api.routes import app
from src.python.app.constant.global_data import GlobalData
from src.python.app.constant.project_constant import Constant as constant
from src.python.app.common.config_manager import cfg
from api.routes import api_handler


def set_execution_environment():
    """
    Setting up environment configuration
    """
    try:
        execution_env = cfg.get_default_config(
            constant.CONFIG_DEFAULT_EXECUTION_ENVIRONMENT)
        if execution_env.lower() == constant.EXECUTION_ENVIRONMENT_LOCAL:
            GlobalData.exec_environment_config = constant.CONFIG_LOCAL_ENVIRONMENT
        elif execution_env.lower() == constant.EXECUTION_ENVIRONMENT_DEV:
            GlobalData.exec_environment_config = constant.CONFIG_DEV_ENVIRONMENT
        elif execution_env.lower() == constant.EXECUTION_ENVIRONMENT_TEST:
            GlobalData.exec_environment_config = constant.CONFIG_TEST_ENVIRONMENT
        elif execution_env.lower() == constant.EXECUTION_ENVIRONMENT_UAT:
            GlobalData.exec_environment_config = constant.CONFIG_UAT_ENVIRONMENT
        elif execution_env.lower() == constant.EXECUTION_ENVIRONMENT_PROD:
            GlobalData.exec_environment_config = constant.CONFIG_PROD_ENVIRONMENT
        elif execution_env.lower() == constant.EXECUTION_ENVIRONMENT_INT:
            GlobalData.exec_environment_config = constant.CONFIG_INT_ENVIRONMENT
    except Exception as e:
            print("Exception in set Execution Environment: {}".format(e))
    
if __name__ == '__main__':
    """
    Getting host ip and port no from configuration file.
    """
    set_execution_environment()
    host_name = cfg.get_environment_config(constant.CONFIG_ENVIRONMENT_SERVER_IP)
    port_no = cfg.get_environment_config(constant.CONFIG_ENVIRONMENT_SERVER_PORT)
    app.run(host=host_name, port=port_no)
