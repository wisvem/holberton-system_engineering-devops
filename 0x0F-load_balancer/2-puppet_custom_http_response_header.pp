# apt-get update.
exec { 'update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell'
}
->

# Installs the nginx package using apt.
package { 'haproxy':
  ensure   => present,
  name     => 'haproxy',
  provider => 'apt'
}
->
$my_string="\nfrontend haproxynode\n\tbind *:80\n\tmode http\n\t\
default_backend backendnodes\n\nbackend backendnodes\n\t\
balance roundrobin\n\tserver  ws01   104.196.30.252:80 check\n\t\
server  ws02   35.185.6.249:80 check"
$my_file='/etc/haproxy/haproxy.cfg'
exec { 'Set default /404':
  command  => 'echo -e "$my_string" >>"$FILE"',
  user     => 'root',
  provider => 'shell'
}

->
exec { 'Start haproxy':
  command  => 'service haproxy restart',
  user     => 'root',
  provider => 'shell'
}
