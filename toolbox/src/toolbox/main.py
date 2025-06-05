import dagger
from dagger import dag, function, object_type


@object_type
class Toolbox:
    @function
    def tool1(self) -> str:
        return "tool1"

    @function
    def tool2(self) -> str:
        return "tool2"
