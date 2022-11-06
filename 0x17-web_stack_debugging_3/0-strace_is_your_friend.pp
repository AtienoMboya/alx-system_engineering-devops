# Fixes bad php extensions

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/ww/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
