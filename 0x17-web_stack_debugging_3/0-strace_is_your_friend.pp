# Correct misspelling on /var/www/html/wp-settings.php line 137

exec { 'fix-typo':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
