# Fabric file
# http://docs.fabfile.org/en/2.4/getting-started.html
"""
Run as `fab deploy`

memo: full rsync command
EG
rsync -azvh -e ssh hacks magicrebirth@magicrebirth.webfactional.com:/home/magicrebirth/webapps/home2019/


"""

from fabric import Connection
from fabric import task

WEBFACTION = "magicrebirth@magicrebirth.webfactional.com:"

SOURCE_SYNC = "/Users/michele.pasin/Dropbox/code/django/research_portal_2019/researcher"
DEST_SYNC = "magicrebirth@magicrebirth.webfactional.com:/home/magicrebirth/webapps/home2019/"

MANAGEPY = 'manage.py'
PY = 'python3.7'


@task
def deploy(c):
    # delete pyc files and rsync remote server
    print("==LOCAL==")
    c.run('pwd')  # tip local commands used default c()
    c.run('find . -name ".pyc" -exec rm -rf {} \;')  # deletepyc_files
    print("-- RUNNING RSYNC...")
    c.run('rsync -azvh -e ssh {} {}'.format(SOURCE_SYNC, DEST_SYNC))

    print("\n==REMOTE==")
    c = Connection(WEBFACTION)
    with c.cd("~/webapps/home2019/researcher/src/"):
        c.run('pwd')
        print("-- RUNNING COLLECSTATIC...")
        c.run('{} {} collectstatic --noinput'.format(PY, MANAGEPY))
        print("-- TOUCH WSGI...")
        c.run('touch wsgi.py')
    # c.run('pwd')
