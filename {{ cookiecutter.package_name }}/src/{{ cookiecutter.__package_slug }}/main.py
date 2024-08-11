import logging

log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(
        level="DEBUG",
        format="%(levelname)s | [%(asctime)s] | [logger:%(name)s] | [%(module)s.%(funcName):%(lineno)s] |> %(message)s",
        datefmt="%Y-%m-%d_%H:%M:%S",
    )

    log.info("App start")