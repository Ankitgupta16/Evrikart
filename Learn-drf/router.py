from store.viewsets import UrstoreViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Urstore', UrstoreViewset)

# localhost:
# GET, POST, PUT, DELETE
# list , retrive
