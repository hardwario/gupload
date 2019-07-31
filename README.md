# gupload - Google Drive CLI Uploader

[![Travis](https://img.shields.io/travis/hardwario/gupload/master.svg)](https://travis-ci.org/hardwario/gupload)
[![Release](https://img.shields.io/github/release/hardwario/gupload.svg)](https://github.com/hardwario/gupload/releases)
[![License](https://img.shields.io/github/license/hardwario/gupload.svg)](https://github.com/hardwario/gupload/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/gupload.svg)](https://pypi.org/project/gupload/)


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
    Usage: gupload [OPTIONS] [FILES]...

    Options:
    --to ID                    Target folder identifier.  [required]
    -f, --file <NAME PATH>...  Input file(s) to be uploaded.
    -n, --nono                 No action: print names of files to be upload, but
                                don't upload.
    --version                  Show the version and exit.
    --help                     Show this message and exit.


## Example:

### Upload and rename

    $ gupload --folder 1OQ3lq2O1zqZ01vUgzvg1iyXXtBJRl6pW --file a.out ../a.out --file changelog.txt ../changelog.txt

Output:

    Uploading file: a.out
    Uploading file: changelog.txt


### Upload all zip files

    $ gupload --folder 1OQ3lq2O1zqZ01vUgzvg1iyXXtBJRl6pW *.zip

Output:

    Uploading file: a.zip
    Uploading file: b.zip

### Combination

    $ gupload --folder 1OQ3lq2O1zqZ01vUgzvg1iyXXtBJRl6pW --file changelog.txt ../changelog.txt *.zip

Output:

    Uploading file: changelog.txt
    Uploading file: a.zip
    Uploading file: b.zip

## Contributing

Please read [**CONTRIBUTING.md**](https://github.com/hardwario/gupload/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [**SemVer**](https://semver.org/) for versioning. For the versions available, see the [**tags on this repository**](https://github.com/hardwario/gupload/tags).

## Authors

* [**Pavel Hübner**](https://github.com/hubpav) - Initial work
* [**Karel Blavka**](https://github.com/blavka) - Extension

## License

This project is licensed under the [**MIT License**](https://opensource.org/licenses/MIT/) - see the [**LICENSE**](https://github.com/hardwario/gupload/blob/master/LICENSE) file for details.
