import os
import subprocess

# Set the output value by writing to the outputs in the Environment File,
# mimicking the behavior defined here:
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter


def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()


def main():
    secret_type = os.environ["INPUT_SECRET_TYPE"]
    mask_secrets = os.environ["INPUT_MASK_SECRETS"].split(",")
    cmd = []
    psono_env = {}
    psono_env["PSONO_CI_API_KEY_ID"] = os.environ["INPUT_CI_API_KEY_ID"]
    psono_env["PSONO_CI_API_SECRET_KEY_HEX"] = \
        os.environ["INPUT_CI_API_SECRET_KEY_HEX"]
    psono_env["PSONO__CI_SERVER_URL"] = os.environ["INPUT_CI_SERVER_URL"]

    cmd.append("/app/psonoci")

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
        secret = subprocess.run(cmdval,
                                capture_output=True,
                                text=True,
                                env=psono_env)

        if field in mask_secrets:
            print(f'::add-mask::{secret}')

        set_github_action_output(field, secret)


if __name__ == "__main__":
    main()
