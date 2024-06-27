#change OS configuration to let holberton user login
#and open file without any error message

exec {'OS security config':
  command => 'sed -i "s/holberton/foo" /etc/security/limits/conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
