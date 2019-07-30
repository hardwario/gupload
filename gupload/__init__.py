'Google Drive CLI Uploader'

import apiclient
import click
import googleapiclient.discovery

__version__ = 'v1.0.1'


@click.command()
@click.option('-d', '--folder', help='Target folder identifier.', metavar='ID')
@click.option('-f', '--file', 'files', nargs=2,
              type=click.Tuple([str, click.File('rb')]),
              multiple=True, help='Input file(s) to be uploaded.',
              metavar='<NAME PATH>...')
@click.version_option(version=__version__)
def main(folder, files):
    try:
        service = googleapiclient.discovery.build('drive', 'v3')
        for name, file in files:
            click.echo('Uploading file: {}'.format(name))
            body = {'name': name}
            if folder is not None:
                body['parents'] = [folder]
            media_body = apiclient.http.MediaIoBaseUpload(
                file, mimetype='application/octet-stream')
            service.files().create(
                body=body, media_body=media_body, fields='id').execute()
    except KeyboardInterrupt:
        pass
