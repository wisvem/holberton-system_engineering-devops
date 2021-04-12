# apt-get update.
exec { 'update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell'
}
->

# Installs the haproxy package using apt.
package { 'haproxy':
  ensure   => present,
  name     => 'haproxy',
  provider => 'apt'
}
->

exec { 'Addd header':
  command  => 'sed -i "48 a \tadd_header X-Served-By \$HOSTNAME;" /etc/haproxy/haproxy.cfg',
  user     => 'root',
  provider => 'shell'
}

->
exec { 'Start haproxy':
  command  => 'service haproxy restart',
  user     => 'root',
  provider => 'shell'
}
