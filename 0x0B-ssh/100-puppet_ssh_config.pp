# Adds configurations to ssh config files

$str = "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n"
file { '/home/vagrant/.ssh/config':
  ensure  => file,
  content => $str,
}
