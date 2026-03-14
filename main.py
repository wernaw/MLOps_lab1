import os
import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml as pyyaml


def export_envs(environment: str = "dev", secrets: str = "secrets.yaml") -> None:
    env_file = f"config/.env.{environment}"
    load_dotenv(env_file)

    # Load secrets from YAML file
    if os.path.exists(secrets):
        with open(secrets, "r") as file:
            secrets_data = pyyaml.safe_load(file)
            for key, value in secrets_data.items():
                os.environ[key] = str(value)
    else:
        print(f"Warning: Secrets file {secrets} does not exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("SECRET_KEY: ", settings.SECRET_KEY)
