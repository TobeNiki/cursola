from typing import Any
import sys

class _const:
    
    class ConstError(TypeError):
        pass

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s) " % __name)
        self.__dict__[__name] = __value

sys.modules[__name__] = _const()

