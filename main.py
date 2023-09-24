import os
from packet import to_pickle, to_csv, to_json

path_dir = os.getcwd()
to_pickle(path_dir)
to_json(path_dir)
to_csv(path_dir)
