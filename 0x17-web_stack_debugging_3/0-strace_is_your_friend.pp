# Manifest to configure an Ubuntu server with nginx
file_line { 'Check if file exist':
  ensure => present,
  path   => '/var/www/html/wp-settings.php',
}
->
exec { 'fix type error':
  command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  user     => 'root',
  provider => 'shell'
}
