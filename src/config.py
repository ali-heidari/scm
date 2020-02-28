import subprocess


def main():
    cmd = ['yum','list', 'installed', 'curl']
    cmd = ['ls','-la']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    o, e = proc.communicate()

    print('Output: ' + o.decode('ascii'))
    print('Error: '  + e.decode('ascii'))
    print('code: ' + str(proc.returncode))


if __name__ == "__main__":
    main()