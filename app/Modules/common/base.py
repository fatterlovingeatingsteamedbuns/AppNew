import os, json,sys
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])
from common.env_config import EnvList
from common.parameters_config import ParametersConfig

# import nautcore.telemetry.metric.utilities.test_result_metric as utilities


def retrive_data():
    if ParametersConfig.is_local == True:
        ## Local debug mode
        dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_file_path = os.path.join(dir, 'data.json')
        
    else:
        if not os.path.exists(os.environ.get('DATA_PATH')):
            raise Exception("The path of saving data doesn't exist")
        data_file_path = os.environ.get('DATA_PATH') + "data.json"

    try:
        with open(data_file_path, 'r') as f:
            #从json文件中读取数据
            dataset = json.load(f)
            return dataset
    except:
        raise Exception(f"Error opening the file with path {data_file_path}")


def get_test_result_metric(env):
    test_result = None
    try:
        if env == EnvList.SH:
            workflow_name = 'mem-uxbvt-sh'
        elif env == EnvList.PPE:
            workflow_name = 'mem-uxbvt-ppe'
        elif env == EnvList.PE:
            workflow_name = 'mem-uxbvt-pe'
        elif env == EnvList.GCB:
            workflow_name = 'mem-uxbvt-gcb'
        elif env == EnvList.GCP:
            workflow_name = 'mem-uxbvt-gcp'
        elif env == EnvList.GHB:
            workflow_name = 'mem-uxbvt-ghb'
        elif env == EnvList.GCP:
            workflow_name = 'mem-uxbvt-ghp'
        elif env == EnvList.INT:
            workflow_name = 'mem-uxbvt-int'
        else:
            workflow_name = ''
        workflow_id = os.environ.get('WORKFLOW_ID')
        # test_context = utilities.TestContext(
        #     workflowId=workflow_id, workflowName=workflow_name
        # )
        # test_result = utilities.TestResult(testContext=test_context)
        return test_result
    except Exception:
        return None



# dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(dir)