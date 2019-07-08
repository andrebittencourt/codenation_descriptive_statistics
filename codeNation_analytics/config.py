from os import path

import codeNation_analytics

base_path = path.dirname(path.dirname(codeNation_analytics.__file__))
workspace_path = path.join(base_path, 'workspace')
data_path = path.join(workspace_path, 'data')
models_path = path.join(workspace_path, 'models')
