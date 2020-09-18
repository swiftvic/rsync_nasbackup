import os, subprocess, time, shlex

synology_path_home = "/media/synology/home"
synology_path_shared = "/media/synology/shared"
dest_path = "/media/seagate"

source_paths = [synology_path_home, synology_path_shared]
rsync = "rsync -avz --progress --delete --exclude '#recycle'"
#rsync_cmd = f"rsync -avz --progress --delete --exclude '#recycle' {source_paths} {dest_path}" 

for source_path in source_paths:
    print(source_path)
    
def check_mount(path):
    '''
    Function checks mounts and if the path is not mounted it will attempt to mount it.
    Will return True if mounted. False if not.
    '''
    print(f"Checking if '{path}'' is mounted.")
    if os.path.ismount(path):
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

def rsync_cmd(source, dest):
    return (rsync + " " + source + " " + dest)

if __name__ == '__main__':
    # Check if dest path is mounted
    if check_mount(dest_path):
        for source_path in source_paths:
            is_mounted = check_mount(source_path)
            if is_mounted:
                # add to list

        time.sleep(10)
    else:
        # Cannout mount source, exit
        print("Source not mounted, exiting.")
        exit()
    
    unmount(dest_path)
    