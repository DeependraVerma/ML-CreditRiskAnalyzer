import os
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/exception/exception.py",
    f"{project_name}/logger/logging.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/pipeline/training_pipeline.py",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    f".github/workflows/.gitkeep",
    f"test/__init__.py",
    f"test/unit/__init__.py",
    f"test/unit/test_unit.py",
    f"test/integration/__init__.py",
    f"test/integration/test_int.py",
    "experiment/experiment.ipynb",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    "setup.cfg",
    "init_setup.sh",
    "tox.ini",
    "pyproject.toml"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"File directory {filedir} created for the file {filename}")
    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
        logging.info(f"The file {filename} is created for {filedir}")
    else:
        logging.info(f"File with name {filename} already exist")