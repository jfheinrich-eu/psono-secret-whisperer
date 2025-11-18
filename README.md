<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://jfheinrich.eu/storage/assets/psono-secret-whisperer.png" alt="Project logo"></a>
</p>

<h3 align="center">PSONO Secret Whisperer</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![Maintainer](https://img.shields.io/badge/maintainer-@jfheinrich-blue)
[![GitHub Issues](https://img.shields.io/github/issues/jfheinrich-eu/psono-secret-whisperer.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/jfheinrich-eu/psono-secret-whisperer.svg)](https://GitHub.com/Naereen/StrapDown.js/pull/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A GitHub Action for securely retrieving secrets from PSONO server.
    <br>
</p>




## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about)
- [🎈 Usage ](#-usage)
- [➡️ Inputs ](#️-inputs)
- [⬅️ Outputs ](#️-outputs)
- [🛡️ Security Recommendations ](#️-security-recommendations)
- [‼️ Requirements ](#️-requirements)
- [📄 License ](#-license)
- [✍️ Authors ](#️-authors)

## 🧐 About <a name = "about"></a>

A GitHub Action for securely retrieving secrets from PSONO server.

## 🎈 Usage <a name="usage"></a>

```yaml
jobs:
  my-job:
    runs-on: ubuntu-latest
    steps:
      - name: Fetch secrets from PSONO
        id: psono-secrets
        uses: jfheinric-eu/psono-secret-whisperer@v1
        with:
            ci_api_key_id: ${{ secrets.CI_API_KEY_ID }}
            ci_api_key_secret_hex: ${{ secrets.CI_API_KEY_SECRET_HEX }}
            ci_server_url: 'https://your-psono-server.com'
            secret_id: ${{ secrets.SECRET_ID }}
            secret_type: 'env'
            secret_fields: 'API_KEY,DATABASE_URL,OTHER_SECRET'
            mask_secrets: 'API_KEY,OTHER_SECRET'
            # The first field (secret1) will be accessible as "api_key
            # the other two will be still accessible as "secret2" and "secret3"
            custom_field_names: 'api_key'

      # Access secrets
      - name: Use secrets
        run: |
          echo "API Key: ${{ steps.psono-secrets.outputs.api_key }}"
          echo "Database URL: ${{ steps.psono-secrets.outputs.secret2 }}"
```

## ➡️ Inputs <a name="inputs"></a>

| Input                   | Description                                           | Required | Default           |
|-------------------------|-------------------------------------------------------|----------|-------------------|
| `ci_api_key_id`         | PSONO API key                                         | Yes      | -                 |
| `ci_api_key_secret_hex` | PSONO API key                                         | Yes      | -                 |
| `ci_server_url`         | URL of your PSONO server                              | Yes      | -                 |
| `secret_id`             | secret id to fetch                                    | Yes      | -                 |
| `secret_fields`         | Comma-separated list of secret keys to retrieve       | No       | username,password |
| `mask_secrets`          | Comma-separated list of secret keys to masked         | No       | -                 |
| `custom_field_names`    | Comma-separated list of output field names            | No       | -                 |

## ⬅️ Outputs <a name="outputs"></a>

The action provides following outputs:

Output field from `secret1` till `secret10`. `secret1` is the value for the first field in `inputs.secret_fields` and so on.

If custom names are given, then the output field names are the given names.

## 🛡️ Security Recommendations <a name="security-recommendations"></a>

- Always use GitHub secrets to store your PSONO credentials
- Limit the secret keys you retrieve to only what you need
- Consider using GitHub's OIDC support for even more secure authentication

## ‼️ Requirements <a name="requirements"></a>

The action requires:
- A PSONO server that's accessible from GitHub Actions
- Valid PSONO credentials with access to the requested secrets

## 📄 License <a name="license"></a>

This GitHub Action is released under the [MIT License](LICENSE).

## ✍️ Authors <a name = "authors"></a>

- [@jfheinrich](https://github.com/jfheinrich) - Idea & Initial work
