from typing import List
from itertools import count

from app.schema import UserOut

users: List[UserOut] = []
id_generator = count(1)
