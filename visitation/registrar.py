
import registry
import fund
import organisation

Registry = registry.Registry
Fund = fund.Fund
Organisation = organisation.Organisation

from registry import Registry

__r = Registry()
__r.add('Fund', Fund, ())
__r.add('Organisation', Organisation, ())


