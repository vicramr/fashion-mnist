# No shebang line; this file is only meant to be sourced, not executed as a child process.

# Next we need to set the API key environment variables. There are definitely some
# security vulnerabilities associated with doing this - primarily, we should be worried that 
# the session's environment may be visible to other processes or somehow recorded.
# Still, it is a convenient way to set up our credentials while ensuring that they will not
# be accidentally committed to Github.
#
# The main precaution I want to take is to ensure that the credentials are never logged
# in .bash_history or anything like that. This means we will have to PHYSICALLY COPY AND PASTE
# the credentials every time we run this script. That seems acceptable to me.

# Neptune API token info is here: https://neptune-client.readthedocs.io/en/latest/tutorials/get-started.html#copy-api-token
echo "[setup.sh] Please enter the Neptune API token."
read -s neptune_api_token
export NEPTUNE_API_TOKEN="$neptune_api_token"

# Because this script is being sourced, when we activate the environment the changes will be seen from the parent shell.
conda activate fashionmnist || source activate fashionmnist
