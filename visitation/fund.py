
#TODO(PMM) marker interfaces?

import organisation

Organisation = organisation.Organisation

class Fund(object):


    def data(self):
        return {}

    """ returns the children on the container """

    def items(self):
        return [Organisation(), Organisation()]


