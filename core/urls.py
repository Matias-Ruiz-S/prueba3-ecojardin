from django.urls import path
from .views import home, macetero
from .views import contacto
from .views import flores
from .views import macetero
from .views import tierradehoja
from .views import flo001, flo002, flo003, flo004, mac001, mac002, mac003, mac004, tie001, tie002, tie003, tie004

urlpatterns = [
    path('', home,name="home"),
    path('contacto', contacto,name="contacto"),
    path('flores', flores,name="flores"),
    path('maceteros', macetero,name="macetero"),
    path('tierradehoja', tierradehoja,name="tierradehoja"),
    path('flores/001', flo001,name="flo001"),
    path('flores/002', flo002,name="flo002"),
    path('flores/003', flo003,name="flo003"),
    path('flores/004', flo004,name="flo004"),
    path('maceteros/001', mac001,name="mac001"),
    path('maceteros/002', mac002,name="mac002"),
    path('maceteros/003', mac003,name="mac003"),
    path('maceteros/004', mac004,name="mac004"),
    path('tierradehoja/001', tie001,name="tie001"),
    path('tierradehoja/002', tie002,name="tie002"),
    path('tierradehoja/003', tie003,name="tie003"),
    path('tierradehoja/004', tie004,name="tie004"),
]
