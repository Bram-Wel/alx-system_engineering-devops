# Install & Configures Nginx with redirection using puppet

exec { 'apt update && apt upgrade':
  path    => '/usr/bin:/bin',
  command => 'sudo apt update && sudo apt upgrade -y',
  returns => [0,1],
}

package { 'nginx':
  ensure  => installed,
}

file_line { 'redirect':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'rewrite ^/reirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
