#change configuration to let holberton user login
#and open file without any error message

exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
}
