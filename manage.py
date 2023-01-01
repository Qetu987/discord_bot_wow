import sys
sys.path.insert(1, '/Users/ruslan/workspace/dis_bot')

from db_manager.drop_db import drop
from db_manager.show_db import show
from db_manager.create_db import create

def drop_db():
    drop()

def show_db():
    show()

def create_db():
    create()




f = globals().get(sys.argv[1])
if f:
    f()
else:
    print('No such method: %s' % sys.argv[1], end='\n\n')

    for func in dir():
        print(func) if func[0] != '_' and func != 'f' else None