# gupload - Google Drive CLI Uploader

Our motivation to create the **gupload** tool was the deployment of the GitLab CI artifacts to our Google Drive disk. The tool is not limited to this use-case though. It is a simple Python 3 command-line utility ingesting file names and their respective path arguments. Those are uploaded to Google Drive via Google service account (recommended approach by Google) and an optionally specified folder (through its ID).

The secret file is accessed via the environmental variable `GOOGLE_APPLICATION_CREDENTIALS` and it should be set prior the program execution:

    $ export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json

## Requirements

* Python 3 + PIP
* Enabled Google Drive API (you can do it in the Google Cloud Console)
* Google service account (you can do it in the Google Cloud Console)
* Credential JSON file to the service account
* Configured environmental variable `GOOGLE_APPLICATION_CREDENTIALS` to the service account credentials

## Installation

Install/upgrade the tool from PyPI using:

    $ pip3 install --upgrade gupload

## Usage

    $ gupload --help
    Usage: gupload [OPTIONS]

    Options:
    -d, --folder ID            Target folder identifier.
    -f, --file <NAME PATH>...  Input file(s) to be uploaded.
    --version                  Show the version and exit.
    --help                     Show this message and exit.

Example:

    $ gupload --folder 1OQ3lq2O1zqZ01vUgzvg1iyXXtBJRl6pW --file a.out ../a.out --file changelog.txt ../changelog.txt

Output:

    Uploading file: a.out
    Uploading file: changelog.txt

## Contributing

Please read [**CONTRIBUTING.md**](https://github.com/hardwario/gupload/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [**SemVer**](https://semver.org/) for versioning. For the versions available, see the [**tags on this repository**](https://github.com/hardwario/gupload/tags).

## Authors

* [**Pavel Hübner**](https://github.com/hubpav) - Initial work

## License

This project is licensed under the [**MIT License**](https://opensource.org/licenses/MIT/) - see the [**LICENSE**](https://github.com/hardwario/gupload/blob/master/LICENSE) file for details.
