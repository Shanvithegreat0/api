import os
import glob

apps = ['users', 'contacts']
base_dir = os.path.dirname(os.path.abspath(__file__))

for app in apps:
    migration_dir = os.path.join(base_dir, app, 'migrations')
    migration_files = glob.glob(os.path.join(migration_dir, '[!__init__]*.py'))
    
    for file in migration_files:
        os.remove(file)
        print(f"Deleted: {file}")

    pycache_dir = os.path.join(migration_dir, '__pycache__')
    if os.path.exists(pycache_dir):
        pycache_files = glob.glob(os.path.join(pycache_dir, '*'))
        for file in pycache_files:
            os.remove(file)
            print(f"Deleted: {file}")

        os.rmdir(pycache_dir)
        print(f"Deleted: {pycache_dir}")

print("Migration files deleted successfully.")
