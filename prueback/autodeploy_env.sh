# Env vars to determine what steps to run in autodeploy yeh

# Build an image with the new django only, not the python packages
export IMAGE_DJANGO=true

# Also build the python packages
export IMAGE_PIP=true

# Run the migrate command.
export MIGRATIONS=true


# Load the fixtures
export LOADDATA=true

# Add a new cronjob
export CRONJOB=false
