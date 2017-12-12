[![Build Status](https://travis-ci.org/galaxyproject/ansible-galaxy-tools.svg?branch=master)](https://travis-ci.org/galaxyproject/ansible-galaxy-tools)

This Ansible role is for automated installation of tools from a Tool Shed into
Galaxy.

When run, this role will create an execution environment, install
[ephemeris](https://github.com/galaxyproject/ephemeris) and invoke the
shed-install command to install desired tools into Galaxy. The list of tools to
install is provided in `files/tool_list.yaml` file.

Usage
-----
To use the role, you need to create a playbook and include the role in it. A
sample playbook is available [here](https://github.com/afgane/galaxy-tools-playbook)
that will get you up and running in minutes.

Variables
---------
### Required variables ###
Only one of the two variables is requried (if both are set, the API key
takes precedence and a bootstrap user is not created):
- `galaxy_tools_api_key`: the Galaxy API key for an admin user on the target
  Galaxy instance (not required if the bootstrap user is being created)
- `galaxy_tools_admin_user_password`: a password for the Galaxy bootstrap user
  (required only if `galaxy_install_bootstrap_user` variable is set)

### Optional variables ###
See `defaults/main.yml` for the available variables and their defaults.

### Control flow variables ###
The following variables can be set to either `yes` or `no` to indicate if the
given part of the role should be executed:

 - `galaxy_tools_install_tools`: (default: `yes`) whether or not to run the
   tools installation script
 - `galaxy_tools_create_bootstrap_user`: (default: `no`) whether or not to
   create a bootstrap Galaxy admin user
 - `galaxy_tools_delete_bootstrap_user`: (default: `no`) whether or not to
   delete a bootstrap Galaxy admin user
