import argparse
from aappmart.core.orchestrator import AAPP_MART
from aappmart.utils.logger import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(
        description="AAPP-MART Autonomous Red Team Framework"
    )
    parser.add_argument("--target", required=True)
    parser.add_argument(
        "--mode",
        default="full",
        choices=["full", "recon", "simulation", "predict"]
    )
    parser.add_argument(
        "--profile",
        default="default",
        help="Execution profile (future use)"
    )

    args = parser.parse_args()

    engine = AAPP_MART(
        target=args.target,
        mode=args.mode,
        profile=args.profile
    )

    engine.run()
    print(engine.get_report())

if __name__ == "__main__":
    main()
