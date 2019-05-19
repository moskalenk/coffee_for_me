from pathlib import PurePath

project_path_dir = str(PurePath(__file__).parent)
db_path_dir = str(PurePath(project_path_dir, "db"))
