import logging

from app.config import get_settings


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
    )


def main() -> None:
    settings = get_settings()
    configure_logging(settings.log_level)

    logger = logging.getLogger(__name__)
    logger.info(
        "Starting application | environment=%s | symbol=%s | timeframe=%s",
        settings.environment,
        settings.default_symbol,
        settings.default_timeframe,
    )


if __name__ == "__main__":
    main()
