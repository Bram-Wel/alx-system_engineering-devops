# Correct misspelling on /var/www/html/wp-settings.php line 137

include stdlib

file_line {'/var/www/html/wp-settings.php':
  ensure => present,
  path   => '/var/www/html/wp-settings.php',
  line   => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match  => '^require_once\( ABSPATH \. WPINC \. \'\/class-wp-locale\.phpp\' \);$',
}
