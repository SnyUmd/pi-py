from subprocess import check_output

val = check_output(["ps", "-a"]).decode('utf-8')
print(val);
