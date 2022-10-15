# Adds configurations to ssh config files

exec { 'echo':
  path    => '/usr/bin:/usr/sbin',
  command => 'echo "\nHost *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n" >> /etc/ssh/ssh_config',
}
