from mypackage.service import Service, MySVC
import mypackage
print(mypackage.__file__)

service = Service()
service.pack("model", MySVC())  # MySVC could be loaded from a checkpoint instead
service.save()
