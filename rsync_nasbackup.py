import os, subprocess, time, shlex, time

synology_path_home = "/media/synology/home"
synology_path_shared = "/media/synology/shared"
dest_path = "/media/seagate"
log_path = "/home/vauyeung/rsync_logs"

#source_paths = [synology_path_home, synology_path_shared]
source_paths = [synology_path_home]
rsync = "rsync -avz --progress --delete --exclude '#recycle'" 

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
        print(f"{path} is not mounted, mounting now....")
        try:
            subprocess.check_call(["mount", path])
            print(f"SUCCESS, Mounted: {path}\n")
            return True
        except:
            print(f"FAILED to mount {path}")
            return False

def unmount(path):
    '''
    Tries to unmount and if it fails to do so, it will 
    print that it failed to unmount the path.
    '''
    try: 
        subprocess.check_call(["umount", "--verbose", path])
    except:
        print(f"FAILED: Could not unmount {path}")

def rsync_cmd(source, dest):
    '''
    Function takes in source path and destination path.
    Contructs the commandline Rsync by taking the current date
    concats with source and dest, logs as well with file name of source
    concatinating with backup.log
    '''
    named_tuple = time.localtime()        # Get struct_time
    time_string = time.strftime("%Y-%m-%d", named_tuple)
    source_string = source.split("/")         
    return (rsync + " " + source + " " + dest + " --log-file="+ log_path + "/" + time_string + "_" + source_string[-2] + "_" + source_string[-1] + "-backup.log") 

if __name__ == '__main__':

    # variables
    mounted_paths = []                                                # Keep track of mounted paths 

    print("Paths to be backed up:")
    for source_path in source_paths:
        print(source_path)
    print("-"*30)

    # Check if dest path is mounted
    if check_mount(dest_path):
        mounted_paths.append(dest_path)
        for source_path in source_paths:                                            # Loop through multiple source paths
            is_mounted = check_mount(source_path)
            if is_mounted:                                                          # Mount source path
                mounted_paths.append(source_path)                                   # Add to mounted list
                print(f"Rsync {source_path} to {dest_path}")          
                subprocess.call(shlex.split(rsync_cmd(source_path, dest_path)))     # Run rsync
        time.sleep(10)
    else:
        # Cannot mount source, exit
        print("Source not mounted, exiting.")
        exit()
    
    print("-"*30)
    print("Cleaning up...")
    print("-"*30)
    
    # Unmount all paths that are previously mounted
    for mounted_path in mounted_paths:
        unmount(mounted_path)
    