import os, subprocess, time

synology_path_home = "/media/synology/home"
synology_path_shared = "/media/synology/shared"
seagate_path = "/media/seagate"

paths =[synology_path_home, synology_path_shared, seagate_path]

for path in paths:
    print(path)
    
def check_mounts(path):
    '''
    Function checks mounts and if the path is not mounted it will attempt to mount it.
    Will return True if mounted. False if not.
    '''
    print("Checking if Synology paths are mounted.")
    if os.path.ismount(path):
        # rsync
        print(f"{path} is already mounted.")
        return True
    else:
        print(f"{path} not mounted, mounting now..")
        try:
            subprocess.check_call(["mount", path])
            print(f"Mounted: {path}")
            return True
        except:
            print(f"Failed to mount {path}")
            return False

def unmount(path):
    try: 
        subprocess.check_call(["umount", "--verbose", path])
    except:
        print("Could not unmount")

if __name__ == '__main__':
    is_mounted = check_mounts(synology_path_home)
    if is_mounted:
        time.sleep(10)
    
    unmount(synology_path_home)
    