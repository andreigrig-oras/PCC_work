import make_tshirt
make_tshirt.make_tshirt(size='M', message='hi1')

from make_tshirt import make_tshirt
make_tshirt(message='hi2') 

from make_tshirt import make_tshirt as fn
fn(message='hi3') 

import make_tshirt as mn
mn.make_tshirt(message='hi4')

from make_tshirt import *
make_tshirt(message='hi5')