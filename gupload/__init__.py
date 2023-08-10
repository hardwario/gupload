'Google Drive CLI Uploader'

import apiclient
import click
import googleapiclient.discovery
import os

__version__ = 'v1.2.0'


@click.command()
@click.option('--to', help='Target folder identifier.', metavar='ID', required=True)
@click.option('-f', '--file', 'ofiles', nargs=2,
              type=click.Tuple([str, click.File('rb', lazy=True)]),
              multiple=True, help='Input file(s) to be uploaded.',
              metavar='<NAME PATH>...')
@click.option('-n', '--nono', help="No action: print names of files to be upload, but don't upload.", is_flag=True)
@click.option('--no-duplicates', 
              help="If the target folder contains a folder with the same name, update instead of creating a new file.",
              is_flag=True)
@click.argument('files', nargs=-1, type=click.File('rb', lazy=True))
@click.version_option(version=__version__)
def main(to, ofiles, nono, no_duplicates, files):
    try:
        service = googleapiclient.discovery.build('drive', 'v3') if not nono else None

        def get_files_in_folder():
            q = "'1DIW_yd5NuW3AUOdrtaTECBNPFBb0zphw' in parents"
            response = service.files().list(q=q).execute()
            return {file["name"]: file["id"] for file in response["files"]}

        def upload(name, fd):
            if fd.name != name:
                click.echo('Uploading file: {} as: {}'.format(fd.name, name))
            else:
                click.echo('Uploading file: {}'.format(name))

            if nono:
                return

            body = {'name': name}
            if to is not None:
                body['parents'] = [to]
            media_body = apiclient.http.MediaIoBaseUpload(fd, mimetype='application/octet-stream')
            service.files().create(body=body,
                                   media_body=media_body,
                                   fields='id').execute()
            
        def update(name, id, fd):
            click.echo('Updating existing file: {}'.format(name))

            if nono:
                return

            body = {'name': name}
            media_body = apiclient.http.MediaIoBaseUpload(fd, mimetype='application/octet-stream')
            service.files().update(fileId=id,
                                   media_body=media_body).execute()

        file_ids_by_name = {}
        if no_duplicates:
            file_ids_by_name = get_files_in_folder()
        
        for name, fd in ofiles:
            if no_duplicates and name in file_ids_by_name:
                file_id = file_ids_by_name[name]
                update(name, file_id, fd)
            else:
                upload(name, fd)

        for fd in files:
            name = os.path.basename(fd.name)
            if no_duplicates and name in file_ids_by_name:
                file_id = file_ids_by_name[name]
                update(name, file_id, fd)
            else:
                upload(name, fd)

    except KeyboardInterrupt:
        pass
