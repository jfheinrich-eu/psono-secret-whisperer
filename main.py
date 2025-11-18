import os
import subprocess

# Set the output value by writing to the outputs in the Environment File,
# mimicking the behavior defined here:
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter


def set_github_action_output(output_name: str, output_value: str) -> None:
    with open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a") as f:
        f.write(f"{output_name}={output_value}\n")


def main():
    secret_type: str = os.environ["INPUT_SECRET_TYPE"]
    mask_secrets: list[str] = os.environ["INPUT_MASK_SECRETS"].split(",")
    custom_field_names: list[str] = \
        os.environ["INPUT_CUSTOM_FIELD_NAMES"].split(",")
    cmd: list[str] = []
    psono_env: dict[str, str] = {}
    psono_env["PSONO_CI_API_KEY_ID"] = os.environ["INPUT_CI_API_KEY_ID"]
    psono_env["PSONO_CI_API_SECRET_KEY_HEX"] = \
        os.environ["INPUT_CI_API_SECRET_KEY_HEX"]
    psono_env["PSONO_CI_SERVER_URL"] = os.environ["INPUT_CI_SERVER_URL"]

    if os.environ.get("CI") is not None:
        cmd.append("/app/psonoci")
    elif os.environ.get("PSONOCI_PATH") is not None:
        cmd.append(os.environ["PSONOCI_PATH"])
    else:
        cmd.append("psonoci")

    if secret_type == "secret":
        cmd.append("secret")
        cmd.append("get")
    elif secret_type == "env":
        cmd.append("env-vars")
        cmd.append("get-or-create")
    else:
        print("Unknown SECRET_TYPE: " + secret_type)
        exit(1)

    cmd.append(os.environ["INPUT_SECRET_ID"])

    count = 0
    for field in os.environ["INPUT_SECRET_FIELDS"].split(","):
        count += 1
        if count > 10:
            print("To much fields, only ten fields allowed")
            exit(100)

        cmdval = cmd.copy()
        cmdval.append(field)
        try:
            secret = subprocess.run(
                cmdval, capture_output=True, text=True, check=True,
                env=psono_env
            )
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            exit(2)
        except FileNotFoundError:
            print("Error: Command psonoci not found")
            exit(3)

        if field in mask_secrets:
            print(f"::add-mask::{secret.stdout}\n")

        if (len(custom_field_names) >= count and
                custom_field_names[count - 1].strip() != ""):
            set_github_action_output(
                custom_field_names[count - 1].strip(), secret.stdout
            )
        else:
            set_github_action_output(f"secret{count}", secret.stdout)


if __name__ == "__main__":
    main()
