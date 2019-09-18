"""
This is the driver script for an initial experiment.
"""

import main
import utils
import neptune
import constants

if __name__ == "__main__":
    main.main()

    neptune.init(constants.neptune_project_qualified_name)
    # Docs for create_experiment: https://neptune-client.readthedocs.io/en/latest/technical_reference/project.html#neptune.projects.Project.create_experiment
    with neptune.create_experiment(name="Insert experiment name here", description="Insert description here", upload_source_files=utils.get_src_files()) as npt_exp:
        pass
