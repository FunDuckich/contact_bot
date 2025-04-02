from .first import r as first_router
from .category import r as category_router
from .advertisement import r as adv_router
from .mid import r as mid_router
from .tickets import r as tickets_router
from .other import r as other_router
from .last import r as last_router

__all__ = [
    "first_router",
    "category_router",
    "adv_router",
    "mid_router",
    "tickets_router",
    "other_router",
    "last_router"
]
