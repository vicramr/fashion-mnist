"""
This is the driver script for an initial experiment.
"""

if __name__ == "__main__":
    import initialize
    initialize.initialize()

    import neptune

    from src import utils
    from src import constants

    neptune.init(constants.neptune_project_qualified_name)
    # Docs for create_experiment: https://neptune-client.readthedocs.io/en/latest/technical_reference/project.html#neptune.projects.Project.create_experiment
    with neptune.create_experiment(name="Insert experiment name here", description="Insert description here", upload_source_files=utils.get_source_files()) as npt_exp:
        pass
