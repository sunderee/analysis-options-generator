# Dart Analysis Options Generator

Python-based CLI tool for automatically populating analysis_options.yaml file with all the available linting rules
described by the [official documentation](https://dart.dev/tools/linter-rules).

**Motivation**: although VSCode has superb auto-complete functionality through Dart/Flutter plugins, newly generated
Dart/Flutter projects are missing analysis options file with pre-populated linting rules and their explanations (similar
to how TypeScript does it with `tsconfig.json`). As a result, many developers don't configure their linter following
best
practices, and manual configuration takes time.

This is an opinionated generator and will (by default) set the severity to every enabled rule to `error`.

## Usage

First, create the virtual environment and install dependencies from `requirements.txt`. Next, run the PyInstaller in
order to produce an executable. You can name it whatever you want, `analysis-gen` is what I'll call it.

```bash
# Create virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Generate an executable
pyinstaller --onefile --name=analysis-gen main.py
```

This should produce a CLI executable found in `dist/analysis-gen`. At this point, you can use it however you like. My
suggestion is to create an alias.

```bash
alias analysis-gen="/absolute/path/to/dist/analysis-gen"
```

If you want to learn how to use the CLI, refer to the help message (`analysis-gen --help`):

```
$ analysis-gen --help
usage: analysis-gen [-h] [-r {core,recommended,flutter}] -p PATH [-s]

Tool for automatically populating analysis_options.yaml file with all the available linting rules described by the official documentation.

options:
  -h, --help            show this help message and exit
  -r {core,recommended,flutter}, --rule-set {core,recommended,flutter}
                        Sets the rule set that analysis_options.yaml will contain. Defaults to core.
  -p PATH, --path PATH  Absolute path to where you want to generate the analysis_options.yaml file
  -s, --soft-mode       Sets the severity of enabled linting rules to "warning"
```

## Further information and details

*Disclaimer: this section is copied from the official documentation. No need to reinvent the wheel if Google already
wrote things concisely enough. Knowing that people typically don't click on the links, I took some liberty to bring the
documentation to you.*

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