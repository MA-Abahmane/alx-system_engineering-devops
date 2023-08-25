# Puppet Cheat Sheet

Puppet is a configuration management tool used for automating the provisioning and management of servers and infrastructure. This cheat sheet provides a quick reference for some commonly used Puppet commands and concepts.

## Puppet Basics

- **Resource Declaration:**
  ```puppet
  resource_type { 'title':
    attribute => value,
    # Additional attributes
  }
Save to grepper


# Attributes

file { 'resource title':
  path                    =>  (namevar) The path to the file to manage.  Must be fully...
  ensure                  =>  Whether the file should exist, and if so what...
  backup                  =>  Whether (and how) file content should be backed...
  checksum                =>  The checksum type to use when determining...
  checksum_value          =>  The checksum of the source contents. Only md5...
  content                 =>  The desired contents of a file, as a string...
  ctime                   =>  A read-only state to check the file ctime. On...
  force                   =>  Perform the file operation even if it will...
  group                   =>  Which group should own the file.  Argument can...
  ignore                  =>  A parameter which omits action on files matching 
  links                   =>  How to handle links during file actions.  During 
  mode                    =>  The desired permissions mode for the file, in...
  mtime                   =>  A read-only state to check the file mtime. On...
  owner                   =>  The user to whom the file should belong....
  provider                =>  The specific backend to use for this `file...
  purge                   =>  Whether unmanaged files should be purged. This...
  recurse                 =>  Whether to recursively manage the _contents_ of...
  recurselimit            =>  How far Puppet should descend into...
  replace                 =>  Whether to replace a file or symlink that...
  selinux_ignore_defaults =>  If this is set then Puppet will not ask SELinux...
  selrange                =>  What the SELinux range component of the context...
  selrole                 =>  What the SELinux role component of the context...
  seltype                 =>  What the SELinux type component of the context...
  seluser                 =>  What the SELinux user component of the context...
  show_diff               =>  Whether to display differences when the file...
  source                  =>  A source file, which will be copied into place...
  source_permissions      =>  Whether (and how) Puppet should copy owner...
  sourceselect            =>  Whether to copy all valid sources, or just the...
  target                  =>  The target for creating a link.  Currently...
  type                    =>  A read-only state to check the file...
  validate_cmd            =>  A command for validating the file's syntax...
  validate_replacement    =>  The replacement string in a `validate_cmd` that...

   ...plus any applicable metaparameters.
}



# Applying Manifests:

Apply Puppet manifest to the local system:

puppet apply manifest.pp


# Puppet Config Files:

Main configuration file: /etc/puppetlabs/puppet/puppet.conf
Module path: /etc/puppetlabs/code/environments/<environment>/modules
Puppet Commands
Agent Related:


# Start Puppet agent run:

puppet agent -t
Test Puppet agent run (no changes made):

puppet agent --test --noop


# Server Related:

Trigger Puppet server compilation:


puppetserver ca generate --certname <CERTNAME>



# Module Related:

Generate a new Puppet module:


puppet module generate <MODULE_NAME>


# Certificate Related:

List certificates waiting for approval:


puppetserver ca list


# Sign a certificate request:


puppetserver ca sign --certname <CERTNAME>
Puppet Resources
Common Resource Types:
package: Manage software packages.
file: Manage files and directories.
service: Manage system services.
user: Manage users and groups.
group: Manage groups.
Puppet Language Basics
Variables:


# Assign a variable:


$variable_name = value
Use a variable:
puppet

$message = "Hello, Puppet!"
notify { $message: }


# Conditionals:


if condition {
  # Code to execute if condition is true
} elsif another_condition {
  # Code to execute if another_condition is true
} else {
  # Code to execute if no conditions are true
}


# Iterations (Each):

each $item in $array {
  # Code to execute for each item
}
Puppet Forge
Puppet Forge: https://forge.puppet.com
Explore pre-built Puppet modules for various tasks.
Helpful Links
Puppet Documentation
Puppet Style Guide
