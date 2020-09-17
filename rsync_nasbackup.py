import os, subprocess, time

synologypathhome = "/media/synology/home"
synologypathshared = "/media/synology/shared"
seagatepath = "/media/seagate"

paths =[synologypathhome, synologypathshared, seagatepath]

for path in paths:
    print(path)
    
print("Checking if Synology paths are mounted.")
if os.path.ismount(synologypathhome):
    # rsync
    print("mounted")
    pass
else:
    print(f"{synologypathhome} not mounted, mounting now..")
    subprocess.check_call(["mount", synologypathhome])
    print(f"Mounted: {synologypathhome}")
    time.sleep(10)

# cleanup
try: 
    subprocess.check_call(["umount", "--verbose", synologypathhome])
except:
    print("Could not unmount")