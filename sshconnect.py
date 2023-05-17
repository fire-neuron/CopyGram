ssh = None

def open_session(**kargs):
    global ssh,frame
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(kargs['host'], username=kargs['username'], password=kargs['password'])
    return ssh




