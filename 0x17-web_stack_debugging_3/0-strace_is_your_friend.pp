# Manifest to configure an Ubuntu server with nginx
exec { 'fix type error':
  command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  user     => 'root',
  provider => 'shell'
}
