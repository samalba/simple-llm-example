# Simple LLM example with Dagger

This is a simple example of using Dagger with an LLM and tools.

**Prerequisites**: [This README assumes you have gone through the Dagger quickstart to build an agent](https://docs.dagger.io/quickstart/agent)

In a nutshell, the example shows how to use a simple Dagger module that interacts with an LLM. Tools are in a submodule called `toolbox`.

The `toolbox` was installed in the main module using (no need to do this if you're using the example as-is):

```bash
dagger install ./toolbox
```

This makes the toolbox code available to the `dag.env()` from the main module:

```python
dag.env().with_toolbox_input("tools", dag.toolbox(), "the tools to use")
```

Note: this allows to instantiate the toolbox several times, for example if you're using different api keys, or different scopes for your tools.
