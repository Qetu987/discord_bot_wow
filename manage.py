import sys
sys.path.insert(1, '/Users/ruslan/workspace/dis_bot')

from db_manager.drop_db import drop as drop_db
from db_manager.show_db import show as show_db
from db_manager.create_db import create as create_db

f = globals().get(sys.argv[1])
if f:
    f()
else:
    print('No such method: %s' % sys.argv[1], end='\n\n')

    for func in dir():
        print(func) if func[0] != '_' and func != 'f' and func != 'sys' else None