# Executes a kill command

exec {'pkill -f killmenow':
  path   => '/usr/bin/:/usr/sbin/:/bin/',
  onlyif => 'pgrep killmenow',
}
