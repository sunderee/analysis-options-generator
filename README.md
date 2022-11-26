# Dart Analysis Options Generator

Tool for automatically populating `analysis_options.yaml` file with all the available linting rules described by the
[official documentation](https://dart.dev/tools/linter-rules). This is a Python-based CLI.

**Motivation:** although VSCode has a superb auto-complete functionality through Dart/Flutter plugins, newly generated
Dart/Flutter projects are missing `analysis_options.yaml` file with pre-populated linting rules and their explanations
(similarly to how TypeScript does it with `tsconfig.json`). As a result, many developers don't configure their linter in
accordance to the best practices, and manual configuration takes time.

This is an opinionated generator, and will (by default) set the severity to every enabled rule to `error`.

## Usage

First you'll have to generate `rules.json` file; which is just a file of all the rules with some additional information
associated with them. The reason why we're doing this, is because there's no reason to run costly (and lengthy) HTTP
operation with every time you're generating `analysis_options.yaml` file for your next project. You can always
regenerate it.

```bash
# Create virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Run setup.py script
python3 setup.py
```

Now you can use the `main.py` script. Use `--help` flag to see how it works.

```bash
python3 main.py --help
```

You need to provide the absolute path to the directory in which you want to generate the `analysis_options.yaml` file.
Then, using `--rule-sets` flag you choose one of the three preferred rule sets. Lastly, with `--soft-mode` turned on,
you set the severity of each rule to warning, not error (which is the default severity).

## Further information and details

*Disclaimer: this section is heavily based on the official documentation on linting rules.*

Some rules can be fixed automatically using **quick fixes**. A quick fix is an automated edit targeted at fixing the
issue reported by the linter rule. If the rule has a quick fix, it can be applied
using [`dart fix`](https://dart.dev/tools/dart-fix) or using your editor with Dart support. To learn more,
see [Quick fixes for analysis issues](https://medium.com/dartlang/quick-fixes-for-analysis-issues-c10df084971a).

### Rule sets

There are three rule sets:

1. Core
2. Recommended
3. Flutter

There are two official packages available: [`lints`](https://pub.dev/packages/lints)
and [`flutter_lints`](https://pub.dev/packages/flutter_lints). In order to understand what these rule sets are, let's
look at the explanation from the official documentation.

1. `lints` contains two rule sets curated by the Dart team. We recommend using at least the **core** rule set, which is
   used when scoring packages uploaded to pub.dev. Or, better yet, use the **recommended** rule set, a superset of **
   core** that identifies additional issues and enforces style and format. If you’re writing Flutter code, use the rule
   set in the `flutter_lints` package, which builds on `lints`.
2. `flutter_lints`: contains the **Flutter** rule set, which the Flutter team encourages you to use in Flutter apps,
   packages, and plugins. This rule set is a superset of the **recommended** set, which is itself a superset of the **
   core** set that partially determines the score of packages uploaded to pub.dev.

Meaning that **core** rule set is the bare-minimum rule set that every Dart/Flutter application should follow. **
Recommended** is a superset of **core**, and it brings additional linting rules promoted by Dart/Flutter teams. **
Flutter** is a set of rules that builds on top of **recommended** and **core** and is a bare-minimum to be used for
writing Flutter applications.

### Rule types

There are three rule types:

1. **Errors**: possible errors or mistakes in your code.
2. **Style**: matters of style, largely derived from
   the [Dart style guide](https://dart.dev/guides/language/effective-dart/style).
3. **Pub**: possible issues with [pub package setup](https://dart.dev/guides/packages).

### Maturity levels

Each rule has a maturity level:

1. **Stable**: these rules are safe to use and are verified as functional with the latest versions of the Dart language.
   All
   rules are considered stable unless they’re marked as experimental or deprecated.
2. **Experimental**: these rules are still under evaluation and might never be stabilized. Use these with caution and
   report
   any issues you come across.
3. **Deprecated**: these rules are no longer suggested for use and might be removed in a future linter release.

### Severity

Each analyzer error code and linter rule has a default severity. You can use the analysis options file to change the
severity of individual rules, or to always ignore some rules. The analyzer supports three severity levels:

1. `info`: an informational message that doesn't cause analysis to fail.
2. `warning`: a warning that doesn't cause analysis to fail unless the analyzer is configured to treat warnings as
   errors.
3. `error`: an error that causes analysis to fail.