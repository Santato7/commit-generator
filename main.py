import os
import subprocess

os.mkdir("fake_dir")
os.chdir("fake_dir")
subprocess.run("git init --quiet", shell=True, check=True)
subprocess.run("echo 'fake file' > fake_file.txt", shell=True, check=True)
subprocess.run("git add fake_file.txt", shell=True, check=True)
subprocess.run(
    "git commit --quiet --date='1970-01-01 00:00:00' -m 'fake commit'",
    shell=True,
    check=True,
)
