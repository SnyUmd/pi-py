from subprocess import check_output
out = check_output(["ls", "-l"]).decode('utf-8')
print(out)

#import subprocess

#def res_cmd(cmd):
#  return subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0].decode('utf-8')

#def main():
#  cmd = ("ls -l")
#  print(res_cmd(cmd))

#if __name__ == '__main__':
#  main()