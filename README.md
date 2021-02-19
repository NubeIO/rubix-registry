# Rubix Registry

Rubix Registry is a package which helps to centralizing some settings global to the Apps. Currently we are storing 
wires-plat details.

### How to install

```bash
poetry add git+https://github.com/NubeIO/rubix-registry@master
```

### How to delete

```bash
poetry remove rubix-registry
```

### How to integrate

```python
from registry.registry import RubixRegistry

RubixRegistry().store_wires_plat({"client_id": ""})
RubixRegistry().read_wires_plat()
```
