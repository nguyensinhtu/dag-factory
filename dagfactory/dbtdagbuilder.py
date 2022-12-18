from dbt.cli import main
from airflow import DAG
from typing import Union, Dict, Any
from copy import deepcopy
import os
from click import Command
from utils import call_click_command


class DbtDagBuilder:
    def ___init__(
        self,
        config_path: os.PathLike,
        dag_name: str,
        dag_config: Dict[str, Any],
        defautl_conf: Dict[str, Any],
        compile_if_not_exist=False,
    ):
        self.dag_name: str = dag_name
        self.dag_config: Dict[str, Any] = deepcopy(dag_config)
        self.default_config: Dict[str, Any] = deepcopy(defautl_conf)
        self.root_path: os.PathLike = config_path
        self.should_compile_manifest = compile_if_not_exist

    @staticmethod
    def compile(product_dir: os.PathLike):
        pass

    def build(self) -> Dict[str, Union[str, DAG]]:
        pass


if __name__ == "__main__":
    call_click_command(main.compile)  
    # main.compile(project_dir="/Users/tu.nguyen12/Projects/dag-factory/examples/dbt")
