# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v1.2.0] - 2025-11-18
### :bug: Bug Fixes
- [`b18aa61`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/b18aa61ea5ebfaf7cfb9eba40928203c5c906742) - correct typos and formatting in README.md *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`b79b7df`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/b79b7df1396213f5a749fa93376f2aa9e94accb9) - correct spelling error in README.md *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :recycle: Refactors
- [`f683596`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/f6835963f8d25050f48d48e38989a45555c0e4aa) - reorganize workflows and scripts for better maintainability and clarity *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`d0c6b98`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/d0c6b98a808a5ae1dc30924430f6090f348217ae) - improve error handling and code readability in scripts *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`e511d30`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/e511d30d8a3be1658745d90318f049c7bcbdc315) - **deps**: bump actions/labeler from 5 to 6 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*


## [v1.1.0] - 2025-08-20
### :sparkles: New Features
- [`dbd6bad`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/dbd6bad47fb0a1cc3773b21d7d3887a50a4e4395) - add pull request labeler workflow and configuration *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`9945015`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/994501579791f22ae7a4bfc7cd51f7ada254e007) - add job summary generation and set status *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`0767346`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/0767346aa60fa5d624f79c09206c146a4bbb4c6f) - add environment variable OPENAI_MODEL *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :bug: Bug Fixes
- [`168d41e`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/168d41eb89a2663417aa9d737bdf4cbfb3298daa) - update datetime handling and integrate OpenAI client for report generation *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`ed5f338`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/ed5f338b8dd37595b3641479801686d25541cb6a) - update prettier version to v3.1.2 in pre-commit configuration *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`d398f1e`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/d398f1e7f597d99d5cb343cbe3b9c1f29a337295) - update pre-commit hooks and their versions in configuration *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`fb1ab92`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/fb1ab9257f13ae023f89c3f473742971df3c696e) - remove prettier hook from pre-commit configuration *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`caddc81`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/caddc81a3682b55d0b497ab5a9dd954b4080c11f) - format long lines in main.py for better readability *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`a0f072b`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/a0f072b5cccfbbcaa20d299745d41db6fe51efe1) - remove black hook from pre-commit configuration and improve line formatting in main.py *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`0b289e4`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/0b289e43d2eba92933ac9b968a3c34f8046707d9) - improve prompt formatting in GPT analysis function for better readability *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`b2c0ceb`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/b2c0cebc2e73b55b15fe54d4282885d6ddb64758) - correct typo in dependabot check condition *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`166ffea`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/166ffea3b870dd712cab4bf692236e601802c8bf) - Potential fix for code scanning alert no. 13: Workflow does not contain permissions *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`8f8d6f8`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/8f8d6f825c5a8b6f9523738226d702aa961933a6) - add environment for setup-secrets *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`84b56a9`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/84b56a94eed203356a558b4cfde6f7b10b8580bf) - resolve variable name issues *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`eb9c492`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/eb9c4928dc5c869439386b1bd74eb15c8245a372) - Update integration.yml *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`fc5da59`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/fc5da59e1abb36e3d6788b78f0572904a506172d) - update AI - Model to gpt-4.1 *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`4ae64ef`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/4ae64ef108925111fd492bfafcc7b3b0d9b123bf) - update workflow naming *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`6ae973f`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/6ae973fc224585acd0ec90bc71a5229c32870ed5) - Skip integration tests for dependabot PRs *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`e0bf45e`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/e0bf45e09ef4940df4217980ffa4c37b676ee04b) - resolve review issues *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`83c43f0`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/83c43f0f1cdac90fca9fc4479476a7f83bc6c262) - update messages in workflows to English for consistency *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`10c2c83`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/10c2c837ba1c2a39d2740135e01ee17be0cb03e7) - correct typo in success message in integration workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`c18d5f8`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/c18d5f89142838c51e7353cc4dab323e83969741) - remove unnecessary blank lines in workflow files *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`115e3a5`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/115e3a5093a13e613ad71656ca9efea86d63c0cc) - update release workflow to trigger on push and check for merge commits *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`828fc06`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/828fc069ff838a2b3c4ba123f8110ab77ee89c05) - Apply suggestions from code review *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`7e48187`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/7e481874785d3008fb3c8ccae2df198a746c5058) - enhance PR number retrieval in release workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`69aba68`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/69aba6836ebf92a832046ad5189623d98f783ffb) - remove redundant merge commit check and setup secrets step in release workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`7d9e489`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/7d9e489dcdab9507f3de3ffde00e7cf80381ced8) - enhance PR detection logic in release workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`9b8f805`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/9b8f805d9991567cd28d0d60326ea2ff0ad37d5f) - Apply suggestions from code review *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`0cb876e`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/0cb876ee561b7506d802411bb7a9323225e133ae) - Apply suggestions from code review, Part 2 *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`f8d2f8f`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/f8d2f8f03935dbc8ffb0058dccfd87eb2ec73aad) - streamline PR label checking logic in release workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`0a7b0d1`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/0a7b0d1b80b598a47d419334dee18eaa4cd28b8c) - Apply suggestions from code review (round 3) *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`5b2bb02`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/5b2bb022f1273b3ef5278c8d6fb5148dc4ea51a8) - enhance PR validation logic and skip reasons in release workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :recycle: Refactors
- [`327a076`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/327a0769b7268cbe346b3b9341af2db5ff53c239) - remove unnecessary validation jobs from PR workflows *(commit by [@jfheinrich](https://github.com/jfheinrich))*

### :wrench: Chores
- [`66e2a22`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/66e2a221afbc21632fa4ab5090089ae5656a640b) - **deps**: bump actions/setup-python from 5.5.0 to 5.6.0 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`2a3f7e2`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/2a3f7e266c24722bca7955a00b50ae78fb72dd2e) - **deps**: bump jefflinse/pr-semver-bump from 1.7.2 to 1.7.3 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`c8a421c`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/c8a421cb99d65e608c8c90ae75bdb519c4ed230c) - add daily-report *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`900d224`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/900d224c052cbfa4b9e60fd735a8f8354b88f315) - **deps**: add openai *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`babec47`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/babec472788fa88f1b0e180868ce05871d08a346) - remove unnecessary comment from daily report workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`1a7f2dc`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/1a7f2dccae094cada64f5c25639e2f9344e7248e) - add permissions section to daily report workflow *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`2ea8553`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/2ea8553d62786738ad92f8291d4eb8e6f21c5d61) - add pre-commit to the list of Python packages installed *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`bc71c26`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/bc71c2653612464a5066068cb7c80227cda2dcfe) - **deps**: bump stefanzweifel/git-auto-commit-action from 5 to 6 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`9b499b5`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/9b499b5d952bbbb4efed01075ccb42494dc98651) - **deps**: bump actions/checkout from 3 to 4 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`0ca9dc9`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/0ca9dc964e3accff4a74f769558e288ef497ce2e) - **deps**: bump actions/setup-python from 4 to 5 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`78b20ea`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/78b20ea3e7cb839d88b6838b966b0fc9899a4e8b) - **deps**: bump actions/checkout from 4 to 5 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`522506d`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/522506d34938d2d267f82308a9c5a02da61419ba) - **deps**: bump jfheinrich-eu/pipreqs-action from 4.1.0 to 4.4.0 *(commit by [@dependabot[bot]](https://github.com/apps/dependabot))*
- [`de9959c`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/de9959cd5fa3b87d36a0ec1cf42d97e1f96ba64a) - Entferne Daily Report Skript und zugehörige Workflow-Dateien *(commit by [@jfheinrich](https://github.com/jfheinrich))*
- [`124c696`](https://github.com/jfheinrich-eu/psono-secret-whisperer/commit/124c69622147b24b4bbe29dd2ed4872fb438c72c) - **deps**: update actions/checkout to v5 *(commit by [@jfheinrich](https://github.com/jfheinrich))*

[v1.1.0]: https://github.com/jfheinrich-eu/psono-secret-whisperer/compare/v1.0.0...v1.1.0
[v1.2.0]: https://github.com/jfheinrich-eu/psono-secret-whisperer/compare/v1.1.0...v1.2.0
