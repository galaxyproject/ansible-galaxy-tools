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
- `galaxy_tools_api_key`: the Galaxy API key for an admin user on the target Galaxy instance

### Optional variables ###
- `galaxy_tools_instance_url`: (default `127.0.0.1:8080`) a URL or an IP address for
  the Galaxy instance where the tools are to be installed
- `galaxy_tools_tool_list_file`: (default `files/tool_list.yaml`) the file
  containing all the tools to be installed
- `galaxy_tools_base_dir`: (default: `/tmp`) the system path from where this role will be run

### Control flow variables ###
The following variables can be set to either `yes` or `no` to indicate if the
given part of the role should be executed:

 - `galaxy_tools_install_tools`: (default: `yes`) whether or not to run the
   tools installation script

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
default, it will be places in `/tmp` dir. The log file with the tool execution
progress is available in `/tmp/galaxy_tool_install.log`.
