# Config file
exec { 'update':
    command => 'sudo /usr/bin/apt-get update -y'
}
exec { 'install-nginx':
    command => 'sudo /usr/bin/apt-get install -y'
}
exec { 'echo-holb':
    command => 'sudo /bin/echo Holberton School > /var/www/html/index.nginx-debian.html'
}
exec { 'echo-404':
    command => 'sudo /bin/echo Ceci n\'est pas une page > /var/www/html/404.html'
}
$my_string = "\\\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n"
$myfile = '/etc/nginx/sites-available/default'
$error404="\\\n\terror_page 404 /404.html;\n\tlocation /404.html {\n\t\tinternal;\n\t}\n";

file_line {'redirect':
    match   => $my_string,
    path    => $myfile,
    line    => $my_string,
    replace => false
}

file_line {'redirect':
    match   => $error404,
    path    => $myfile,
    line    => $error404,
    replace => false
}

exec { 'Start-nginx':
    command => 'sudo service /usr/sbin/nginx start'
}
