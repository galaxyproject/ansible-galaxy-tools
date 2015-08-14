This Ansible role is for automated installation of tools from a Tool Shed into
Galaxy.

When run, this role will create an execution environment on one system and then
invoke the tool installation script that will target a Galaxy instance on
potentially another system. Target hosts are set via variables (see below).

Requirements
------------
None

Dependencies
------------
None

Role variables
--------------
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

Example playbook
----------------
To use the role, create a playbook like the one below. Set any variables
(remember, `galaxy_tools_api_key` is required) and save the playbook as
`tools.yml`. This playbook assumes the role has been placed into `roles/tools`
directory:

    - hosts: localhost
      connection: local
      vars:
          galaxy_tools_instance_url: http://54.158.48.0/
          galaxy_tools_api_key: d0ca91a20a67ec0d48612ac920ebdf59
      roles:
          - tools

Finally, run the playbook with:

    $ ansible-playbook tools.yml -i hosts

Note that a virtualenv will be created as part of the script execution. By
default, it will be placed in `/tmp` dir. The log file with the tool execution
progress is available in `/tmp/galaxy_tool_install.log`.
