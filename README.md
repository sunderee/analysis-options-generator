# Dart Analysis Options Generator

Tool for automatically populating `analysis_options.yaml` file with all the available linting rules described by the
[official documentation](https://dart.dev/tools/linter-rules). This is a Python-based CLI.

**Motivation:** although VSCode has a superb auto-complete functionality through Dart/Flutter plugins, newly generated
Dart/Flutter projects are missing "analysis_options.yaml" file with pre-populated linting rules and their explanations
(similarly to how TypeScript does it with `tsconfig.json`). As a result, many developers don't configure their linter in
accordance to the best practices, and manual configuration takes time.

**Heavy work in progress.**