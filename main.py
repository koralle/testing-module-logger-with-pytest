from src.lib_with_module_logger import add as module_add
from src.lib_with_root_logger import add as root_add
from src.loggers import create_module_logger

if __name__ == "__main__":
    root_add(a=4, b=5)
    module_add(a=4, b=5, logger=create_module_logger("MODULE_ADD (PROPAGATE=False)"))
    module_add(
        a=4,
        b=5,
        logger=create_module_logger(
            "MODULE_ADD (PROPAGATE=True)", logging_propagate=True
        ),
    )
