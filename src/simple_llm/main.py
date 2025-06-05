import dagger
from dagger import dag, function, object_type
from dagger.client.gen import Toolbox


@object_type
class SimpleLlm:

    @function
    def simple_ask(
        self,
        assignment: str,
    ) -> str:
        """Query an LLM with a simple assignment"""
        environment = (
            dag.env()
            .with_toolbox_input("tools", dag.toolbox(), "the tools to use")
            .with_string_output("response", "the response from the LLM")
        )

        work = (
            dag.llm()
            .with_env(environment)
            .with_prompt(assignment)
        )

        return work.env().output("response").as_string()
