import os
import subprocess

# Set the output value by writing to the outputs in the Environment File,
# mimicking the behavior defined here:
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter


def set_github_action_output(output_name, output_value):
    # f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    # f.write(f'{output_name}={output_value}\n')
    # f.close()
    print(f"::set-output name={output_name}::{output_value}\n")


def main():
    secret_type = os.environ["INPUT_SECRET_TYPE"]
    mask_secrets = os.environ["INPUT_MASK_SECRETS"].split(",")
    cmd = []
    psono_env = {}
    psono_env["PSONO_CI_API_KEY_ID"] = os.environ["INPUT_CI_API_KEY_ID"]
    psono_env["PSONO_CI_API_SECRET_KEY_HEX"] = \
        os.environ["INPUT_CI_API_SECRET_KEY_HEX"]
    psono_env["PSONO_CI_SERVER_URL"] = os.environ["INPUT_CI_SERVER_URL"]

    if os.environ.get('CI') is not None:
        cmd.append("/app/psonoci")
    elif os.environ.get('PSONOCI_PATH') is not None:
        cmd.append(os.environ['PSONOCI_PATH'])
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

    for field in os.environ["INPUT_SECRET_FIELDS"].split(","):
        cmdval = cmd.copy()
        cmdval.append(field)
        try:
            secret = subprocess.run(cmdval,
                                    capture_output=True,
                                    text=True,
                                    check=True,
                                    env=psono_env)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            exit(2)
        except FileNotFoundError:
            print(f"Error: Command '{cmdval[0]}' not found")
            exit(3)

        if field in mask_secrets:
            print(f'::add-mask::{secret.stdout}\n')

        set_github_action_output(field, secret.stdout)


if __name__ == "__main__":
    main()
